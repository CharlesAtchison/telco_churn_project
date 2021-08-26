# Telco Churn Project

<a name='toc'></a>
## Table of Contents
1. [Project Summary](#project_summary)
    1. [Project Objectives](#project_objectives)
    2. [Business Goals](#business_goals)
    3. [Audience](#audience)
    4. [Deliverables](#deliverables)
    5. [Data Dictonary](#data_dict)
3. [Executive Summary](#exe_summ)
2. [Data Acqisition](#data_acquisition)
5. [Preparation](#preparation)
6. [Exploratory Data Analysis](#exp_data_analysis)
2. [Drivers of Churn](#drivers_of_churn)
3. [Machine Learning Construction](#ml_construction)
7. [Statistical Testing](#stat_testing)
8. [Modeling](#modeling)
9. [Model Evaluation](#model_eval)

<hr style="border-top: 10px groove tan; margin-top: 5px; margin-bottom: 5px"></hr>

<a name='project_summary'></a>
## Project Summary

<a name='project_objectives'></a>
### Project Objectives 
> - Create a Jupyter Notebook Report that shows processes and analysis with the goal of finding drivers for customer churn.
> - Within README.md file, include project description with goals, inital hypotheses, a data dictonary, project planning, instructions on how to recreate your project, answers to hypotheses, key findings, recommendations, and takeaways from the project.
> - CSV file with customer_id, probabilty of churn, and prediction of churn (1 = churn, 0 = not_churn). These predictions will be dervied from the best performing model on the test portion of the data. 
> - Any abstracted modules that are created to make the presentation more clean, during the acquistion and preparation of data.
> - Notebook walkthrough and presentation with a high-level overview of the entire project.

<a name='business_goals'></a>
### Business Goals 
> - Find drivers for customer churn at Telco. Why are customers churning?
> - Construct a machine-learning classification model that accurately predicts customer churn.
> - Document your process well enough to be presented or read like a report.

<a name='audience'></a>
### Audience 
> - Target audience is the Codeup Data Science Team.

<a name='deliverables'></a>
### Deliverables
> - A final report within Juypter Notebooks
> - A final report presentation using Juypter Notebooks
> - Modules necessary to recreate project

<a name='data_dict'></a>
### Data Dictionary

| Target                | Datatype               | Definition   |
|:----------------------|:-----------------------|:-------------|
| churn                 | 7043 non-null: object  |describes if the customer has churned|




| Feature               | Datatype               | Definition   |
|:----------------------|:-----------------------|:-------------|
| customer_id           | 7043 non-null: object  |unique customer identifier|
| gender                | 7043 non-null: object  |identifies customer gender|
| senior_citizen        | 7043 non-null: int64   |describes if customer is senior citizen|
| partner               | 7043 non-null: object  |describes if customer has a partner|
| dependents            | 7043 non-null: object  |describes if customer has dependents|
| tenure                | 7043 non-null: int64   |quantifies length of serivce from customer|
| phone_service         | 7043 non-null: object  |describes if customer has phone service|
| multiple_lines        | 7043 non-null: object  |describes if customer has multiple phone lines|
| online_security       | 7043 non-null: object  |describes if customer has online security|
| online_backup         | 7043 non-null: object  |describes if customer has online backup|
| device_protection     | 7043 non-null: object  |describes if customer has device protection|
| tech_support          | 7043 non-null: object  |describes if customer has tech support|
| streaming_tv          | 7043 non-null: object  |describes if customer has tv streaming|
| streaming_movies      | 7043 non-null: object  |describes if customer has movie streaming|
| paperless_billing     | 7043 non-null: object  |describes if customer uses paperless billing|
| monthly_charges       | 7043 non-null: float64 |quantifies average monthly charges|
| total_charges         | 7043 non-null: object  |quantifies all charges for customer|
| contract_type         | 7043 non-null: object  |describes customer contract type|
| internet_service_type | 7043 non-null: object  |describes customer internet service type|
| payment_type          | 7043 non-null: object  |describes customer service payment type|
    
    
<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>

