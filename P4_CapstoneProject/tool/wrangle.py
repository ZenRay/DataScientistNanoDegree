#!/user/bin/env python
#-*-coding:utf-8-*-

import pandas as pd
import numpy as np
import re


class Wrangle:
    """Wrangle the data
    Wrangle the data about the capstone project
    """
    
    def __init__(self, data, columns):
        """Initialize an instance
        Initialize the data and the columns to deal with specific data

        Parameters:
        -----------
        data: pandas data
            It maybe a DataFrame or a Series
        columns: label or labels
            The labels are abnormal features in the data
        """
        self.data = data
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