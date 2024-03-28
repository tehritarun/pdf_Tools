import tkinter as tk
import pdf_actions as pdf


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Tools")
        self.iconbitmap("assets\\icon_pdf_tool.ico")
        self.geometry("500x300")

        self.operation = tk.StringVar()
        self.operation.set(-1)
        self.show_frame(HomePage)

    def show_frame(self, cont):
        if (self.operation.get() == "-1") and (cont == ActionPage):
            print("select radio first")
            return
        frame = cont(self)
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        r1 = tk.Radiobutton(
            self, text="Merge PDFs", variable=parent.operation, value="merge"
        )
        r2 = tk.Radiobutton(
            self, text="Unlock PDF", variable=parent.operation, value="unlock"
        )

        r1.pack(pady=10)
        r2.pack(pady=10)

        TButton(self, "SUBMIT", lambda: parent.show_frame(ActionPage))
        self.place(x=0, y=0, relwidth=1, relheight=1)


class ActionPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.fileframe = FilesFrame(self)
        self.actionframe = ActionFrame(self, parent.operation.get())
        self.place(x=0, y=0, relwidth=1, relheight=1)

    def call_pdf_action(self, action):
        if action.lower() == "merge":
            pdf.merge_pdf(self.fileframe.list.get(0, tk.END))
        elif action.lower() == "unlock":
            pdf.decryptpdf(
                self.fileframe.list.selection_get(), passwd=self.actionframe.entry.get()
            )


class FilesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # frame for files list
        frame_1 = tk.Frame(self)

        # define and place Widgets
        self.list = tk.Listbox(frame_1, bg="gray")
        self.list.pack(expand=True, fill="both", padx=10, pady=10)

        # populate listbox
        self.populate_listbox()

        frame_1.place(x=0, y=0, relwidth=0.67, relheight=0.6)

        # frame for action buttons
        frame_2 = tk.Frame(self)

        # define and place label for error
        self.label = tk.Label(frame_2, text="", fg="red")
        self.label.pack(expand=True)

        # place buttons
        TButton(frame_2, "UP", lambda: self.update_listbox(True))
        TButton(frame_2, "DOWN", lambda: self.update_listbox(False))
        TButton(frame_2, "REMOVE", self.remove_from_listbox)

        frame_2.place(relx=0.67, y=0, relwidth=0.33, relheight=0.6)

        self.pack(expand=True, fill="both")

    # function to move items up or down in list
    def update_listbox(self, moveup: bool):
        if len(self.list.curselection()) == 0:
            self.label.config(text="Please select a File first!")
            return
        self.label.config(text="")
        value = self.list.selection_get()
        total = len(self.list.get(0, tk.END))
        index = self.list.curselection()[0]
        self.list.delete(first=index)
        if moveup:
            index = index - 1 if index > 0 else index
        else:
            index = index + 1 if index < total - 1 else index
        self.list.insert(index, value)
        self.list.selection_set(index)

    # fuction to populate listbox
    def populate_listbox(
        self,
    ):
        files = pdf.scan_folder()
        for file in files.items():
            self.list.insert(file[0], file[1])

    # fuction to remove items from listbox
    def remove_from_listbox(self):
        for index in self.list.curselection():
            self.list.delete(index)


class ActionFrame(tk.Frame):
    def __init__(self, parent, actionName: str):
        super().__init__(parent)

        self.entry = None

        if actionName.upper() != "MERGE":
            frame_1 = tk.Frame(self)
            label = tk.Label(frame_1, text="Enter Password")
            self.entry = tk.Entry(frame_1, width=50)

            label.place(x=0, rely=0.4, relwidth=0.4)
            self.entry.place(relx=0.4, rely=0.4, relwidth=0.5)

            frame_1.pack(expand=True, fill="both")

        frame_2 = tk.Frame(self)

        TButton(frame_2, actionName.upper(), lambda: parent.call_pdf_action(actionName))

        frame_2.pack(expand=True, fill="both")

        self.place(rely=0.6, x=0, relwidth=1, relheight=0.4)


class TButton(tk.Button):
    def __init__(self, parent, text, command_function):
        super().__init__(parent, text=text, width=20, command=command_function)

        self.pack(padx=20, expand=True)
