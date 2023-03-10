from tkinter import*
import random

root=Tk()
root.title("Contraseña segura")
root.geometry("400x400")

label1=Label(text="")
label1.place(relx=0.5,rely=0.6, anchor=CENTER)

array_1=[[[1,2,3,4,5,6,7],["Calabaza","Col","Color"],["A","b","C","d","e","F"]]]
print(array_1)
def contraseña_nueva():
   
    
    
     random_1 = random.randint(0, 6)
     random_2 = random.randint(0, 2)
     random_3 = random.randint(0, 5)
     
     resultado_1=str(array_1[0][0][random_1])
     resultado_2=str(array_1[0][1][random_2])
     resultado_3=str(array_1[0][2][random_3])
     
     label1["text"]=resultado_1 + resultado_2 + resultado_3
     


button1=Button(text="Dame click para generar la contraseña", bg="red", command=contraseña_nueva)
button1.place(relx=0.5 , rely=0.5 , anchor=CENTER)
root.mainloop()