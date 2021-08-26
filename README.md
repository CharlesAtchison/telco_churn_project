<center><h1>Telco Churn Project</h1></center>


<h1 name='toc'>Table of Contents</h1>

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
10. 
<hr style="border-top: 10px groove tan; margin-top: 5px; margin-bottom: 5px"></hr>

### Project Summary <a name='project_summary'></a>
<hr style="border-top: 10px groove tan; margin-top: 5px; margin-bottom: 5px"></hr>

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

| Feature                | Datatype               | Definition   |
|:-----------------------|:-----------------------|:-------------|
| churn                  | 7049 non-null: object  |defines if the customer has churned|



| Feature                | Datatype               | Definition   |
|:-----------------------|:-----------------------|:-------------|
| customer_id            | 7049 non-null: object  |unique int for each customer|
| gender                 | 7049 non-null: object  |specifies the gender|
| is_senior_citizen      | 7049 non-null: int64   |identifies if customer is senior citizen|
| partner                | 7049 non-null: object  |if customer has a partner
| dependents             | 7049 non-null: object  |if customer has dependents|
| phone_service          | 7049 non-null: int64   |if customer has phone service|
| internet_service       | 7049 non-null: int64   |if customer has internet service|
| contract_type          | 7049 non-null: int64   |defines contract service|
| payment_type           | 7049 non-null: object  |defines the payment type|
| monthly_charges        | 7049 non-null: float64 |average monthly charges|
| total_charges          | 7038 non-null: float64 |total revenue from customer|
| tenure                 | 7049 non-null: int64   |number of months the customer has been with company|
| is_female              | 7049 non-null: bool    |defines if the customer is female
| has_churned            | 7049 non-null: bool    |defines if the customer has churned|
| has_phone              | 7049 non-null: bool    |defines if the customer has phone services|
| has_internet           | 7049 non-null: bool    |defines if the customer has internet|
| has_phone_and_internet | 7049 non-null: bool    |defines if the customer has internet and phone|
| partner_depenents      | 7049 non-null: int64   |defines if the customer has partner and dependents|
| start_date             | 7049 non-null: object  |date customer joined company|
| avg_monthly_charges    | 7049 non-null: object  |average monthly charges|
| matches_orig           | 7049 non-null: object  |does it match avg month charges|
| phone description      | 7049 non-null: object  |number of lines|
| internet_desciption    | 7049 non-null: object  |internet service type|
| contract_description   | 7049 non-null: object  |contract type and length|
    
    
<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>

