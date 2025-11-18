"""
Helper Functions for E-commerce Analytics

This module contains utility functions that can be reused across different notebooks.
"""

import pandas as pd
import numpy as np


def detect_user_column(df):
    """
    Auto-detect user ID column from dataframe.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Input dataframe
    
    Returns:
    --------
    str or None
        Column name if found, None otherwise
    """
    candidates = [c for c in df.columns 
                  if any(k in c.lower() for k in ["user", "customer", "client", "buyer"])]
    return candidates[0] if candidates else None


def detect_revenue_column(df, numeric_cols=None):
    """
    Auto-detect revenue/amount column from dataframe.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Input dataframe
    numeric_cols : list, optional
        List of numeric column names. If None, will be auto-detected.
    
    Returns:
    --------
    str or None
        Column name if found, None otherwise
    """
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    candidates = [c for c in df.columns
                  if any(k in c.lower() for k in ["revenue", "amount", "price", "sales", 
                                                   "purchase", "order_value", "total"])]
    # Keep only numeric ones for safety
    candidates = [c for c in candidates if c in numeric_cols]
    return candidates[0] if candidates else None


def calculate_iqr_outliers(series):
    """
    Calculate outliers using IQR method.
    
    Parameters:
    -----------
    series : pandas.Series
        Input series
    
    Returns:
    --------
    tuple
        (lower_bound, upper_bound, outlier_count)
    """
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = series[(series < lower_bound) | (series > upper_bound)]
    outlier_count = outliers.shape[0]
    
    return lower_bound, upper_bound, outlier_count


def create_age_groups(df, age_col, bins=None, labels=None):
    """
    Create age groups from age column.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Input dataframe
    age_col : str
        Name of age column
    bins : list, optional
        Age bin edges. Default: [0, 18, 25, 35, 45, 60, 120]
    labels : list, optional
        Age group labels. Default: ["<18", "18-24", "25-34", "35-44", "45-59", "60+"]
    
    Returns:
    --------
    pandas.DataFrame
        Dataframe with added 'age_group' column
    """
    if bins is None:
        bins = [0, 18, 25, 35, 45, 60, 120]
    if labels is None:
        labels = ["<18", "18-24", "25-34", "35-44", "45-59", "60+"]
    
    df = df.copy()
    df["age_group"] = pd.cut(df[age_col], bins=bins, labels=labels, right=False)
    return df

