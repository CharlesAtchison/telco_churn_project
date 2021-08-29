def replace_obj_cols(daf: pd.DataFrame, dropna=False) -> (pd.DataFrame, dict, dict):
    '''Takes a DataFrame and will return a DataFrame that has
    all objects replaced with int values and the respective keys are return
    and a revert key is also generated.
    
    Parameters
    ----------
    
    df : pandas DataFrame
        Will take all object/str based column data types and convert their values
        to integers to be input into a ML algorithm.
    
    dropna: bool
        If this is True, it will drop all rows with any column that has NaN 
        
    Returns
    -------
    DataFrame 
        The returned DataFrame has all the str/object values replaced with integers
        
    dict - replace_key
        The returned replace_key shows what values replaced what str
        
    dict - revert_key
        The returned revert_key allows it to be put into a df.replace(revert_key) 
        to put all the original values back into the DataFrame
    
    Example
    -------
    >>>dt = {'Sex':['male', 'female', 'female', 'male', 'male'],
        'Room':['math', 'math', 'gym', 'gym', 'reading'],
        'Age':[11, 29, 15, 16, 14]}

    >>>test = pd.DataFrame(data=dt)
    
    >>>test, rk, revk  = replace_obj_cols(test)
       Sex  Room  Age
    0    0     0   11
    1    1     0   29
    2    1     1   15
    3    0     1   16
    4    0     2   14,
    
    {'Sex': {'male': 0, 'female': 1},
    'Room': {'math': 0, 'gym': 1, 'reading': 2}},
    
    {'Sex': {0: 'male', 1: 'female'},
    'Room': {0: 'math', 1: 'gym', 2: 'reading'}}
    
    >>>test.replace(revk, inplace=True)
          Sex     Room  Age
    0    male     math   11
    1  female     math   29
    2  female      gym   15
    3    male      gym   16
    4    male  reading   14
        
    '''
    df = daf.copy(deep=True)
    replace_key = {}
    revert_key = {}
    col_names = df.select_dtypes('object').columns
    if dropna:
        df.dropna(inplace=True)
    for col in col_names:
        uniques = list(df[col].unique())
        temp_dict = {}
        rev_dict = {}
        for each_att in uniques:
            temp_dict[each_att] = uniques.index(each_att)
            rev_dict[uniques.index(each_att)] = each_att
        replace_key[col] = temp_dict
        revert_key[col] = rev_dict
    df.replace(replace_key, inplace=True)
    
    return df, replace_key, revert_key