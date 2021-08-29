from env import user, password, host
from sklearn.model_selection import train_test_split
import pandas as pd
import os


def get_db_url(username: str, hostname: str , password: str, database_name: str):
    '''
    Takes username, hostname, password and database_name and 
    returns a connection string
    '''
    connection = f'mysql+pymysql://{username}:{password}@{hostname}/{database_name}'
    
    return connection


def get_telco_data():
    filename = "telco_data.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=[0])

    else:
        conn = get_db_url(username=user, password=password, hostname=host, database_name='telco_churn')
        
        sql = '''
        select customer_id, gender, senior_citizen, partner, dependents,
        tenure, phone_service, multiple_lines, online_security, online_backup,
        device_protection, tech_support, streaming_tv, streaming_movies,
        paperless_billing, monthly_charges, total_charges, churn, contract_type,
        internet_service_type, payment_type
        from customers
        join contract_types
        using (contract_type_id)
        join internet_service_types
        using (internet_service_type_id)
        join payment_types
        using (payment_type_id)
        '''
        df = pd.read_sql(sql, conn)

        df.to_csv(filename)

        return df

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


def fetch_data_dict(telco_df):
    ''' Fetches and formats a data_dict to put into project README.md
    returns two pandas DataFrame formatted markdown.
    '''

    data_dict = {
        'customer_id':'unique customer identifier',
        'gender':'identifies customer gender',
        'senior_citizen':'describes if customer is senior citizen',
        'partner':'describes if customer has a partner',
        'dependents':'describes if customer has dependents',
        'tenure':'quantifies length of serivce from customer',
        'phone_service'	:'describes if customer has phone service',
        'multiple_lines':'describes if customer has multiple phone lines',
        'online_security':'describes if customer has online security',
        'online_backup':'describes if customer has online backup',
        'device_protection':'describes if customer has device protection',
        'tech_support':'describes if customer has tech support',
        'streaming_tv':'describes if customer has tv streaming',
        'streaming_movies':'describes if customer has movie streaming',
        'paperless_billing':'describes if customer uses paperless billing',
        'monthly_charges':'quantifies average monthly charges',
        'total_charges':'quantifies all charges for customer',
        'contract_type':'describes customer contract type',
        'internet_service_type':'describes customer internet service type',
        'payment_type':'describes customer service payment type',
        'churn':'describes if the customer has churned'
                }
    feature_dict = pd.DataFrame([{'Feature': col, 
         'Datatype': f'{telco_df[col].count()} non-null: {telco_df[col].dtype}',
        'Definition' : data_dict[col]} for col in telco_df.columns]).set_index('Feature').to_markdown()
    target_dict = pd.DataFrame([{'Target': col, 
         'Datatype': f'{telco_df[col].count()} non-null: {telco_df[col].dtype}',
        'Definition' : data_dict[col]} for col in telco_df.columns if col == 'churn']).set_index('Target').to_markdown()
    return (target_dict, feature_dict)
