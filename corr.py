 def getCorrelatedFeature(corrdata, threshold):
 '''
 To get the correlated features in a dataset according to a particular threshold in a dataset.
 Returns:
        A dataframe of features that their correlation is greater or equal to the particular threshold
 '''
    feature = []
    value = []
    for i, index in enumerate(corrdata.index):
        if  abs(corrdata[index]) > threshold:
            feature.append(index)
            value.append(corrdata[index])
    df = pd.DataFrame(data=value, index = feature, columns=['Corr Value'])
    return df
