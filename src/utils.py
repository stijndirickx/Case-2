import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def display_info(df):
    """
    Display basic information about a DataFrame.
    
    Parameters:
        df (DataFrame): Input DataFrame
    
    Returns:
        None
    """
    print("DataFrame Info:")
    print("-" * 30)
    print(df.info())
    print("\n")
    print("DataFrame Shape:")
    print("-" * 30)
    print(df.shape)
    print("\n")
    print("Missing Values:")
    print("-" * 30)
    print(df.isnull().sum())
    print("\n")

def display_summary_stats(df):
    """
    Display summary statistics of a DataFrame.
    
    Parameters:
        df (DataFrame): Input DataFrame
    
    Returns:
        None
    """
    print("Summary Statistics:")
    print("-" * 30)
    print(df.describe())
    print("\n")

def display_unique_values(df, columns=None):
    """
    Display unique values for specified columns of a DataFrame.
    If no columns are specified, display unique values for all columns.
    
    Parameters:
        df (DataFrame): Input DataFrame
        columns (list, optional): List of column names to display unique values
    
    Returns:
        None
    """
    if columns is None:
        columns = df.columns
    
    for col in columns:
        unique_values = df[col].unique()
        print(f"Unique values in {col}: {unique_values}")
        print("\n")

def display_value_counts(df, columns=None):
    """
    Display value counts for specified columns of a DataFrame.
    If no columns are specified, display value counts for all columns.
    
    Parameters:
        df (DataFrame): Input DataFrame
        columns (list, optional): List of column names to display value counts
    
    Returns:
        None
    """
    if columns is None:
        columns = df.columns
    
    for col in columns:
        value_counts = df[col].value_counts()
        print(f"Value counts for {col}:")
        print(value_counts)
        print("\n")

def plot_histogram(df, column):
    """
    Plot a histogram for a specified column in the DataFrame.
    
    Parameters:
        df (DataFrame): Input DataFrame
        column (str): Column name for which to plot the histogram
    
    Returns:
        None
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], bins=20, kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_boxplot(df, x_column, y_column):
    """
    Plot a boxplot for a specified column in the DataFrame.
    
    Parameters:
        df (DataFrame): Input DataFrame
        x_column (str): Column name for the x-axis
        y_column (str): Column name for the y-axis
    
    Returns:
        None
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=x_column, y=y_column, data=df)
    plt.title(f'Boxplot of {y_column} grouped by {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()