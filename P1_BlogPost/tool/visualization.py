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
    data, by, calculate_columns, func, new_field="type", by_value=None, 
    by_field="condition", melt_var_name="variable", melt_value_name="value"
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
            A value put into new_field, if it's not None. Otherwise, use the by
            as the value
        by_field: string default condition
            A label name is used to change the label name that is create by 
            reset_index
        melt_var_name: string default variable
            A label name is used to change the label name that is a parameter 
            var_name in melt method
        melt_value_name: string default value
            A label name is used to change the label name that is a parameter 
            value_name in melt method
    Results:
        result: DataFrame
            A prepared DataFrame will be used to concate

    Examples:
    ---------
    >>> data.groupby("amenity_internet")[["price", "reviews"]].mean() \
    ...     .reset_index()
    	amenity_internet   	price	    reviews
    0	    False	    109.839506      38.416481
    1	    True	    128.349051	    56.378976

    >>> group_for_concat(
        data, "amenity_internet", ["price", "reviews"],np.mean, 
        by_value="internet"
    )
        type	condition	variable	value
    0	internet	False	price	109.839506
    1	internet	True	price	128.349051
    2	internet	False	reviews	38.416481
    3	internet	True	reviews	56.378976
    """
    data = data.copy()

    if by_value is None:
        by_value = by

    result = data.groupby(by=by)[calculate_columns].apply(func).reset_index()

    result = result.melt(
        id_vars=by, value_vars=calculate_columns, var_name=melt_var_name,
        value_name=melt_value_name
    )
    
    result[new_field] = by_value
    result.rename({by:by_field}, inplace=True, axis=1)
    return result[[new_field, by_field, melt_var_name, melt_value_name]]