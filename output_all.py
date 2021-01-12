import tkinter
import tkinter as tk
from tkinter import *
import area
from area import ScrollableFrame

class OutputAll():


    def begin(self,time,approximate_roots,precision,index_dictionary):
        root = tk.Tk()

        self.make_label_pack_vertical(root,tk,f"Execution time : {time} ms",10)
        self.make_label_pack_vertical(root,tk,f"Precision : {precision} %",10)
        self.make_label_pack_vertical(root,tk,"Approximate roots are :",10)
        self.make_table(root,approximate_roots,index_dictionary)

        root.geometry("900x650")
        root.mainloop()



    def make_table(self,root,approximate_roots,index_dictionary):
        frame = ScrollableFrame(root)
        keys_list = list(index_dictionary)

        for i in range(len(approximate_roots)):
            listBox = Listbox(frame.scrollable_frame, height=1, width=53,font=20)
            listBox.insert(END,f" {keys_list[i]} : {approximate_roots[i]}")
            listBox.pack(pady=10)

        frame.pack()



    def make_label_pack_vertical(self,rootObject, tk, text, font):
        tk.Label(rootObject,
                 text=text,
                 justify=tk.CENTER,
                 padx=0,
                 font=font,
                 pady=15).pack()
