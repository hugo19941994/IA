from tkinter.filedialog import *
import tkinter.messagebox

top = tkinter.Tk()
top.geometry("250x200")
top.title("Clasificador de CV")
logo = PhotoImage(file = "logo_everis.png")

def load_file():
        fname_1 = askopenfilename(filetypes=(("PDF", "*.pdf"),
                                             ("HTML files", "*.html"),
                                             ("Text files", "*.docx;*.txt;*.odt"),
                                             ("All files", "*.*") ))
        if fname_1:
            try:
                print(fname_1)
            except:
                tkinter.showerror("Open Source File", "Failed to read file\n'%s'" % fname_1)
            return

def load_folder():
        fname_2 = askdirectory()
        if fname_2:
            try:
                print(fname_2)
            except:
                tkinter.showerror("Open Source File", "Failed to read file\n'%s'" % fname_2)
            return

label_3=Label(top, image=logo)
label_1=Label(top, text="CV especifico")
label_2=Label(top, text="Carpeta de CV")

button_1=Button(top, text="Clasificar")
button_2=Button(top, text="Ir a la carpeta")
button_3=Button(top, text="Buscar", command=load_file)
button_4=Button(top, text="Buscar", command=load_folder)

label_3.grid(columnspan=3)
label_1.grid(row=1, column=0)
label_2.grid(row=2, column=0)
button_3.grid(row=1, column=1)
button_4.grid(row=2, column=1)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)


top.mainloop()
