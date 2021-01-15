import tkinter
import tkinter as tk
from tkinter import *
import area
from area import ScrollableFrame

class Output():
    def __init__(self):
        self.methods_list = ["Guass Seidel","Guass Elimination", "Guass Jordan",  "LU decomposition"]

    def begin(self, total_time: [], approximate_roots_lists: [], index_dictionary: [],iterations_list:[], precision):
        root = tk.Tk()
        print(iterations_list)

        canvas = tk.Canvas(root)
        scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

        frame = tk.Frame(canvas)
        for i in range(len(approximate_roots_lists)):
            self.render(frame,total_time[i], approximate_roots_lists[i], precision, index_dictionary, self.methods_list[i])

        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'),
                         yscrollcommand=scroll_y.set)

        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')
        root.geometry("500x650")
        root.mainloop()

    def render(self,root, time, approximate_roots, precision, index_dictionary, method_name):

        self.make_label_pack_vertical(root, tk, f"Method used : {method_name} ", 10)

        self.make_label_pack_vertical(root,tk,f"Execution time : {time} ms",10)
        self.make_label_pack_vertical(root,tk,f"Precision : {precision} %",10)
        self.make_label_pack_vertical(root,tk,"Approximate roots are :",10)
        self.make_table(root,approximate_roots,index_dictionary)
        self.make_label_pack_vertical(root,tk,"-----------------------------------------",10)


    def make_table(self, root, approximate_roots, index_dictionary):
        frame = ScrollableFrame(root)
        keys_list = list(index_dictionary)

        for i in range(len(approximate_roots)):
            listBox = Listbox(frame.scrollable_frame, height=1, width=53, font=20)
            listBox.insert(END, f" {keys_list[i]} : {approximate_roots[i]}")
            listBox.pack(pady=20,padx=50)


        frame.pack()



    def make_label_pack_vertical(self,rootObject, tk, text, font):
        tk.Label(rootObject,
                 text=text,
                 justify=tk.CENTER,
                 padx=0,
                 font=font,
                 pady=15).pack()
