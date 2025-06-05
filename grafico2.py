import tkinter as Tk
def suma():
    num1= int(entry_num1.get())
    num2= int(entry_num2.get())
    resultado=num1+num2
    label_resultado.config(text="resultado:"+str(resultado))
    
app =Tk.Tk()
app.title("tecnologico de estudios sumperiores de jiloyork")
label_num1=Tk.Label(text="primer numero")
entry_num1=Tk.Entry()

label_num2=Tk.Label(text="segundo numero")
entry_num2=Tk.Entry()

label_resultado = Tk.Label(text="*****")
button_suma=Tk.Button(text="sumar",command=suma)

label_num1.pack()
entry_num1.pack()

label_num2.pack()
entry_num2.pack()

label_resultado.pack()
button_suma.pack()

app.geometry("500x500")
app.mainloop()
