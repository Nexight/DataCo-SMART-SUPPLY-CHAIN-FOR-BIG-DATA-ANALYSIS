import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("pandas:", pd.__version__)
print("numpy:", np.__version__)

# Configuración visual
plt.style.use("seaborn-v0_8")
sns.set_palette("pastel")

# Carga de dataset
df = pd.read_csv("DataCoSupplyChainDataset.csv", encoding="latin1")

# Exploración inicial
print("Dimensiones del dataset:", df.shape)
print("Primeras filas del dataset:\n")
print(df.head())

print("\nEstadísticas básicas:")
print(df.describe(include="all").transpose())

# Comprobación de valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

#Visualizacion rápida (ventas por región)
if "Order Region" in df.columns and "Sales" in df.columns:
    ventas_region = df.groupby("Order Region")["Sales"].sum().reset_index()

    plt.figure(figsize=(8,5))
    sns.barplot(x="Order Region", y="Sales", data=ventas_region)
    plt.title("Ventas totales por Región")
    plt.xticks(rotation=45)
    plt.show()
else:
    print("No se encontraron columnas 'Order Region' o 'Sales' en el dataset.")