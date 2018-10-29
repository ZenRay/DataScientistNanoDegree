import sys
import pandas as pd
from sqlalchemy import create_engine
import os

def load_data(messages_filepath, categories_filepath):
    """Load the original dataset

    Load the dataset from the specific file, and transform the dataset into the 
    same dataframe

    Parameters:
    -----------
    messages_filepath: string
        File path is about messages data
    categories_filepath: string
        File path is about categories data
    
    Results:
    df: DataFrame
        Dataset is loaded from the messages and the categories dataset
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    # merge the dataframe
    df = messages.merge(categories, on="id")

    return df

def clean_data(df):
    """Wrangle data
    
    Wrangle the dataframe

    Parameters:
    df: DataFrame
        DataFrame contains all data infromation
    
    Returns:
    df: DataFrame
        After cleaning the dataframe, return itself
    """
    # extract the categories info
    category = df["categories"].str.split(";", expand=True)

    category_colnames = category.iloc[0, :].apply(lambda x: x.split("-")[0])
    category.columns = category_colnames

    for column in category:
        # parse the value from the string
        category[column] = category[column].apply(lambda x: x.split("-")[1])
        category[column] = pd.to_numeric(category[column])

    # concate the category info and the dataframe
    df.drop("categories", axis=1, inplace=True)

    df = pd.concat([df, category], axis=1)

    # drop duplicates
    if df.duplicated().sum() > 0:
        df.drop_duplicates(inplace=True)

    return df

def save_data(df, database_filename):
    """Save the dataset

    After cleaning the dataset, store the data into the SQLite database

    Paramters:
    ----------
    df: DataFrame
        Cleaning data
    database_filename: String
        File path is about the database stored the data
    """
    engine = create_engine("sqlite:///" + database_filename)
    db_name = os.path.basename(database_filename).split(".")[0]
    try:
        df.to_sql(db_name, engine, index=False)
    except ValueError as error:
        print(error)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()