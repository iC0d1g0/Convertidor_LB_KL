from tkinter import *
from tkinter import messagebox



class Grafica : 
    def __init__(self):

        #Forma de la ventana
        self.ventana = Tk()
        self.ventana.configure(background="#1FA071")
        self.ventana.geometry("300x300")
        self.ventana.title("Kilo/libra |ver 0.1")
        self.ventana.resizable (False, False)
        self.ventana.protocol("WM_DELETE_WINDOW",self.on_close)

        #contenido dentro de la ventana
        self.titulo = Label(self.ventana, text= "Convertidor", font= ("Courier", 15), background="#afffbc")
        self.titulo.pack(padx=20, pady=20)
        self.titulo2 = Label(self.ventana, text= "KG/LB o LB/KG", font= ("Courier", 15), background="#A3F4EE")
        self.titulo2.pack(padx=20, pady=5)

        self.entrada = Entry(self.ventana, bd= 5)
        self.entrada.pack()
        self.salida = Label(self.ventana, bd= 5, text="0.0", font= ("Courier", 15), background="#1FA071", pady="5"  )
        
        self.salida.pack(padx=20, pady=20)
        self.caja = Frame(self.ventana)
        self.boton1 = Button(self.caja, text="KG/LB",bd=5, background="#A3F4EE", command=self.KG_LB  ).grid(column="0", row="0")
        self.boton2 = Button(self.caja, text="LB/KG",bd=5, background="#A3F4EE", command=self.LB_KG  ).grid(column="2", row="0")
        self.caja.pack()


        self.ventana.mainloop()
    def isfloat(self,num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def KG_LB(self):
        self.entra= self.entrada.get()
        if self.isfloat(self.entra):
            self.libra = 2.205
            
            self.kilo = float(self.entra)
            self.kilo = self.kilo * self.libra
            self.ejemplo = str(self.kilo)+ " LB."
                      
            self.salida.configure(text=self.ejemplo)
        else: 
                self.salida.configure(text="ERROR")
    
    def LB_KG(self):
            self.kilo = 0.453592
            self.entra= self.entrada.get()
            if self.isfloat(self.entra):
               self.libra = float(self.entra)
               self.libra = self.kilo * self.libra
               self.ejemplo = str(self.libra)+ " KG."
               self.salida.configure(text=self.ejemplo)
            else: 
                self.salida.configure(text="ERROR")
    def on_close (self):
        if messagebox.askyesno(title="Quieres salir", message="Enserio quieres cerrar?"):
            self.ventana.destroy()

        

            
           
            


Grafica()

        




