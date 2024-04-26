
def remove_outliers(column):
    if column.name != "Timestamp":
        Q1 = column.quantile(0.25)
        Q3 = column.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return column[(column >= lower_bound) & (column <= upper_bound)]
    else:
        return column
    
def cleaner(df):    
    df_no_outliers = df.apply(remove_outliers)
    cleanData = df_no_outliers[(df_no_outliers['GHI'] >= 0) & (df_no_outliers['DNI'] >= 0) & (df_no_outliers['DHI'] >= 0)]
    return cleanData
