import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

values = [[2, 3, 4], [5, 6, 7], [2, 2, 2], [4, 5, 6], [9, 10, 11]]
n = len(values[0])
points = [[0 for j in range(50)] for i in range(n)]
# values[0]=[2,3,4],[1]=[5,6,7]=>points[0]=[2,5],[1]=[3,6],[2]=[4,7]
for i in range(len(points)):
    for j in range(len(values)):
        points[i][j] = values[j][i]
for point in points:
    pass
    # print(point)
iterations = []
for i in range(50):
    iterations.append(i + 1)

data2 = {'iterations': iterations
    , 'variable': points[0]
         }
df2 = DataFrame(data2, columns=['variable', 'iterations'])

root = tk.Tk()

figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, pady=15)
df2 = df2[['iterations', 'variable']].groupby('iterations').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
ax2.set_title('variable Vs. iterations')

root.mainloop()
