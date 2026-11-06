import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("1280x720")
root.configure(bg="#f4f4f4") 

main_frame = tk.Frame(root, bg="white")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=450)



root.mainloop()