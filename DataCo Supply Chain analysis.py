import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Exploración inicial

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

# ----------------------------------------------------------------
# Creación de nuevas columnas
# ----------------------------------------------------------------

# Conversión de fechas
if "order date (DateOrders)" in df.columns and "shipping date (DateOrders)" in df.columns:
    df["Lead_Time_Days"] = (
        pd.to_datetime(df["shipping date (DateOrders)"], errors="coerce")
        - pd.to_datetime(df["order date (DateOrders)"], errors="coerce")
    ).dt.days

"""# 1. Lead Time (el tiempo entre orden y envío)

if "order date (DateOrders)" in df.columns and "shipping date (DateOrders)" in df.columns:
    df["Lead_Time_Days"] = (df["shipping date (DateOrders)"] - df["order date (DateOrders)"]).dt.days

#2 Shipping Delay (el tiempo entre envío y entrega)
if "shipping date (DateOrders)" in df.columns and "Delivery Date" in df.columns:
    df["Shipping_Delay_Days"] = (df["Delivery Date"] - df["shipping date (DateOrders)"]).dt.days

# 3. Order Duration (tiempo entre envío y entrega)
if "order date (DateOrders)" in df.columns and "Delivery Date" in df.columns:
    df["Order_Duration_Days"] = (df["Delivery Date"] - df["order date (DateOrders)"]).dt.days

# 4. Marca de pedidos retrasados (Late Delivery Flag)
if "Shipping_Delay_Days" in df.columns:
    df["Is_Delayed"] = df["Shipping_Delay_Days"].apply(lambda x: 1 if x is not None and x > 7 else 0)"""

if "Late_delivery_risk" in df.columns:
    df["Is_Delayed"] = df["Late_delivery_risk"]
    
# 5. Revisión de columnas nuevas
print("\nNuevas columnas creadas:")
print(df[["Lead_Time_Days", "Shipping_Delay_Days", "Order_Duration_Days", "Is_Delayed"]].head())

# 6 Gráfico de distribución de retrasos
if "Is_Delayed" in df.columns:
    plt.figure(figsize=(5,4))
    sns.countplot(x="Is_Delayed", data=df)
    plt.title("Pedidos retrasados (1 = Sí, 0 = No)")
    plt.show()