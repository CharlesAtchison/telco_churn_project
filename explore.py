
import matplotlib.pyplot as plt

import seaborn as sns


def make_heatmap(train, target):
    cols = [col for col in train.columns if col not in [target]]
    X = train[cols]        #independent columns
    y = train[target]    #target column i.e survived

    # get correlations of each features in dataset
    corrmat = train.corr()
    top_corr_features = corrmat.index
    plt.figure(figsize=(20,20)) 

    # plot heat map
    sns.heatmap(train[top_corr_features].corr(),annot=True,cmap="RdYlGn")
    return corrmat[target].sort_values()



