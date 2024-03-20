from tkinter import *
import pdf_actions as pdf

root = Tk()


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


def print_listbox(listbox: Listbox):
    print(listbox.get(0, END))


def remove_from_listbox(listbox: Listbox):
    for index in listbox.curselection():
        listbox.delete(index)


up_button = Button(root, text="up", command=lambda: update_listbox(flist, True))
up_button.grid(row=0, column=1, padx=10)

down_button = Button(root, text="down", command=lambda: update_listbox(flist, False))
down_button.grid(row=1, column=1, padx=10)

remove_button = Button(root, text="Remove", command=lambda: remove_from_listbox(flist))
remove_button.grid(row=2, column=1, padx=10)
flist = Listbox(root, bg="grey", width=100)
flist.grid(row=0, column=0, rowspan=3)

submit_button = Button(
    root, text="Merge", command=lambda: pdf.merge_pdf(flist.get(0, END))
)
submit_button.grid(row=3, column=0, columnspan=2)

file_dict = pdf.scan_folder()
for item in file_dict.items():
    flist.insert(item[0], item[1])

root.mainloop()
