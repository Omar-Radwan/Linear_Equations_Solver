import tkinter
import tkinter as tk
from tkinter import *
import area
from area import ScrollableFrame
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
NO_SOLUTION="No solution exists!"
INFINITE_SOLUTIONS="Infinite solutions!"
DIVISION_BY_ZERO="Division by zero!"
NOT_DIAGONALLY_DOMINANT="Can't be solved using Gauss seidel .. not diagonally dominant!"
class Output():
    def __init__(self):
        self.value_list=[]
        self.points=[]
        self.iterations=[i+1 for i in range(50)]

    def begin(self, total_time: [], approximate_roots_lists: [], index_dictionary: [],iterations_list:[],method_list:[], precision):
        root = tk.Tk()

        canvas = tk.Canvas(root)
        scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

        frame = tk.Frame(canvas)
        for i in range(len(approximate_roots_lists)):
            self.render(frame,total_time[i], approximate_roots_lists[i], precision, index_dictionary, method_list[i],iterations_list)

        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'),
                         yscrollcommand=scroll_y.set)

        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')
        root.geometry("500x650")
        root.mainloop()

    def render(self,root, time, approximate_roots, precision, index_dictionary, method_name,iterations_list):
        print(method_name)
        self.make_label_pack_vertical(root, tk, f"Method used : {method_name} ", 10)

        self.make_label_pack_vertical(root,tk,f"Execution time : {time} ms",10)
        self.make_label_pack_vertical(root,tk,f"Precision : {precision} %",10)
        self.make_label_pack_vertical(root,tk,"Approximate roots are :",10)
        self.make_table(root,approximate_roots,index_dictionary)
        if method_name=="Guass Seidel" or method_name=="All":
            self.make_label_pack_vertical(root,tk,"-----------------------------------------",10)
            self.iterations_table(root,iterations_list,index_dictionary)
            self.set_points()
            keys_list = list(index_dictionary)
            for i in range(len(self.points)):
                point=self.points[i]
                variable=keys_list[i]
                print(variable)
                self.graph(root,point,variable)
        self.make_label_pack_vertical(root,tk,"-----------------------------------------",10)


    def make_table(self, root, approximate_roots, index_dictionary):
        frame = ScrollableFrame(root)
        keys_list = list(index_dictionary)

        for i in range(len(approximate_roots)):
            listBox = Listbox(frame.scrollable_frame, height=1, width=53, font=20)
            listBox.insert(END, f" {keys_list[i]} : {approximate_roots[i]}")
            listBox.pack(pady=20,padx=50)


        frame.pack()


    def iterations_table(self,root,iterations_list,index_dictionary):
        frame = ScrollableFrame(root)


        for i in range(len(iterations_list)):
            iteration=iterations_list[i]
            values=iteration.values
            errors=iteration.errors
            max_error=iteration.max_error
            self.value_list.append(values)
            keys_list = list(index_dictionary)
            n=len(values)


            listBox = Listbox(frame.scrollable_frame, height=2*n+2, width=53, font=20)
            listBox.insert(1, f"iteration {i+1}")
            for j in range(len(values)):
                value=values[j]
                error=errors[j]
                listBox.insert(END, f" {keys_list[j]} : {value}")
                listBox.insert(END, f"Error of {keys_list[j]} : {error}")

            listBox.insert(END, f"Max error : {max_error}")
            listBox.pack(pady=20, padx=50)


        frame.pack()

    def graph(self,root,point,variable):
        print(self.iterations)
        data2 = {'iterations': self.iterations
            , variable: point
                 }
        df2 = DataFrame(data2, columns=[variable, 'iterations'])

        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, root)
        line2.get_tk_widget().pack(fill=tk.BOTH,pady=20)
        df2 = df2[['iterations', variable]].groupby('iterations').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
        ax2.set_title('variable Vs. iterations')


    def set_points(self):
        n = len(self.value_list[0])
        self.points = [[0 for j in range(50)] for i in range(n)]
        for i in range(len(self.points)):
            for j in range(len(self.value_list)):
                self.points[i][j] = self.value_list[j][i]

    def make_label_pack_vertical(self,rootObject, tk, text, font):
        tk.Label(rootObject,
                 text=text,
                 justify=tk.CENTER,
                 padx=0,
                 font=font,
                 pady=15).pack()
