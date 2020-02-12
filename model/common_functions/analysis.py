def missing_percentage(df):
    """This function takes a DataFrame as input and returns two columns, total missing values and total missing values percentage"""
    import pandas as pd
    total = df.isnull().sum().sort_values(ascending = False)[df.isnull().sum().sort_values(ascending = False) > 0]
    percent = round(df.isnull().sum().sort_values(ascending = False)/len(df)*100,2)[round(df.isnull().sum().sort_values(ascending = False)/len(df)*100,2) > 0]
    return pd.concat([total, percent], axis=1, keys=['Total','Percent'])

def constant_baseline_rmsle(y):
    """Calculation of optimal constant value for RMSLE"""
    import numpy as np
    C = np.exp(np.sum(np.log(y + 1))/y.shape[0])-1
    return np.float32(C)[0]

def importance_beautify(importance, columns):
    """Catboost importance beautify - make models feautures subscribed"""
    impDict = {}
    for i in range(0, len(importance)):
        impDict[columns[i]]=importance[i]
    sorted(impDict.items(), key=lambda x: x[1], reverse=True)