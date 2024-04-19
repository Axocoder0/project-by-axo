import tkinter as tk
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        pass
root=tk.Tk()
frame = tk.Frame(root)
frame.pack(pady=10)
listbox =tk.Listbox(frame,width=50,height=10,font=("Arial",12))
listbox.pack(side=tk.LEFT,fill=tk.BOTH)
scrollbar =tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
entry=tk.Entry(root,width=50, font =("Arial",12))
entry.pack()
add_button = tk.Button(root,text="ADD TASK",width=48,command=add_task)
add_button.pack()
delete_button=tk.Button(root,text="DELETE TASK",width=48,command= delete_task)
delete_button.pack()
root.mainloop()