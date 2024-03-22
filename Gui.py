from tkinter import *
import pdf_actions as pdf


def update_listbox(listbox: Listbox, moveup: bool):
    value = listbox.selection_get()
    total = len(listbox.get(0, END))
    index = listbox.curselection()[0]
    listbox.delete(first=index)
    if moveup:
        index = index - 1 if index > 0 else index
    else:
        index = index + 1 if index < total - 1 else index
    listbox.insert(index, value)
    listbox.selection_set(index)


def remove_from_listbox(listbox: Listbox):
    for index in listbox.curselection():
        listbox.delete(index)


def main_window(Operation_name: str):
    root = Tk()
    root.geometry("500x300")

    # Side buttons
    up_button = Button(
        root, text="up", width=20, command=lambda: update_listbox(flist, True)
    )
    up_button.grid(row=0, column=1, padx=10)

    down_button = Button(
        root, text="down", width=20, command=lambda: update_listbox(flist, False)
    )
    down_button.grid(row=1, column=1, padx=10)

    remove_button = Button(
        root, text="Remove", width=20, command=lambda: remove_from_listbox(flist)
    )
    remove_button.grid(row=2, column=1, padx=10)

    # listbox
    flist = Listbox(root, bg="grey", width=50)
    flist.grid(row=0, column=0, rowspan=3, padx=10)

    # main buttons
    if Operation_name.lower() == "merge":
        submit_button = Button(
            root,
            text="Merge",
            width=20,
            pady=20,
            command=lambda: pdf.merge_pdf(flist.get(0, END)),
        )
    elif Operation_name.lower() == "decrypt":
        label = Label(root, text="Enter Password")
        label.grid(row=3, column=0)
        passwd_entry = Entry(root)
        passwd_entry.grid(row=3, column=1)
        submit_button = Button(
            root,
            text="Unlock",
            width=20,
            pady=20,
            command=lambda: pdf.decryptpdf(
                flist.selection_get(), passwd=passwd_entry.get()
            ),
        )
    submit_button.grid(row=4, column=0, columnspan=2)

    file_dict = pdf.scan_folder()
    for item in file_dict.items():
        flist.insert(item[0], item[1])

    root.mainloop()


def Home_Window():
    Win = Tk()
    pdf_operation = IntVar()
    r1 = Radiobutton(Win, text="Merge PDFs", variable=pdf_operation, value=1)
    r1.pack()
    r2 = Radiobutton(Win, text="Unlock PDF", variable=pdf_operation, value=2)
    r2.pack()
    submit_button = Button(Win, text="Submit", width="20", command=Win.destroy)
    submit_button.pack()
    Win.mainloop()
    return pdf_operation.get()


if __name__ == "__main__":
    operation = Home_Window()
    if operation == 1:
        main_window("merge")
    if operation == 2:
        main_window("decrypt")
