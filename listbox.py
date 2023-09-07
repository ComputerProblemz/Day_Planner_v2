from tkinter import*

def submit():
    select=[]
    for index in listbox.curselection():
        select.insert(index,listbox.get(index))

    print("Item added!")
    for index in select:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)   
    listbox.config(height=listbox.size())

window = Tk()
window.title("Day Planner")
icon=PhotoImage(file='gui.png')
window.iconphoto(True,icon)

listbox= Listbox(window,
                bg="#E6F7FF",
                font=("Constantia",40),
                width=15,
                selectmode=MULTIPLE)
listbox.pack()

listbox.config(height=listbox.size())

#------------------------------------------
entryBox = Entry(window)
entryBox.pack()

#---------------------------------
addButton= Button(window,text="Add",command=add,font=("Arial",18,"bold"))
addButton.pack()

deleteButton= Button(window,text="Delete",command=delete,font=("Arial",11,"bold"))
deleteButton.pack()

submitButton= Button(window,text="Submit",command=submit,font=("Arial",18,"bold"))
submitButton.pack()


window.mainloop()
