
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.model_selection import GridSearchCV
from itertools import combinations
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
  
import warnings 

warnings.filterwarnings('ignore')



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



def most_accurate_attributes(X_train, X_validate, y_train, y_validate):
    most_accurate_comb = None
    accuracy = 0

    all_combs = list()
    for i in range(2, len(X_train.columns) + 1):
        all_combs.extend(set(list(combinations(X_train.columns, i))))

    tries = 0
    for combo in all_combs:
        if tries % 100 == 0:
            print(tries)
        X_Train = X_train[[*combo]]
        dc = DecisionTreeClassifier()
        rf = RandomForestClassifier(n_jobs=-1)
        knn = KNeighborsClassifier(n_jobs=-1)
        lr = LogisticRegression(n_jobs=-1)
        models = [dc, rf, knn, lr]
        for each_model in models:
            each_model.fit(X_Train, y_train)
            train_score = each_model.score(X_train[[*combo]], y_train)
            val_score = each_model.score(X_validate[[*combo]], y_validate)
            mean_score = (train_score + val_score) / 2
            if mean_score > accuracy:
                print(mean_score)
                most_accurate_comb = {each_model : combo}
                accuracy = mean_score
            tries += 1
            
    return (most_accurate_comb, accuracy)


def explore_validation_curve(X : pd.DataFrame, y : pd.DataFrame, param_grid : dict, model, cv=None, color_args={'train': ['black', 'orange'], 'test': ['red', 'cyan']}):
    '''Function that will print out plot of the single or multiple input hyperparameter(s) for the validation
    curves the plotted mean for each nth value and the standard deviation for each nth value. This requires
    some model generated and will return a sklearn.model_select.GridSearchCV class.

    
    Parameters
    ----------
    X : pandas DataFrame
        Some x_values dataframe to be put into the validation_curve.
    
    y : pandas DataFrame
        Some y_values dataframe to be put into the validation_curve.

    param_grid : str
        What hyperparmeter you would like to explore within the validation_curve and an associated numpy range.
        With each additional hyperparameter, you'll have combinatoric possibilities of 
        n!/r!(n − r)!, where r is the number of hyperparameters and n is the number
        of n values for each hyperparameter.

        format :
                        {
                            __some_hyperparameter__: __some_numpy_range__,
                            __some_hyperparameter__: __some_numpy_range__
                        }
        
        Examples
        --------
        Single Hyperparameter
        param_grid = {'n_estimators' : np.arange(1, 200, 2)}
        
        Multi Hyperparameter
        param_grid = {'n_estimators' : np.arange(1, 200, 2),
                      'max_depth' : np.arange(1, 13, 1)}

    
    model : Sklearn model
        Can check sklearn models, verified currently compatible with:
            DecisionTreeClassifier,
            RandomForestClassifier,
            KNeighborsClassifier
            
    cv : int, cross-validation generator or an iterable, default=None
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:

        - None, to use the default 5-fold cross validation,
        - integer, to specify the number of folds in a `(Stratified)KFold`,
        - :term:`CV splitter`,
        - An iterable yielding (train, test) splits as arrays of indices.

        For integer/None inputs, if the estimator is a classifier and ``y`` is
        either binary or multiclass, :class:`StratifiedKFold` is used. In all
        other cases, :class:`KFold` is used.


    color_args : dict
        Not required, default values:
        {'train': ['black', 'orange'],
         'test': ['red', 'cyan']}
        
        can personalize but must be in the format of
        # train_line    line_color      standard_dev fill color
        {'train}    :   ['black'     ,  'orange']

        # test_line    line_color      standard_dev fill color
        {'test'}    :   ['red'     ,  'cyan']

    Returns
    -------
    sklearn GridSearchCV
        The returned class is a the GridSearchCV with associated selectable attributes.
        
    
    Examples
    -------
    >>> param_grid = {'n_estimators' : np.arange(1, 200, 2),
                      'max_depth' : np.arange(1, 13, 1)}
                      
    >>> val = explore_validation_curve(X_train, y_train, param_grid, RandomForestClassifier())

    
    >>> print(type(val))
    
    <class 'sklearn.model_selection._search.GridSearchCV'>
    
    --------------------------------------------------------------------------------------------------

    >>> param_grid = {'n_estimators' : np.arange(1, 200, 2),
                      'max_depth' : np.arange(1, 13, 1)}
    
    >>> val = explore_validation_curve(X_train, y_train, param_grid, DecisionTreeClassifier(), cv=5,
                                color_args={'train': ['green', 'purple'],
                                            'test': ['orange', 'red']})
    >>> print(type(val))
    
    <class 'sklearn.model_selection._search.GridSearchCV'>

    --------------------------------------------------------------------------------------------------

    >>> param_grid = {'n_neighbors' : np.arange(1, 30, 2),
                      'max_depth' : np.arange(1, 13, 1)}
    
    >>> val = explore_validation_curve(X_train, y_train, param_grid, KNeighborsClassifier(), cv=5,
                                color_args={'train': ['green', 'purple'],
                                            'test': ['orange', 'red']})
    >>> print(type(val))
    
    <class 'sklearn.model_selection._search.GridSearchCV'>

    '''
    
    # Check that if the param_name is 'max_depth' that the range is not greater than the number of attributes in model.
    # if 'max_depth' in param_grid.keys() and len(param_grid['max_depth']) > X.shape[1]:
    #     raise Exception(f"Sorry, your range cannot be larger than the number of attributes ({X.shape[1]}) when using 'max_depth")
        
    # Calculate validation curve and return as array
    print('Starting grid search')
    grid = GridSearchCV(model, param_grid, cv=cv, return_train_score=True)
    print('fitting')
    grid.fit(X, y)

    ## Results from grid search
    results = grid.cv_results_
    means_test = results['mean_test_score']
    stds_test = results['std_test_score']
    means_train = results['mean_train_score']
    stds_train = results['std_train_score']

    ## Getting indexes of values per hyper-parameter
    masks=[]
    best_vals = dict()
    masks_names= list(grid.best_params_.keys())
    for p_k, p_v in grid.best_params_.items():
        best_vals[p_k] = p_v
        masks.append(list(results['param_'+p_k].data==p_v))

    params=grid.param_grid

    ## Ploting results
    pram_preformace_in_best = {}
    for i, p in enumerate(masks_names):
        plt.title(f'Validation Curve for {p}')
        # Check if there is only 1 hyperparameter to test
        if len(masks_names) > 1:
            # Stack the masks to find the best index
            m = np.stack(masks[:i] + masks[i+1:])
            pram_preformace_in_best
            best_parms_mask = m.all(axis=0)
            # Map the best index 
            best_index = np.where(best_parms_mask)[0]
        else:
            best_index = np.arange(len(means_test))
        x = np.array(params[p])
        # Find the test_mean and train mean for each hyperparameter
        test_mean = np.array(means_test[best_index])
        test_std = np.array(stds_test[best_index])
        train_mean = np.array(means_train[best_index])
        train_std = np.array(stds_train[best_index])
        best_mean = means_test[best_index][best_vals[p]-1]
        # Build the plot for each hyperparameter
        plt.plot(x, train_mean, label='Training score', color=color_args['train'][0])
        plt.plot(x, test_mean, label='Test score', color=color_args['test'][0])
        plt.fill_between(x, test_mean - test_std, test_mean + test_std, linestyle='--', label='test', color=color_args['test'][1])
        plt.fill_between(x, train_mean - train_std, train_mean + train_std, linestyle='-', label='train' , color=color_args['train'][1])
        plt.xlabel(p.upper())
        plt.ylabel('Accuracy')
        plt.legend(loc='best')
        plt.annotate(f'Best {p} at N = {best_vals[p]}\nat {best_mean:0.2f}',
            xy=(best_vals[p], best_mean), xycoords='data',
            xytext=(0, 20),
            textcoords='offset points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"))
        plt.show()
        
    print(grid.best_params_)

    # Return a GridSearchCV class with the associated attributes to examine.
    return grid