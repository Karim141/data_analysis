# Telecom Customer Churn Analysis

## Project Overview
This project analyzes a dataset of telecommunications customers to identify patterns indicating whether customers are likely to cancel their service (Churn). Utilizing various data science techniques and machine learning models, this analysis provides insights into the drivers of customer churn and suggests preventive measures.

## Dataset
The dataset `telecom_customer_churn.csv` includes various customer attributes such as monthly charges, contract duration, and whether they have an international plan. The initial examination of the dataset is detailed in the `data_summary.txt` file. The dataset was sourced from [Kaggle](https://www.kaggle.com/datasets/mnassrib/telecom-churn-datasets/data?select=churn-bigml-20.csv).

### data_summary.txt
The file [`data_summary.txt`](./data_summary.txt) provides a basic overview of the dataset, including the number of rows and columns, data types of each column, and an excerpt of the first five rows. This information is crucial for gaining an initial understanding of the data structure.

## Visualizations
Several visualizations were created to analyze different aspects of the dataset more deeply.

### Dataset Distributions
The graphic [`dataset_distributions.png`](./dataset_distributions.png) displays the distribution of all numeric features in the dataset. These histograms are useful for identifying data scaling, potential outliers, and the need for normalization.

### Churn Distribution Pie Chart
The pie chart [`churn_distribution_pie_chart.png`](./churn_distribution_pie_chart.png) visually represents the ratio of customers who have stayed versus those who have churned. This quick overview of the churn rate is essential for understanding the extent of the issue.

### International Plan Distribution
The histogram [`international_plan_distribution.png`](./international_plan_distribution.png) specifically examines the impact of having an international plan on churn rates. Customers with an international plan might exhibit a higher churn rate due to higher costs or specific needs.

### Pairplots
The pairplots in [`pairplot.png`](./pairplot.png) provide a comprehensive view of the relationships between various features. Color differentiation by customer retention status allows for easy identification of patterns and correlations.

### ROC Curves Comparison
The graphic [`roc_curves_comparison.png`](./roc_curves_comparison.png) displays the Receiver Operating Characteristic (ROC) curves for each trained model. These curves are critical for assessing the models' effectiveness in distinguishing between churned and retained customers.

## Models
Three models were trained to predict the likelihood of customer churn: Logistic Regression, Random Forest, and Naive Bayes. Each model was evaluated to determine its suitability for predicting customer churn.

### detailed_model_performance.txt
The file [`detailed_model_performance.txt`](./detailed_model_performance.txt) contains detailed performance evaluations of these models. The report includes metrics such as Precision, Recall, and F1-Score, which help understand the accuracy and reliability of each model.

## Interpretations and Conclusions
The analysis clearly shows that certain features like the international plan and monthly charges correlate significantly with customer churn. Notably, a higher churn rate among customers with an international plan could indicate potential dissatisfaction with costs or services.

The ROC curve comparison indicates that the Random Forest model performs the best with the highest AUC, suggesting it most effectively differentiates between churned and retained customers.

## Recommendations
Based on the findings, we recommend telecommunications companies:
- Review and possibly adjust the pricing and benefits of the international plan to enhance customer satisfaction.
- Develop targeted customer retention programs aimed at customers at high risk of churn.

## Executing the Project
To replicate or further develop this project, clone the repository and execute the Python script. Utilize the extensive comments in the script to make adjustments or conduct additional analyses.
