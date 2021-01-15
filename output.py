import tkinter
import tkinter as tk
from tkinter import *
import area
from area import ScrollableFrame

class Output():

    def begin(self, total_time: [], approximate_roots_lists: [], index_dictionary: [],iterations_list:[],method_list:[], precision):
        root = tk.Tk()
        print(iterations_list)

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
            print(iteration.values)
            values=iteration.values
            errors=iteration.errors
            max_error=iteration.max_error

            keys_list = list(index_dictionary)

            listBox = Listbox(frame.scrollable_frame, height=1, width=53, font=20)
            listBox.insert(END, f"iteration {i+1}")
            listBox.pack(pady=20, padx=50)
            for j in range(len(values)):
                value=values[j]
                error=errors[j]
                listBox = Listbox(frame.scrollable_frame, height=2, width=53, font=20)
                listBox.insert(1, f" {keys_list[j]} : {value}")
                listBox.insert(2, f"Error of {keys_list[j]} : {error}")
                listBox.pack(pady=20, padx=50)

            listBox = Listbox(frame.scrollable_frame, height=1, width=53, font=20)
            listBox.insert(END, f"Max error : {max_error}")
            listBox.pack(pady=20, padx=50)



        frame.pack()
    def list_box(self,string,frame):
        listBox = Listbox(frame, height=1, width=53, font=20)
        listBox.insert(END, string)
        listBox.pack(pady=20, padx=50)

    def make_label_pack_vertical(self,rootObject, tk, text, font):
        tk.Label(rootObject,
                 text=text,
                 justify=tk.CENTER,
                 padx=0,
                 font=font,
                 pady=15).pack()
