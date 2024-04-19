#Importing relevant and required libaries to process this project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import cufflinks as cf

telecom_df = pd.read_csv("telecom_customer_churn.csv")

print(telecom_df.head())
print(telecom_df.shape)
print(telecom_df.columns)

