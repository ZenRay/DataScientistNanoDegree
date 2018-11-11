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