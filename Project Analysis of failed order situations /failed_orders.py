import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data_orders.csv")


#Question 1
df['order_result'] = df.apply(lambda row: 'Cancelled Before Driver' if row['cancellations_time_in_seconds'] and not row['is_driver_assigned_key'] 
                              else ('Cancelled After Driver' if row['cancellations_time_in_seconds'] and row['is_driver_assigned_key'] 
                                else 'Not Cancelled'), axis=1)

order_distribution = df['order_result'].value_counts()

sns.set(style="white")  # Hinzufügen von Gitterlinien
colors = sns.color_palette("viridis")  # Verwendung einer stilvollen Farbpalette

# Diagramm erstellen
plt.figure(figsize=(8, 6))  # Größenanpassung des Diagramms
sns.barplot(x=order_distribution.index, y=order_distribution.values, palette=colors, width=0.4)
plt.title('Verteilung der Bestellungen nach Gründen für das Scheitern', fontsize=14)
plt.xlabel('Bestellergebnis', fontsize=14)
plt.ylabel('Anzahl der Bestellungen', fontsize=14)
plt.xticks(rotation=0, ha='center')  # Schriftartanpassungen für x-Achse
plt.yticks(range(0, max(order_distribution.values) + 1000, 2000), fontsize=12)
plt.tight_layout()  # Optimierung des Layouts
sns.despine(left=True, right=True, top=True, bottom=True)  # Achsenlinien entfernen



#Question 2

df["order_datetime"] = pd.to_datetime(df["order_datetime"], format="%H:%M:%S")

failed_orders = df[df["order_status_key"] == 4]
failed_orders["hour"] = failed_orders["order_datetime"].dt.hour

plt.figure(figsize=(8,6))
sns.histplot(data=failed_orders, x="hour",hue="is_driver_assigned_key", bins=24, multiple="stack", palette="viridis")
plt.show()