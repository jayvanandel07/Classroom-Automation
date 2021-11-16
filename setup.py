import tkinter as tk
from tkinter import ttk


LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for Page in (HomePage, ClassTimesPage, ClassesPage):

            frame = Page(container, self)
            self.frames[Page] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="HomePage", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(ClassTimesPage))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(ClassesPage))
        button2.grid(row=2, column=1, padx=10, pady=10)


# second window frame page1
class ClassTimesPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(HomePage))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(ClassesPage))
        button2.grid(row=2, column=1, padx=10, pady=10)


class ClassesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(ClassTimesPage))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(HomePage))
        button2.grid(row=2, column=1, padx=10, pady=10)


print("Push")

app = tkinterApp()
app.mainloop()
