import tkinter
import pdf_actions as pdf


def update_listbox(listbox: tkinter.Listbox, moveup: bool, label: tkinter.Label):
    if len(listbox.curselection()) == 0:
        label.config(text="Please select a File first!")
        return
    label.config(text="")
    value = listbox.selection_get()
    total = len(listbox.get(0, tkinter.END))
    index = listbox.curselection()[0]
    listbox.delete(first=index)
    if moveup:
        index = index - 1 if index > 0 else index
    else:
        index = index + 1 if index < total - 1 else index
    listbox.insert(index, value)
    listbox.selection_set(index)


def remove_from_listbox(listbox: tkinter.Listbox):
    for index in listbox.curselection():
        listbox.delete(index)


def main_window(Operation_name: str):
    root = tkinter.Tk()
    root.geometry("500x300")

    # Side buttons
    up_button = tkinter.Button(
        root, text="MOVE UP", width=20, command=lambda: update_listbox(flist, True, err_label)
    )
    up_button.grid(row=0, column=0, padx=10)

    down_button = tkinter.Button(
        root, text="MOVE DOWN", width=20, command=lambda: update_listbox(flist, False, err_label)
    )
    down_button.grid(row=1, column=0, padx=10)

    remove_button = tkinter.Button(
        root, text="REMOVE", width=20, command=lambda: remove_from_listbox(flist)
    )
    remove_button.grid(row=2, column=0, padx=10)

    # listbox
    flist = tkinter.Listbox(root, bg="grey", width=50)
    flist.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

    err_label = tkinter.Label(root, text="", fg='red')
    err_label.grid(row=3, column=1, columnspan=2)

    # main buttons
    if Operation_name.lower() == "merge":
        submit_button = tkinter.Button(
            root,
            text="MERGE",
            width=20,
            command=lambda: pdf.merge_pdf(flist.get(0, tkinter.END)),
        )
    elif Operation_name.lower() == "decrypt":
        label = tkinter.Label(root, text="Enter Password")
        label.grid(row=4, column=0)
        passwd_entry = tkinter.Entry(root, width=50)
        passwd_entry.grid(row=4, column=1, pady=10, padx=10)
        submit_button = tkinter.Button(
            root,
            text="UNLOCK",
            width=20,
            command=lambda: pdf.decryptpdf(
                flist.selection_get(), passwd=passwd_entry.get()
            ),
        )
    submit_button.grid(row=5, column=1, columnspan=2, pady=10)

    file_dict = pdf.scan_folder()
    for item in file_dict.items():
        flist.insert(item[0], item[1])

    root.mainloop()


def Home_Window():
    Win = tkinter.Tk()
    Win.geometry("500x300")
    pdf_operation = tkinter.IntVar()
    r1 = tkinter.Radiobutton(Win, text="Merge PDFs",
                             variable=pdf_operation, value=1)
    r1.pack(pady=10)
    r2 = tkinter.Radiobutton(Win, text="Unlock PDF",
                             variable=pdf_operation, value=2)
    r2.pack(pady=10)
    submit_button = tkinter.Button(
        Win, text="Submit", width="20", command=Win.destroy)
    submit_button.pack(pady=10)
    Win.mainloop()
    return pdf_operation.get()


if __name__ == "__main__":
    operation = Home_Window()
    if operation == 1:
        main_window("merge")
    if operation == 2:
        main_window("decrypt")
