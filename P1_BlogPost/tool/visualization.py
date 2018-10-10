#!/usr/bin/env python
#-*-coding:utf-8 -*-

import pandas as pd
import numpy as np

def parse_amenity(
    data, amenity, target_field, field="amenities", inplace=False, silence=False
):
    """Parse the amenity value
    If the amenity exits, return True, otherwise False

    Parameters:
        data: DataFrame
            Origin DataFrame contains amenities
        amenity: string
            The amenity value is used to check whether it exits
        target_field: string
            The new field store the parse information
        field: string default amenities
            The field is in data, the default value is amenities
        inplace: boolean default False
            If True, fill in place. 
        silence: boolean default False
            If it is True, silence the warning and sort, and force parse value.
    Results:
        result: Series
            Accordding to the amenity value, it exits then return True, when 
            inplace is False
    """
    try:
        if amenity and amenity in data[field].unique():
            result = data[field].str.contains(amenity)
        else:
            raise ValueError("Value couldn't be parsed, because {} is not in {}". \
                format(amenity, field))
    except ValueError as error:
        if silence:
            result = data[field].str.contains(amenity)
        else:
            raise error

    if inplace:
        data[target_field] = result
    else:
        return result

def group_for_concat(
    data, by, calulate_columns, func, new_field="type", by_value=None
):
    """Group by the field, prepare the data to concate

    Parameters:
        data: DataFrame
            Origin DataFrame
        by: string
            Used to determine the groups for the groupby. It is a column label
        calulate_columns: list
            The fields in columns is used to caculate
        fun: function
            It is a aggregate function, like sum, mean
        new_field: string
            A new label name, store the by value 
        by_value: string default None
            A value put into new_field, if it's not None
    Results:
        result: DataFrame
            A prepared DataFrame will be used to concate
    """
            