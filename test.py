import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

print("Todo instalado correctamente")
print("Versión de pandas:", pd.__version__)
print("Versión de numpy:", np.__version__)
print("Versión de matplotlib:", mpl.__version__)
print("Versión de seaborn:", sns.__version__)

help(plt.versions)

# Configuración visual
plt.style.use("seaborn-v0_8")
sns.set_palette("pastel")

# Carga de dataset
df = pd.read_csv("DataCoSupplyChainDataset.csv", encoding="latin1")

print("\nColumnas disponibles en el dataset:")
print(df.columns.tolist())
