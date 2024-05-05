# Importing necessary libraries for data handling and visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import roc_curve, roc_auc_score, classification_report

# Enhancing display settings for better dataframe inspection
pd.set_option('display.max_columns', None)

# Load the dataset
telecom_df = pd.read_csv("files/telecom_customer_churn.csv")

# Output basic information about the dataset
print(telecom_df.info())
print(telecom_df.head())

# Saving a summary of the dataset to a text file
with open("data_summary.txt", "w") as file:
    file.write("Basic Dataset Info:\n")
    file.write(f"Number of rows: {telecom_df.shape[0]}\n")
    file.write(f"Number of columns: {telecom_df.shape[1]}\n\n")
    file.write("Column names and data types:\n")
    file.write(str(telecom_df.dtypes) + "\n\n")
    file.write("First 5 rows of the dataset:\n")
    file.write(str(telecom_df.head()) + "\n")

# Histogram of the dataset to understand distribution
plt.figure(figsize=(20, 30)) 
num_columns = telecom_df.select_dtypes(include=[np.number]).columns.size
rows = num_columns // 3 + (num_columns % 3 > 0)

for i, column in enumerate(telecom_df.select_dtypes(include=[np.number]).columns):
    plt.subplot(rows, 3, i + 1) 
    telecom_df[column].hist(bins=20)
    plt.title(column)
    plt.xticks(rotation=45)  
    plt.tight_layout()
plt.savefig('dataset_distributions.png')  
plt.close()

# Pie chart for the Churn distribution
churn_data = telecom_df['class'].value_counts().reset_index()
churn_data.columns = ['Churn Status', 'Count']
churn_data['Churn Status'] = churn_data['Churn Status'].map({0: 'Retained', 1: 'Churned'})

colors = {'Retained': '#636EFA', 'Churned': '#EF553B'}

fig = go.Figure(data=[go.Pie(labels=churn_data['Churn Status'], values=churn_data['Count'], hole=.3,
                             marker_colors=[colors[label] for label in churn_data['Churn Status']])])
fig.update_traces(textinfo='percent+label', textfont_size=20)

fig.update_layout(
    title_text='Churn Distribution Pie Chart',
    title_x=0.5,  # Zentriert den Titel
    legend_title="Churn Status",
    legend=dict(
        yanchor="bottom",
        y=0.01,
        xanchor="right",
        x=0.99
    )
)

fig.write_image('churn_distribution_pie_chart.png')

# Histogram for international plans related to churn status
data = telecom_df[['international_plan', 'class']].copy()
data['international_plan'] = data['international_plan'].map({0: 'No', 1: 'Yes'})  # Umcodierung für bessere Lesbarkeit
data['class'] = data['class'].map({0: 'Retained', 1: 'Churned'})  # Klarere Benennung der Churn-Status

fig = px.histogram(data, x='international_plan', color='class',
                   color_discrete_map={'Retained': '#636EFA', 'Churned': '#EF553B'},  # Ansprechendere Farben
                   barmode='group',  # 'group' für gruppierte Darstellung
                   title='International Plan Distribution by Churn Status',
                   labels={'class': 'Churn Status', 'count': 'Customer Count', 'international_plan': 'International Plan'},
                   category_orders={'international_plan': ['No', 'Yes'], 'class': ['Retained', 'Churned']},  # Ordnen der Kategorien
                   text_auto='.2s',  # Anzeigen der Zahlen auf den Balken, formatiert
                   )

fig.update_layout(
    xaxis_title="International Plan",
    yaxis_title="Customer Count",
    legend_title="Churn Status",
    legend=dict(
        yanchor="top",
        y=0.95,  
        xanchor="right",
        x=1
    )
)

fig.update_traces(textposition='outside')
fig.write_image('international_plan_distribution.png')

# Correlation Matrix
corr_matrix = telecom_df.corr()
plt.figure(figsize=(15, 15))
sns.heatmap(corr_matrix, annot=True, fmt="0.2f")
plt.title("Correlation Matrix of Telecom Customers", fontsize=20)
plt.savefig('correlation_matrix.png')

# Analysing churn by day charges
retain_data = telecom_df[telecom_df["class"] == 0]["total_day_charge"]
churn_data = telecom_df[telecom_df["class"] == 1]["total_day_charge"]

plt.figure(figsize=(10, 6))
sns.kdeplot(retain_data, color="red", fill=True, label="Retain")
sns.kdeplot(churn_data, color="blue", fill=True, label="Churn")
plt.legend()
plt.xlabel("Day Charges")
plt.ylabel("Density")
plt.title("Distribution of Day Charges by Churn")
plt.savefig('day_charges_distribution.png')

# Analysing churn by evening charges
retain_data = telecom_df[telecom_df["class"] == 0]["total_eve_charge"]
churn_data = telecom_df[telecom_df["class"] == 1]["total_eve_charge"]

plt.figure(figsize=(10, 6))
sns.kdeplot(retain_data, color="red", fill=True, label="Retain")
sns.kdeplot(churn_data, color="blue", fill=True, label="Churn")
plt.legend()
plt.xlabel("Evening Charges")
plt.ylabel("Density")
plt.title("Distribution of Evening Charges by Churn")
plt.savefig('evening_charges_distribution.png')

# Cross-table of state and churn
crossvar_city_churn = pd.crosstab(index=telecom_df['state'], columns=telecom_df['class'])
crossvar_city_churn = crossvar_city_churn.sort_values(by=1, ascending=False)

mask = telecom_df['class'] == 1

fig, ax = plt.subplots(figsize=(13, 9))
colors = ['purple', 'orange']
legend = ['No-Churn', 'Churn']
crossvar_city_churn.plot(kind='bar', alpha=0.7, color=colors, width=0.6, edgecolor='black', ax=ax, legend=True)
ax.set_xlabel(' ')
ax.set_ylabel('Share of cities %', fontsize=12, weight='bold')
ax.set_title('Total customers\' churn/ no-churn in the states', fontsize=12, weight='bold')
ax.set_xticklabels(crossvar_city_churn.index, rotation=45, ha='right', fontsize=8, weight='bold')
ax.legend(legend, fontsize=8, loc='upper left')
ax.text(s=f'Total customers: {telecom_df.shape[0]} and Total churn in the states: {telecom_df.loc[mask].shape[0]}',
        x=25, y=120, color='black', weight='bold', alpha=0.9, fontsize=10)
ax.yaxis.grid(which='major', linestyle='dashed', color='gray')
plt.savefig('state_churn_distribution.png')

# Preparing data for model training
X = telecom_df.drop('class', axis=1)
y = telecom_df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initializing and training models
model_lr = LogisticRegression()
model_rf = RandomForestClassifier()
model_nb = GaussianNB()
model_lr.fit(X_train_scaled, y_train)
model_rf.fit(X_train_scaled, y_train)
model_nb.fit(X_train_scaled, y_train)

# Evaluate models and write detailed performance metrics to a text file
with open("detailed_model_performance.txt", "w") as file:
    models = [model_lr, model_rf, model_nb]
    model_names = ['Logistic Regression', 'Random Forest', 'Naive Bayes']
    
    for model, name in zip(models, model_names):
        predictions = model.predict(X_test_scaled)
        report = classification_report(y_test, predictions, target_names=['Not Churned', 'Churned'])
        file.write(f"{name} Model Performance:\n")
        file.write(report + "\n\n")

# Generating and plotting ROC curves
fpr_lr, tpr_lr, _ = roc_curve(y_test, model_lr.predict_proba(X_test_scaled)[:, 1], pos_label=1)
fpr_rf, tpr_rf, _ = roc_curve(y_test, model_rf.predict_proba(X_test_scaled)[:, 1], pos_label=1)
fpr_nb, tpr_nb, _ = roc_curve(y_test, model_nb.predict_proba(X_test_scaled)[:, 1], pos_label=1)
plt.figure()
plt.plot(fpr_lr, tpr_lr, label='Logistic Regression (AUC = {:.2f})'.format(roc_auc_score(y_test, model_lr.predict_proba(X_test_scaled)[:, 1])))
plt.plot(fpr_rf, tpr_rf, label='Random Forest (AUC = {:.2f})'.format(roc_auc_score(y_test, model_rf.predict_proba(X_test_scaled)[:, 1])))
plt.plot(fpr_nb, tpr_nb, label='Naive Bayes (AUC = {:.2f})'.format(roc_auc_score(y_test, model_nb.predict_proba(X_test_scaled)[:, 1])))
plt.title('ROC Curves Comparison')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc='lower right')
plt.savefig('roc_curves_comparison.png')

