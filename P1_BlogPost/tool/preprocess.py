#!/usr/bin/env python
#-*-coding:utf-8 -*-

import pandas as pd
import numpy as np
from collections import defaultdict
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import make_scorer, fbeta_score, f1_score, r2_score, mean_squared_error
from sklearn.decomposition import  PCA

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
        X, data.loc[index_train, pred_column], test_size=0.2, random_state=42,
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

def dummy_variables(data, columns, pred_column=None):
    """Deal with the dummy variables
    Convert the dummy variables into values

    Parameters:
        data: dataframe
            original data
        columns: list
            List contains column those will be used to predict value
        pred_column: string default None
            Need to be predicted missing value in the column
        algo: objects about algorithm
            List contains algorithm that will be used to train the model,
            and predict the missing value
        params: dict
            It is used to search the best parameters by gridsearchcv
        cv: int
            It is uded to a parameter in GridSearchCV
    Results:
        data: dataframe
            Dummy variables is converted into values
        columns: 
        index_missing: Index
            pred_column with missing values index
        index_train: Index
            columns with non_missing values index is used to train model
    """
    if pred_column:
        data = data[columns + [pred_column]].copy()
        index_missing = data[pred_column].isnull()
        index_train = data[pred_column].notnull()
    else:
        data = data[columns].copy()
        index_missing = None
        index_train = None

    category_column = data[columns].select_dtypes("object").columns

    for column in category_column:
        data = data.join(pd.get_dummies(data[column], drop_first=True, prefix=column))
        data.drop(column, inplace=True, axis=1)
        columns.remove(column)

    return data, columns, index_missing, index_train

def predict_numerical_value(
    data, columns, pred_column, algo, params, cv=2, pca_components=None, 
    metrics_func=None
):
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
        pca_compnents: int default None
            If it is a validate int number, there is a pca decomposition step
        metircs_func: Callable default None
            Use another metrics to measure the model, if it exists
    Results:
        pred_column value
    """
    data = data.copy()
    new_data, new_columns, index_missing, index_train = dummy_variables(
        data, columns, pred_column
    )
    
    train_X, test_X, train_y, test_y = train_test_split(
        new_data.loc[index_train, new_columns], new_data.loc[index_train, pred_column], 
        test_size=0.2, random_state=42
    )
    predict_X = new_data.loc[index_missing, new_columns]

    if pca_components:
        pca = PCA(n_components=pca_components)
        pca.fit(train_X)
        train_X = pca.transform(train_X)
        test_X = pca.transform(test_X)
        predict_X = pca.transform(predict_X)

        print("After decomposition with {} components PCA.".format(pca_components))


    # make the score metrics, basic metrics is r2 and mse
    score = {
         "mse": make_scorer(mean_squared_error, greater_is_better=False),
        "r2": make_scorer(r2_score, greater_is_better=True) 
    }

    if metrics_func:
        for key, value in metrics_func:
            score[key] = value
    
    if params:
        algorithm = GridSearchCV(
            algo, param_grid=params, scoring=score, iid=False, cv=cv, refit="mse"
        )
    else:
        algorithm = algo
    
    algorithm.fit(train_X, train_y)
    print("The train data r2 score is {:0.4f}.\nTest mse score is {:0.4f}. ".format(
        r2_score(train_y, algorithm.predict(train_X)), 
        mean_squared_error(test_y, algorithm.predict(test_X)))
    )
    
    y_missing = algorithm.predict(predict_X)
    data.loc[index_missing, pred_column] = y_missing
    
    return data.loc[:, pred_column]

def rmspe(y_true, y_predict):
    """Measurement metric
    Use the rmspe to validate model

    Parameters:
        y_true: array
            True labels
        y_predict: array
            Predict labels
        
    Results:
        result: float
            Evaluation score RMSPE
    """
    if not(isinstance(y_predict, (np.ndarray, pd.core.series.Series)) and \
        isinstance(y_true, (np.ndarray, pd.core.series.Series))):
        raise TypeError("The type of y_true and y_predict must be ndarray, Series!")

    if len(y_true) != len(y_predict):
        raise ValueError("Length between y_predict and y_true isn't same!")

    n = len(y_predict)
    percent = (y_true - y_predict) / y_true

    score = np.sqrt(np.power(percent, 2).sum() * 1/n)
    
    return score