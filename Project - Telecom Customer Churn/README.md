# Telekommunikationskundenabwanderung - Analyse und Visualisierung

## Überblick

Dieses Projekt befasst sich mit der Analyse und Visualisierung von Daten über Telekommunikationskundenabwanderung. Ziel ist es, Einblicke in die Faktoren zu gewinnen, die Kunden dazu veranlassen, den Dienst eines Telekommunikationsunternehmens zu kündigen.

## Schritte

### 1. Import relevanter Bibliotheken und Laden der Daten

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import cufflinks as cf

telecom_df = pd.read_csv("telecom_customer_churn.csv")

# Überblick über die Daten
print(telecom_df.head())
print(telecom_df.shape)
print(telecom_df.columns)
