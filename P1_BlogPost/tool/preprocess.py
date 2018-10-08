#!/usr/bin/env python
#-*-coding:utf-8 -*-

import pandas as pd
import numpy as np
from collections import defaultdict
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import make_scorer, fbeta_score, f1_score

def parse_money(data, column, dtype="float32"):
    sep_option = ["$", ","]
    replacement = ""

    for i in sep_option:
        data[column] = data[column].str.replace(i, replacement)

    return data[column].astype(dtype)

def option_count(data, option_column, value_column, options):
    '''Count the checkbox option value

    Paremeters:
        data: dataframe 
            where you want to search value from 
        option_column: string
            Column name want to look through, which contains option value
        value_column: string
            Column want to count values from, which is matched with option_column
        options: list
            Strings want to search for in each row 
    
    Result:
        result: dataframe
            each look_for with the count of how often it shows up 
    '''
    result = defaultdict(int)

    for option in options:
        for row in range(data.shape[0]):
            if option in data.loc[row, option_column]:
                result[option] += data.loc[row, value_column]
    
    result = pd.Series(result).reset_index()
    result.columns = [option_column, value_column]

    return result

def predict_category_value(data, columns, pred_column, algo, params, cv=2):
    """predict the missing value in pred_column

    Parameters:
        data: dataframe
            original data
        columns: list
            List contains column those will be used to predict value
        pred_column: string
            Need to be predicted missing value in the column
        algo: objects about algorithm
            List contains algorithm that will be used to train the model,
            and predict the missing value
        params: dict
            It is used to search the best parameters by gridsearchcv
        cv: int
            It is uded to a parameter in GridSearchCV
    Results:
        result: Series
            pred_column value
    """
    data = data[columns + [pred_column]].copy()
    index_missing = data[pred_column].isnull()
    index_train = data[pred_column].notnull()


    # dummy variable steps
    category_column = data[columns].select_dtypes("object").columns

    for column in category_column:
        data = data.join(pd.get_dummies(data[column], drop_first=True, prefix=column))
        data.drop(column, inplace=True, axis=1)
    
    X = data.loc[index_train, data.select_dtypes(exclude=["object"]).columns]
    
    train_X, test_X, train_y, test_y = train_test_split(
        X, data.loc[index_train, pred_column], test_size=0.5, random_state=42,
    )

    fscore = make_scorer(fbeta_score, beta=0.6, average="micro")
    grid_algo = GridSearchCV(algo, param_grid=params, scoring=fscore, iid=False, cv=cv)
    grid_algo.fit(train_X, train_y)
    print("The best estimater is {}".format(grid_algo.best_estimator_))
    print("The best f_0.5 score is %0.4f%%" % (grid_algo.best_score_ * 100))
    
    # validate the model
    test_predict = grid_algo.predict(test_X)
    score = fbeta_score(test_y, test_predict, beta=0.6, average="micro")
    print("The test f_0.5 score is %0.4f%%" % (score * 100))

    y_missing = grid_algo.predict(
        data.loc[index_missing, data.select_dtypes(exclude=["object"]).columns]
    )
    
    data.loc[index_missing, pred_column] = y_missing
    
    return data.loc[:, pred_column]