import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('veri.csv', sep=';')

plt.scatter(df['Boy'], df['Kilo'], color="yellow")
plt.title("boy ve Kilo Dağılımı")
plt.xlabel("boy")
plt.ylabel("Kilo")
plt.show()

plt.bar(df["Boy"], df["Kilo"], color="orange")
plt.title(" Boy ve Kilo Bar Grafiği")
plt.xlabel("Boy")
plt.ylabel("Kilo")
plt.xticks(rotation=45)
plt.show()