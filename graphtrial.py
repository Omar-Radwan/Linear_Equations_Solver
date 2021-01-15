import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


data2 = {'variable': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
         'iterations': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
         }
df2 = DataFrame(data2, columns=['variable', 'iterations'])


root = tk.Tk()


figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['variable', 'iterations']].groupby('variable').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
ax2.set_title('variable Vs. iterations')



root.mainloop()