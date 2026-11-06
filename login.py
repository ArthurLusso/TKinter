import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("1280x720")
root.configure(bg="#f4f4f4") 

main_frame = tk.Frame(root, bg="white")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=800, height=450)

try:
    caminho_imagem = "/Users/26210899/Documents/LOPAL/Aula 11/IMG/c9dcf243d852f0bbb41b17b3f4386ea06fea692a.png"
    logo_img = tk.PhotoImage(file=caminho_imagem)
    logo_label = tk.Label(main_frame, image=logo_img, bg="white")
    logo_label.image = logo_img 
except tk.TclError:
    logo_label = tk.Label(main_frame, text="[ LOGO AQUI ]", font=("Arial", 24, "bold"), bg="white", fg="#5b9bd5")
logo_label.pack(pady=(40, 40))



root.mainloop()