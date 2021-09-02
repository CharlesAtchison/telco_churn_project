import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def show_dists(df):
    '''Takes dataframe and returns formatted tables for each column type.
    '''
    fix, axes = plt.subplots(10, 2, sharex=True, figsize=(10, 5))
    for n, col in enumerate(df.columns):
        print(n)
        if df[col].dtype != 'object':
            plt.hist(df[col])
            plt.title(f'Distribution of {col}')
            plt.show()

def show_violinplots(df, target):
    '''Takes train and target and returns violin plots for all metrics
    '''
    fig, axes = plt.subplots(10, 2, sharex=True, figsize=(10, 5))
    target_df = df[target].replace({0:'No', 1:'Yes'})
    for col in df.columns:
        if col != target:
            sns.violinplot(x=target_df, y=df[col])
            plt.title(f'{col.capitalize()} v {target.capitalize()} Plot')
            plt.xlabel(target.capitalize())
            plt.show()

def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test


def format_data_description(df):
    '''formats data and returns a new_df formatted and a markdown of the description
    '''
    # Replace total_charges with zero for those who don't have any tenure yet (AKA. new customers)
    df.total_charges.replace({' ': 0}, inplace=True)
    df.total_charges = df.total_charges.astype('float64')

    # Try to drop customer_id because each is a unique id and doesn't tell us any information about
    # each customer.
    customer_id_index = (df.customer_id).reset_index()
    try:
        df.drop(columns=['customer_id'], inplace=True)
    except:
        pass

    # Change column names to get more metrics within the columns and to input into ML modeling
    replace_key = {
    'gender': {'Female': 0, 'Male': 1},
    'partner': {'Yes': 1, 'No': 0},
    'dependents': {'Yes': 1, 'No': 0},
    'phone_service': {'Yes': 1, 'No': 0},
    'multiple_lines': {'Yes': 1, 'No phone service': 2, 'No': 0},
    'online_security': {'Yes': 1, 'No': 0, 'No internet service': 2},
    'online_backup': {'Yes': 1, 'No': 0, 'No internet service': 2},
    'device_protection': {'Yes': 1, 'No': 0, 'No internet service': 2},
    'tech_support': {'Yes': 1, 'No': 0, 'No internet service': 2},
    'streaming_tv': {'Yes': 1, 'No': 0, 'No internet service': 2},
    'streaming_movies': {'Yes': 1, 'No': 0, 'No internet service': 2},
    'paperless_billing': {'Yes': 1, 'No': 0},
    'churn': {'Yes': 1, 'No': 0},
    'contract_type': {'Two year': 0, 'One year': 1, 'Month-to-month': 2},
    'internet_service_type': {'DSL': 0, 'Fiber optic': 1, 'None': 2},
    'payment_type': {'Mailed check': 0, 'Credit card (automatic)': 1,
                     'Bank transfer (automatic)': 2, 'Electronic check': 3}
            }
    df.replace(to_replace=replace_key, inplace=True)

    return customer_id_index, df.describe().T.to_markdown()
