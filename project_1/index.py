import pandas as pd
import matplotlib.pyplot as plt

salvador_results = pd.read_csv('salvador_results.csv')
global_results = pd.read_csv('global_results.csv')

print(global_results)

df = pd.DataFrame(salvador_results)
df_global = pd.DataFrame(global_results)

df_global['Global'] = df_global['avg_temp'].rolling(window=10).mean()
df['Salvador'] = df['avg_temp'].rolling(window=10).mean()

plt.plot(df['year'], df['Salvador'],label='Salvador')
plt.plot(df_global['year'], df_global['Global'],label='Global')

plt.legend()

# show graph
plt.show()