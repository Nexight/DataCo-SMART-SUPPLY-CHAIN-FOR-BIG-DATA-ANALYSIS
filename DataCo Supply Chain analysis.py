import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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

#----------------------------------------------------------
# Creación de nuevas columnas 

# Convertir fechas
df["order_date"] = pd.to_datetime(df["order date (DateOrders)"], errors="coerce")
df["shipping_date"] = pd.to_datetime(df["shipping date (DateOrders)"], errors="coerce")

# 1. Lead Time (tiempo entre orden y envío)
df["Lead_Time_Days"] = (df["shipping_date"] - df["order_date"]).dt.days

# 2. Diferencia entre días reales y programados de envío
df["Shipping_Delay_Days"] = df["Days for shipping (real)"] - df["Days for shipment (scheduled)"]

# 3. Riesgo de retraso (me parece más fácil de interpretar)
df["Is_Delayed"] = df["Late_delivery_risk"]

# 4. duración total desde el pedido hasta el envío real.
df["Order_Duration_Days"] = df["Days for shipping (real)"]

# 5. Impresión de las nuevas columnas
print("\nNuevas columnas creadas:")
print(df[["Lead_Time_Days", "Shipping_Delay_Days", "Order_Duration_Days", "Is_Delayed"]].head())

# 6. Gráfico: Distribución de retrasos
plt.figure(figsize=(5,4))
sns.countplot(x="Is_Delayed", data=df)
plt.title("Pedidos retrasados (1 = Sí, 0 = No)")
plt.show()
