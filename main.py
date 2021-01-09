import tkinter
import tkinter as tk
from tkinter import *

import area
from area import ScrollableFrame

root = tk.Tk()



class main():
    maximumIterations = tk.IntVar()
    precision = tk.DoubleVar()
    numberOfEquations = tk.StringVar(root)
    method = tk.StringVar(root)
    OptionList = [
        "Guass Elimination",
        "Guass Jordan",
        "Guass Seidel",
        "LU decomposition",
        "All"
    ]
    equationsList = []
    frame = ScrollableFrame(root)

    def begin(self):


        self.takeInputs()
        self.chooseMethod()

        root.geometry("900x650")
        root.mainloop()



    def makeTable(self):
        self.frame = ScrollableFrame(root)
        n=int(self.numberOfEquations.get())

        for i in range(n):
            listBox = Listbox(self.frame.scrollable_frame, height=1,width=53)
            listBox.insert(END, "Equation %s :" % (i + 1))
            textBox = Text(self.frame.scrollable_frame, width=40, height=2)
            listBox.pack(pady=10)
            textBox.pack(pady=10)


        self.frame.pack()
        buttonCommit = Button(root, height=1, width=10, text="Solve",
                              command=lambda: retrieve_input()).pack()



        def retrieve_input():
            inputValue = textBox.get("1.0", "end-1c")

            equationsList=str(inputValue).split("\n")
            print(equationsList)

    def chooseMethod(self):
        self.makeLabelPackVertical(root, tk, "Choose method :", 20)

        self.method.set("")

        opt = tk.OptionMenu(root, self.method, *self.OptionList)
        opt.config(width=40, font=('Helvetica', 12))
        opt.pack(side="top")

        def callback(*args):
            print(self.method.get())

        self.method.trace("w", callback)

    def takeInputs(self):
        self.makeLabelPackVertical(root, tk, "Solving non linear equations", 70)
        self.makeLabelPackVertical(root, tk, "Maximum iterations :", 20)
        name_entry = tk.Entry(root, textvariable=self.maximumIterations, font=('calibre', 10, 'normal'), width=40).pack()
        self.makeLabelPackVertical(root, tk, "Precision :", 20)
        name_entry = tk.Entry(root, textvariable=self.precision, font=('calibre', 10, 'normal'), width=40).pack()
        self.makeLabelPackVertical(root, tk, "Number of equations :", 20)
        name_entry = tk.Entry(root, textvariable=self.numberOfEquations, font=('calibre', 10, 'normal'), width=40).pack()
        def call(*args):
            for l in list(root.children.values()):
                print(l,type(l))

                if type(l)==tkinter.Listbox or type(l)== tkinter.Scrollbar or type(l)==tkinter.Text or\
                        type(l)==tk.Button:
                    l.destroy()
                    self.frame.destroy()


            if self.numberOfEquations.get() != "":
                self.makeTable()

        self.numberOfEquations.trace("w", call)

    def makeLabelPackVertical(self,rootObject, tk, text, font):
        tk.Label(rootObject,
                 text=text,
                 justify=tk.CENTER,
                 padx=0,
                 font=font,
                 pady=15).pack()


m=main()
m.begin()