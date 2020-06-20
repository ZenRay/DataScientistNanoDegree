#!/user/bin/env python
#-*-coding:utf-8-*-

import pandas as pd
import numpy as np
import re


class Wrangle:
    """Wrangle the data
    Wrangle the data about the capstone project
    """
    
    def __init__(self, data, columns:list):
        """Initialize an instance
        Initialize the data and the columns to deal with specific data

        Parameters:
        -----------
        data: pandas data
            It maybe a DataFrame or a Series
        columns: label or labels
            The labels are abnormal features in the data
        """
        self.data = data.loc[:, columns]
        self.columns = columns

    def convert_time(self, column, fix=True):
        """Convert datatype
        Convert the object column into the datime column

        Parameters:
        column: label
            The object label is converted to a datetime dtype
        fix: boolean default True
            If true, drop the column from specific columns
        """

        if column not in self.columns:
            print("Hint: specific columns\n", self.columns)
            raise ValueError(
                "The label {} is not not specific columns".format(column)
            )

        result = pd.to_datetime(self.data[column])

        # update the columns
        if fix:
            self.columns.remove(column)
        
        return result


def fix_missing_value(x, sep=","):
    """Adjust the misssing value in description feature

    Parameters:
    -----------
    data: string
        A string contains a sep character
    sep: string
        A character is used as a seperator
    
    Results:
    -----------
    result: list
        A list contain the validate information
    """
    result = []
    if pd.notnull(x):
        if isinstance(x, int):
            result.append(x)
        else:
            result.extend([int(i.strip()) for i in x.split(sep)])
    
    return result