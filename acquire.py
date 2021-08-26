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