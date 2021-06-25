from tkinter import *           # importa todas las librerias de tkinter
from tkinter import messagebox  # importa messagebox de tkinter
from tkinter import filedialog  # importa filedialog de tkinter
import os                       # importa os
import pygame                   # importa pygame
from math import tan, radians, degrees, copysign #importa tan, radians, degrees, copysign dela libreria de math
from pygame.math import Vector2 # importa Vector2 pygame.math
import json                     # importa la librerias json
import random                   # importa la libreria random

#Declaracion de variables globales
jugador1Global=""
jugador2Global=""

#Creacion de la clase Menu
class Menu:
    #Constructor que recibr como parametro a la raiz para trabajar sobre ella
    def __init__(self, master):
        #Se llama la funcion crearraiz() para agregarle formato a la raiz
        self.crearraiz(master)
        #Asignar master como un valor del objego self
        self.raiz=master 
        #Funcion que llama crearinicio() la cual crea la ventana de inicio
        self.crearinicio()
        #Se definen las variables de texto que se usaran mas adelante para almacenar los nombres
        #------------------------------------------------------------------------------------|
        self.nombrejugador1=StringVar()                                                     #|
        self.nombrejugador2=StringVar()                                                     #|
        #------------------------------------------------------------------------------------|
        #Se almacena el nombre del archivo json de los puntajes en la variable jsonpuntaje
        #Sera usada por obtenerpuntaje para pasarselo como parametro a getlistapuntajes()
        self.jsonpuntaje="clasificaciones.json"
        #Almacena la listapuntuaciones devuelta por obtenerpuntajes()
        #Es llamada por mostrarpuntaje() para mostrar los puntajes en la ventana clasificaciones
        self.listaPuntuacion=self.obtenerpuntajes()
        #Se almacena el nombre del archivo json de la partida desde cero en la variable partidainical
        #Sera usada por Leer Partida para pasarselo como parametro a correr()
        self.partidainicial="partidainicial.json"

    #-----------------------------raiz-------------------------------
    #Funcion llamada en el constructor para aplicarle formato a la raiz
    def crearraiz(self, root):
        #Asigna "Apeed Racer" como titulo de la ventana
        root.title("pyDakarDeath")
        #Crea un icono en la ventana
        #root.iconbitmap("imagenes/iconoauto.ico")
        #Bloquea la expansion de la raiz de forma horizontal
        root.rowconfigure(False, weight=1)
        #Bloquea la expansion de la raiz de forma vertical
        root.columnconfigure(False, weight=1)
        #Bloquea la expansion de la raiz de forma vertical y horizontal
        root.resizable(0,0)
        #Define el color negro como fondo de la raiz
        root.config(bg="Black")

    #----------------------------Inicio-------------------------------
    #Funcion llamada por el constructor para crear el inicio
    def crearinicio(self):  
        #Crea un frame en la raiz
        self.frame=Frame(self.raiz)
        #Empaqueta el frame en la raiz
        self.frame.pack()
        #Importa la imagen autoinicio.png
        self.bg = PhotoImage(file="imagenes/autodesiertoinicio.png")
        #Se crea un lienzo Canvas en el Frame de inicio con 500 de altura y 800 de ancho
        #Se le llama self.inicio a dicho Canvas
        self.inicio =Canvas(self.frame, width=800, height=500)
        #Se empaqueta self.inicio
        self.inicio.pack(fill="both", expand=False)
        #Agrega la imagen de inicio
        self.inicio.create_image(0,1, image=self.bg, anchor="nw")
        #Agrega el texto del inicio
        self.inicio.create_text(400,100, text="DAKAR DEATH", font=("Constantia", 35),fill="Black")
        #Crea el boton iniciar que llama la funcion crearFrameMenu que crea el menu
        botonabrir = Button(self.frame, text="Iniciar", bg="burlywood4", fg="gray99",activeforeground="burlywood4", activebackground="gray99",relief= "raised",font=("Constantia",16, "bold"), command=self.crearFrameMenu)
        #Empaqueta el boton Iniciar
        self.inicio.create_window(310, 450, anchor="nw", window=botonabrir)
        #Crea el boton salir que cierra el juego
        botoncerrar = Button(self.frame, text="Cerrar", bg="burlywood4", fg="gray99",relief= "raised",font=("Constantia",16, "bold"), command=self.cerrar, activebackground="gray99", activeforeground="burlywood4")
        #Empaqueta el boton cerrar
        self.inicio.create_window(410, 450, anchor="nw", window=botoncerrar)

    #Funcion llamada por el boton cerrar que cierra el programa
    def cerrar(self):
        #Comando que destruye la raiz
        self.raiz.destroy()

#-------------------------Funciones abrir menu--------------------------
    #Funcion llamada por por el boton Iniciar en el inicio
    #Se encarga de construir el frame del menu, los botones de este y el frame contuniv (contenedor universal)
    def crearFrameMenu(self):
        #Cierra el canvas de inicio
        self.inicio.destroy()       
        #Crea un frame llamado contuniv en el cual se empaquetaran los elementos del menu
        self.contuniv=Frame(self.frame, width=200, height=500, bg="Khaki")
        #Crea el titulo del juego, con color de letra tan4, fondo negro Khaki y fuente Constantia, tamaño 35 y negrita
        self.titulo = Label(self.contuniv, text="   🏎️Dakar Death🏎️", fg="tan4", bg="Khaki", font=("Constantia", 35, "bold"))
        #Empaqueta el titulo con la funcion .grid(row,column) que maneja el frame como una tabla con cuadriculas
        self.titulo.grid(row=0, column=0, columnspan=10)
        #Crea el frame menu el cual esta ubicado en el frame padre contuniv
        self.menu = Frame(self.contuniv, bg="Khaki")
        #Le aplica color de fondo Khaki y altura de 100 al frame menu
        self.menu.config(bg="Khaki", height=100)
        #Empaqueta el frame menu con la funcion .grid(row,column) que maneja el frame como una tabla con cuadriculas
        self.menu.grid(row=2, column=0)
        #Empaqueta el frame padre contuniv en la raiz
        self.contuniv.pack()
        #Crea un frame vacio en el frame padre, con color de fondo negro, ancho y altura de 300
        self.ventanadinamica=Frame(self.contuniv, bg="Black", width=300, height=300)
        #Llama la funcion crearbotonesmenu que crea y empqueta los botones del menu en el frame menu
        self.crearbotonesmenu()
        #Crea una ventana temporal en el frame ventanadinamica
        self.crearventanatemporal()
    
    #Funcion que crea los botones del menu
    def crearbotonesmenu(self):  
        #Llama la funcion craerframejugar que crea los elementos de la ventana de dos jugadores
        self.craerframejugar()
        #Crea un boton llamado Jugar en el menu, le aplica formato y al pulsarlo
        #ejecuta la funcion verventana() y le pasa por parametro framejugar que es la ventana de 
        #inicio de partida
        botonjugar = Button(self.menu, text="Jugar", width=20, bg="Khaki3",activeforeground="Khaki3",activebackground="NavajoWhite4", bd=5, relief= "raised", font=("Constantia",16, "bold"), command=lambda:self.verventana(self.framejugar))
        #Empaqueta el botonjugar en la fila 1 y la columna 0 con el metodo .grid(row, column)       
        botonjugar.grid(row=1, column=0, columnspan=2)
        #Llama la funcion crearframecargar que crea los elementos de la ventana cargar
        self.crearframecargar()
        #Crea un boton llamado botoncargar en el menu, le aplica formato y al pulsarlo
        #ejecuta la funcion verventana() y le pasa por parametro elframecargar que crea
        #el frame cargar con los datos actualizados de las partidas guardadas que abre las partidas guardadas
        botoncargar = Button(self.menu, text="Cargar Partida", width=20, bg="Khaki3",activeforeground="Khaki3",activebackground="NavajoWhite4", bd=5,relief= "raised", font=("Constantia",16, "bold"), command=lambda:self.elframecargar())
        #Empaqueta el botoncargar en la fila 1 y la columna 3 con el metodo .grid(row, column)        
        botoncargar.grid(row=1, column=3, columnspan=2)
        #Llama la funcion crearFrameClasificaciones que crea un frame con los datos de las mejores puntuaciones
        self.crearFrameClasificaciones()
        #Crea un boton llamado botonclasificaciones en el menu, le aplica formato y al pulsarlo
        #ejecuta la funcion laframeclasificaciones que actualiza y lee los datos del json clasificaciones
        #y luego ejecuta la funcion verventana() y le pasa verframeclasificaciones() como parametro
        botonclasificaciones = Button(self.menu, text="Mejores Puntajes", width=20, bg="Khaki3",activeforeground="Khaki3",activebackground="NavajoWhite4", bd=5, relief= "raised",font=("Constantia",16, "bold"), command=lambda:self.laframeclasificaciones())
        #Empaqueta el botoncargar en la fila 1 y la columna 5 con el metodo .grid(row, column)
        botonclasificaciones.grid(row=1, column=5, columnspan=2)
        #Llama la funcion frameinstrucciones que crea los elementos de la ventana instrucciones
        self.frameinstrucciones()
        #Crea un boton llamado botoninstrucciones en el menu, le aplica formato y al pulsarlo
        #ejecuta la funcion verventana() y le pasa por parametro frameinstrucciones que es la ventana que
        #muestra las instrucciones del juego
        botoninstrucciones = Button(self.menu, text="Como Jugar?", width=20, bg="Khaki3",activeforeground="Khaki3",activebackground="NavajoWhite4", bd=5, relief= "raised",font=("Constantia",16, "bold"), command=lambda:self.verventana(self.frameinstrucciones))
        #Empaqueta el botoninstrucciones en la fila 3 y la columna 1 con el metodo .grid(row, column)
        botoninstrucciones.grid(row=3, column=1, columnspan=3)
        #Etiqueta vacia creada para funcionar como espacio y darle estetica a la interfaz
        espacioinstrucciones=Label(self.menu, text="", bg="Khaki", width=1)
        #Empaqueta la etiqueta en la fila 2 y la columna 0 con el metodo .grid(row, column)
        espacioinstrucciones.grid(row=2, column=0)
        #Llama la funcion framecreditos() que crea los elementos de la ventana creditos
        self.framecreditos()
        #Crea un boton llamado botoncreditos en el menu, le aplica formato y al pulsarlo
        #ejecuta la funcion verventana() y le pasa por parametro framecreditos que es la
        #ventana que muestra los creditos
        botoncreditos = Button(self.menu, text="Creditos", width=20, bg="Khaki3",activeforeground="Khaki3",activebackground="NavajoWhite4", bd=5, relief= "raised",font=("Constantia",16, "bold"), command=lambda:self.verventana(self.framecreditos))
        #Empaqueta el botoncreditos en la fila 3 y la columna 4 con el metodo .grid(row, column)
        botoncreditos.grid(row=3, column= 4, columnspan=2)
        #Crea un boton llamado salir, le aplica formato y al pulsarlo llama la funcion comfirmarsalir()
        botonsalir = Button(self.menu, text="Salir", fg="Red", activeforeground="White",activebackground="Red",bd=5, relief= "raised", height=1, font=("Constantia", 16, "bold"), command=self.confirmarsalir)
        #Empaqueta el botonsalir en la fila 3 y la columna 6 con el metodo .grid(row, column)
        botonsalir.grid(row=3, column= 6)
        #Etiqueta vacia creada para funcionar como espacio y darle estetica a la interfaz
        espacioinstrucciones2=Label(self.menu, text="", bg="Khaki")
        #Empaqueta la  espacio6 en la fila 4 y la columna 0 con el metodo .grid(row, column)
        espacioinstrucciones2.grid(row=4, column=0)

        
    #Funcion que crea una ventana temporal al crear el menu
    #Esta se sustituira si se presiona un boton del menu
    def crearventanatemporal(self):
        #Crea un frame llamado ventanadinamica en el frame contuniv
        #Sobre esta se estaran mostrando las ventanas de las opciones del menu
        self.ventanadinamica = Frame(self.contuniv, bg="Khaki" )
        #Crea una etiqueta vacia para crear un espacio y darle estetica a la interfaz
        ventanavaciaespacio1=Label(self.ventanadinamica, text="                              ", bg="Khaki")
        #Empaqueta la etiqueta con el metodo .grid(row, column) en la fila 0 y la columna 2
        ventanavaciaespacio1.grid(row=0, column=0)
        #Crea una etiqueta vacia para crear un espacio y darle estetica a la interfaz
        ventanavaciaespacio2=Label(self.ventanadinamica, text="                                       ", bg="Khaki")
        #Empaqueta la etiqueta con el metodo .grid(row, column) en la fila 1 y la columna 2
        ventanavaciaespacio2.grid(row=1, column=1,)
        #Crea una etiqueta llamada titulovacio en el cual muestra ls indtruccion "Presione un boton"
        titulovacio = Label(self.ventanadinamica, text="     Presione un boton  ", fg="LightSalmon4",bg="Khaki",  font=("Constantia",28, "bold") )
        #Empaqueta titulovacio con el metodo .grid(row, column) en la fila 2 y columna 2
        titulovacio.grid(row=2, column=2, columnspan=10)
        #llama el metodo verventana() y le pasa como parametro la ventanadinamica
        #Este metodo mostrara la ventana en la interfaz del menu
        self.verventana(self.ventanadinamica)

    #Funcion que muestra en el los frames de las opciones del menu en la interfaz
    #Es llamada al pulsar uno de lo botones del menu y recibe como parametro la ventana que se quiere mostrar
    def verventana(self, contenedor):
        #Almacena la ventana que se quiere empaquetar como contenedor y le aplica el metodo .tkraise()
        #Este metodo permite alternar entre frames
        contenedor.tkraise()
        #busca el contenedor entre las ventanas
        for contenedor in (self.framejugar,self. framecargar, self.frameclasificaciones, self.frameinstrucciones, self.ventanadinamica, self.framecreditos):
            #Empaqueta la ventana usando el metodo .grid(row, column, sticky), donde se se declara la posicion 
            #de la ventana en la fila 1, columna 2 y con orientacion a nsew, la cual expande el frame a toda su casilla
            contenedor.grid(row=1, column=0, sticky="nsew")

#--------------------Funciones de iniciar el juego----------------------
    #Funcion que ejecuta el juego 
    def iniciarpartida(self):
        #Obtiene el valor almacenado en la variable de texto nombrejugador1 y lo almacena en jugador1
        jugador1=self.nombrejugador1.get()
        #Obtiene el valor almacenado en la variable de texto nombrejugador2 y lo almacena en jugador2
        jugador2=self.nombrejugador2.get()
        #Almacena los datos de la partida por default
        datospartidainicial=self.LeerPartida(self.partidainicial)
        #Verifica que el nombre de ambos jugadores no este vacio      
        if jugador1 != "" and jugador2!="":
            #Imprime en consola que si se obtuvieron los nombres d los jugadores
            print("Si obtiene el nombre del jugador 1: "+ jugador1+" y del jugador 2: "+jugador2)
            #Verifica  que el archivo se este ejecutando directamente
            if __name__ == '__main__':
                #Instancia la clase Juego() en el objeto jugo
                self.juego = Juego()
                #Crea el reloj en el objeto juego
                self.Reloj= self.juego.reloj
                #Aplica el metodo .correr de la clase juego, la cual inicialisa el juego
                self.juego.correr(datospartidainicial)
        #Si alguno de los dos nombres esta vacio entra en el else
        else:
            #Se crea un mensaje de informacion en una caja avisandole 
            #al usuario que el nombre de los jugadores no puede estar vacio
            messagebox.showinfo("Nombre", "El espacio de nombre no puede estar vacio")


#**************************Definir ventanas*****************************
    #----------------------Ventana Jugar------------------------
    #Funcion que crea los elementos del frame jugar
    def craerframejugar(self):
        global jugador1Global
        global jugador2Global
        #Crea una frame llamado framejugar en el frame contuniv
        self.framejugar = Frame(self.contuniv, bg="Khaki")
        #Crea una etiqueta llamada titulo1j en el cual muestra el texto "Introduzca el nombre del jugador" en frame1j
        titulo1j = Label(self.framejugar, text=" Introduzca el nombre del jugador 1", width=35, fg="LightSalmon4", bg="Khaki", bd=5, font=("Constantia",20, "bold"))
        #Empaqueta la etiqueta con el metodo .grid(row, column) en la fila 2 y la columna 2
        titulo1j.grid(row=2, column=2, columnspan=3)
        #Crea una etiqueta vacia para crear un espacio y darle estetica a la interfaz
        jugarespacio1=Label(self.framejugar, text="", bg="Khaki", width=15)
        #Empaqueta la etiqueta con el metodo .grid(row, column) en la fila 3 y la columna 0
        jugarespacio1.grid(row=3, column=0)
        #Crea una caja de texto en la ventanaguardar, almacena el texto en NombreNuevaPartida, le aplica formato al texto y lo empaqueta
        nombrej1 = Entry(self.framejugar, textvariable=self.nombrejugador1, fg="LightSalmon4", width=20, font=("Constantia",20, "bold"), justify="center" )
        #Empaqueta la caja de texto con el metodo .grid(row, column) en la fila 4 y la columna 2
        nombrej1.grid(row=4, column=2, columnspan=4)
        #Almacena el nombre del jugador1 en la variable jugador1Global
        jugador1Global=self.nombrejugador1
        #Crea una etiqueta vacia para crear un espacio y darle estetica a la interfaz
        jugarespacio2=Label(self.framejugar, text="", bg="Khaki")
        #Empaqueta la etiqueta con el metodo .grid(row, column) en la fila 5 y la columna 0
        jugarespacio2.grid(row=5, column=0)
        #Crea una etiqueta llamada titulo2j en el cual muestra el texto "Introduzca el nombre del jugador" en framejugar
        titulo2j = Label(self.framejugar, text="  Introduzca el nombre del jugador 2", fg="LightSalmon4", width=35, bg="Khaki", bd=5, font=("Constantia",20, "bold"))
        #Empaqueta la etiqueta con el metodo .grid(row, column) en la fila 6 y la columna 2
        titulo2j.grid(row=6, column=2, columnspan=3)
        #Crea una etiqueta vacia para crear un espacio y darle estetica a la interfaz
        jugarespacio3=Label(self.framejugar, text="", bg="Khaki")
        #Empaqueta la etiqueta con el metodo .grid(row, column) en la fila 7 y la columna 0
        jugarespacio3.grid(row=7, column=0)
        #Crea una caja de texto en la ventanaguardar, almacena el texto en NombreNuevaPartida, le aplica formato al texto y lo empaqueta
        nombrej2 = Entry(self.framejugar, textvariable=self.nombrejugador2, width=20, fg="LightSalmon4", font=("Constantia",20, "bold"), justify="center" )
        jugador2Global=self.nombrejugador2
        #Empaqueta la caja de texto con el metodo .grid(row, column) en la fila 8 y la columna 2
        nombrej2.grid(row=8, column=2, columnspan=4)
        #Crea una etiqueta vacia para crear un espacio y darle estetica a la interfaz
        jugarespacio4=Label(self.framejugar, text="", bg="Khaki")
        #Empaqueta la etiqueta con el metodo .grid(row, column) en la fila 8 y la columna 0
        jugarespacio4.grid(row=9, column=0)
        #Crea un boton llamado botoniniciar en frame3j el cual se muestra en la interfaz
        #con el nombre Jugar, llama la funcion iniciar2j() que ejecuta el juego y se empaqueta
        botoniniciar=Button(self.framejugar, text="Jugar", width=10, bg="Khaki2", bd=5, fg="LightSalmon4", relief= "raised", font=("Constantia",17, "bold"), command=self.iniciarpartida)
        #Empaqueta la etiqueta con el metodo .grid(row, column) en la fila 10 y la columna 2
        botoniniciar.grid(row=10, column=2, columnspan=4)

    #--------------------Ventana cargar partida----------------------
    #Funcion que crea los elementos de la ventana cargar
    def crearframecargar(self):
        #Crea una frame llamado framecargar en el frame contuniv
        self.framecargar = Frame(self.contuniv, bg="Khaki")
        #Crea la etiqueta vacia cargarespacio0 para crear un espacio y darle estetica a la interfaz
        cargarespacio0=Label(self.framecargar, text="", bg="Khaki", width=18)
        #Empaqueta la etiqueta cargarespacio0 en framecargarcon el metodo .grid(row, column) en la fila 0 y la columna 0
        cargarespacio0.grid(row=0, column=0)
        #Crea una etiqueta llamada titulocargar en el cual muestra el texto "Elija la partida que desea cargar" en framecargar
        titulocargar = Label(self.framecargar, text="Seleccione una partida guardada", fg="LightSalmon4", width=35, bg="Khaki", bd=5, font=("Constantia",20, "bold"))
        #Empaqueta la etiqueta con el metodo .grid(row, column) en la fila 1 y la columna 3
        titulocargar.grid(row=1, column=3)
        #Llama a la funcion craerobjetosframecargar() que crea el frame cargar en la interfaz, pasa como parametro framecargar
        self.crearobjetosdeframecargar(self.framecargar)
        #Crea la etiqueta vacia cargarespacio1 para crear un espacio y darle estetica a la interfaz
        cargarespacio1=Label(self.framecargar, text="", bg="Khaki")
        #Empaqueta la etiqueta cargarespacio1 con el metodo .grid(row, column) en la fila 2 y la columna 0
        cargarespacio1.grid(row=3, column=0)
        #Crea un boton llamado botoniniciarcargada en framecargar el cual se muestra en la interfaz
        #con el nombre Jugar, llama la funcion cargarpartida() que ejecuta el juego con los datos de una partida cargada y lo empaqueta
        botoniniciarcargada=Button(self.framecargar, text="Jugar Partida", width=16, bg="Khaki2", bd=5, relief= "raised", font=("Constantia",15, "bold"), command=self.mostrardatospartida)
        #Empaqueta el boton llamado botoniniciarpartida con el metodo .grid(row, column) en la fila 3 y la columna 3
        botoniniciarcargada.grid(row=4, column=3)

    #--------------------Ventana Clasificaciones---------------------
    #Funcion que crea los elementos de la ventana clasificaciones
    def crearframeclasificaciones(self):
        #Crea una etiqueta llamada titulocclasificaciones, la aplica formato y  muestra el texto "Mejores puntajes" en framecargar
        tituloclasificaciones = Label(self.frameclasificaciones, text="Mejores Puntajes", fg="LightSalmon4", bg="Khaki", font=("Constantia",20, "bold"))
        #Empaqueta la etiqueta con el metodo .grid(row, column, columnspan) en la fila 1, la columna 1 y columnspan 3, el cual expande el tamaño de la etiqueta
        tituloclasificaciones.grid(row=1, column=1)
        #Crea la etiqueta vacia clasifespacio1 para crear un espacio y darle estetica a la interfaz
        clasifespacio1 = Label(self.frameclasificaciones, text="", width=19, bg="Khaki")
        #Empaqueta la etiqueta clasifespacio1 con el metodo .grid(row, column) en la fila 2 y la columna 0
        clasifespacio1.grid(row=2, column=0)
        #Crea una etiqueta llamada puntaje1 en frameclasificaciones, en el cual muestra el valor obtenido 
        #del metodo mostrarpuntaje(), al cual le pasa como parametro 0 y le aplica formato
        puntaje1 = Label(self.frameclasificaciones, text=self.mostrarpuntaje(0), width=35, bg="Khaki", fg="LightSalmon4", bd=5, font=("Constantia",20, "bold"))
        #Empaqueta la etiqueta puntaje1 con el metodo .grid(row, column) en la fila 3 y la columna 0
        puntaje1.grid(row=3, column=1)
        #Crea una etiqueta llamada puntaje2 en frameclasificaciones, en el cual muestra el valor obtenido
        #del metodo mostrarpuntaje()  al cual le pasa como parametro 1 y le aplica formato
        puntaje2 = Label(self.frameclasificaciones, text=self.mostrarpuntaje(1), width=35, bg="Khaki", fg="LightSalmon4", bd=5, font=("Constantia",20, "bold"))
        #Empaqueta la etiqueta puntaje2 con el metodo .grid(row, column) en la fila 4 y la columna 1 
        puntaje2.grid(row=4, column=1)
        #Crea una etiqueta llamada puntaje3 en frameclasificaciones, en el cual muestra el valor obtenido
        #del metodo mostrarpuntaje() al cual le pasa como parametro 2 y le aplica formato
        puntaje3 = Label(self.frameclasificaciones, text=self.mostrarpuntaje(2), width=35, bg="Khaki", fg="LightSalmon4", bd=5, font=("Constantia",20, "bold"))
        #Empaqueta la etiqueta puntaje3 con el metodo .grid(row, column) en la fila 3 y la columna 1
        puntaje3.grid(row=5, column=1)
        #Crea una etiqueta llamada puntaje4 en frameclasificaciones, en el cual muestra el valor obtenido
        #del metodo mostrarpuntaje() al cual le pasa como parametro 3 y le aplica formato
        puntaje4 = Label(self.frameclasificaciones, text=self.mostrarpuntaje(3), width=35, bg="Khaki", fg="LightSalmon4", bd=5, font=("Constantia",20, "bold"))
        #Empaqueta la etiqueta puntaje4 con el metodo .grid(row, column) en la fila 6 y la columna 1
        puntaje4.grid(row=6, column=1)
        #Crea una etiqueta llamada puntaje5 en frameclasificaciones, en el cual muestra el valor obtenido
        #del metodo mostrarpuntaje() al cual le pasa como parametro 4 y le aplica formato
        puntaje5 = Label(self.frameclasificaciones, text=self.mostrarpuntaje(4), width=35, bg="Khaki", fg="LightSalmon4", bd=5, font=("Constantia",20, "bold"))
        #Empaqueta la etiqueta puntaje1 con el metodo .grid(row, column) en la fila 7 y la columna 1
        puntaje5.grid(row=7, column=1)

    #---------------------Ventana Instrucciones----------------------
    #Funcion que crea la ventana con las instrucciones
    def frameinstrucciones(self):
        #Crea una frame llamado frameinstrucciones en el frame contuniv
        self.frameinstrucciones = Frame(self.contuniv,  bg="Khaki")
        #Crea una serie de etiquetas en el frame instrucciones con los datos de como jugar la partida
        tituloinstrucciones = Label(self.frameinstrucciones, text="Instrucciones",fg="LightSalmon4", bg="Khaki", font=("Constantia",20, "bold"), justify=CENTER )
        #Empaqueta tituloinstrucciones con el metodo .grid(row, column) 3n la fils 0 y ka columna 1
        tituloinstrucciones.grid(row=0, column=1)
        #Llama a la funcion crearobjetosdeframeinstrucciones() que  crea el frame instrucciones en la interfaz, pasa como parametro frameinstrucciones
        self.crearobjetosdeframeinstrucciones(self.frameinstrucciones)
        #Crea una etiqueta en frameinstrucciones para añadir estetica a la interfaz
        espacioinstrucciones=Label(self.frameinstrucciones, text="", bg="Khaki", width=8)
        #Empaqueta la etiqueta espacioinstrucciones con el metodo .grid(row, column) en la fila 4 y la columna 0
        espacioinstrucciones.grid(row=4, column=0)

    #---------------------Ventana Creditos----------------------
    #Funcion que crea la ventana con los Creditos
    def framecreditos(self):
        #Crea framecreditos el cual es el frame en el cual se van a mostrar los creditos
        self.framecreditos=Frame(self.contuniv, bg="Khaki")
        #Crea titulocreditos en framecreditos el cual es una etiqueta que contiene los creditos
        #usa "\n" para crear saltos de linea
        titulocreditos = Label(self.framecreditos, text="  CREDITOS \n Creadores: \n Brandon Cubero \n Dylan Meza \n Eder Vega\n Profesor: \nAntonio Gonzales Torres\n Proyecto de Taller de Programacion\n I Semestre 2021\n INSTITUTO TECNOLOGICO DE COSTA RICA",fg="LightSalmon4", bg="Khaki", font=("Constantia",20, "bold"), justify=CENTER )
        #Empaqueta titulocreditos con el metodo .grid(row, column) en la fila 0 y la columna 1
        titulocreditos.grid(row=0, column=1)
        #Crea la etiqueta espaciotactico en framecreditos, la cual esta vacia y funcionara como espaciador
        espaciotactico=Label(self.framecreditos, bg="Khaki", width=21) 
        #Empaqueta espaciotactico con el metodo .grid(row, column) en la fila 0 y la columna 1
        espaciotactico.grid(row=2, column=0)
        

#---------------------Funciones Cargar Partida-------------------------
    #Funcion llamada por elframecargar(), recibe como parametro el frame de carga
    def crearobjetosdeframecargar(self, framedecarga):
        #Crea framex, el cual es un Frame en framedecarga en el cual se cargaran la caja de lista
        self.framex=Frame(framedecarga, bg="Black")
        #Almacena en json_file el nombre del archivo JSON donde se  almacenan las partidas
        self.json_file="partidas.json"
        #Llama la funcion crearlistbox(), la cual crea la caja de lista
        self.crearlistbox()

    #Crea la caja de lista
    def crearlistbox(self):
        # Crear una barra de deslizamiento con orientación vertical.
        scrollbar = Scrollbar(self.framex, orient=VERTICAL, bg="Khaki")
        # Crea una caja de lista llamada listbox y vincula la barra de deslizamiento a ella
        self.listbox = Listbox(self.framex, yscrollcommand=scrollbar.set, selectmode=BROWSE, bg="Khaki", fg="LightSalmon4", font=("Constantia",17, "bold"), width=25 )
        #En listanombres almacena los datos obtenidos de ListarNombresPartidas()
        self.listanombres=self.ListarNombresPartidas()
        #Establece un valor para contador
        contador=1
        #Recorre listanombres con un ciclo for
        for i in self.listanombres:
            #Asigna a "e" el valor del contador en forma de cadena de texto
            e=str(contador)
            #Agrega al final de la lista los valores de listanombres con un formato personalizado
            self.listbox.insert(END, e+". "+"{}".format(i))
            #Agrega 1 al contador
            contador+=1
        #Configura la orientacion de la barra de desplazamiento sobre la coordenada Y
        scrollbar.config(command=self.listbox.yview)
        # Ubicarla la barra de desplazamiento a la derecha
        scrollbar.pack(side=RIGHT, fill=Y)
        #Empaqueta listbox
        self.listbox.pack()
        #Empaqueta framex con el metodo ,grid(row, column) en la fila 3 y la columna 3
        self.framex.grid(row=2, column=3)
    
    #Muestra los datos de la partida, es llamada por el boton de jugarpartida
    def mostrardatospartida(self):
        #Obtiene la posicion del elemento seleccionado en listbox
        self.elemento=self.listbox.curselection()
        #Imprime el elemento
        print(self.elemento)
        #Imprimira los datos devueltos por ciclofor, al cual pasa como parametro la posicion seleccionada en elemento
        partidaacargar=self.ciclofor(self.elemento)
        print(partidaacargar)
        self.iniciarpartidacargada(partidaacargar)

    #Lee los datos de las partidas guardadas en el jsonpartidas.json
    def LeerPartida(self, json_file):
        #Abre json_file en modo lectura, el cual contiene el nombre del archivo json donde se han almacenado las partidas
        with open(json_file) as file:
            #Obtiene todos los datos del archivo json y los almacena en data
            self.data = json.load(file)
            #Cierra el archivo
            file.close
            #Devuelve data el cual continene los datos del archivo partidas.json
            return self.data

    def ListarNombresPartidas(self):
        #Lee el json mediante la funcion LeerPartida() y lo almacena en partidas
        partidas = self.LeerPartida(self.json_file) 
        #Crea una lista vacia llamada lista
        lista = []
        #Recorre los datos guardados en el indice 'partidas' 
        for partida in partidas['partidas']:
            #Agrega a la lista lod datos dcon el indice 'Nombre Partida' los cuales corresponden a los nombres de las partidas guardadas
            lista.append(partida['Nombre Partida'])
        #Cuando sale del ciclo for, imprime la lista
        return lista

    #Funcion llamada por mostrardatospartida(), recibe como parametro la posicion del objeto seleccionado en la lista
    def ciclofor(self, elementonuevo):
        #Almacena en listadenombres los datos obtenidos de ListarNombresPartidas
        listadenombres=self.ListarNombresPartidas()
        #Almacena en partidas la informacion de todas las partidas guardadas
        #Las obtiene al llamar la funcion LeerPartida con el nombre del archivo json que guarda las partidas
        partidas=self.LeerPartida(self.json_file)
        #Valida que el elemento nuevo no este vacio
        if len(elementonuevo)!=0:
            #Si el largo del elemento es mayor no es 0, asigna a elemento el valor de elementonuevo en la posicion 0
            elemento=int(elementonuevo[0])
        else:
            #Muestra una caja de mensaje donde se informa que se debe seleccionar una partida
            return messagebox.showinfo("Cargar Partida", "Debe seleccionar una partida")       
        #Entra al ciclo for donde se recorrera la listadenombres y se devolveran los datos de la posicion que indique el valor de bombre 
        for nombre in range(0, len(listadenombres)):
            #Verifica si el valor de nombre es igual a la de elemento
            if nombre==elemento:
                #Si es asi devuelve el diccionario almacenado en el archivo json en esa posicion
                return partidas["partidas"][nombre]
            #Si no son iguales, se aumenta en 1 el valor de nombre
            nombre+=1        
    
        #Funcion que ejecuta el juego 
    
    #Inicia la partida seleccionada en listbox
    def iniciarpartidacargada(self, partidaacargar):
            if __name__ == '__main__':
                #Instancia la clase Juego() en el objeto jugo
                self.juego = Juego()
                #Crea el reloj en el objeto juego
                self.Reloj= self.juego.reloj
                #Aplica el metodo .correr de la clase juego, la cual inicialisa el juego
                self.juego.correr(partidaacargar)
       

    #Funcion llamada por el botoncargar partida
    def elframecargar(self):
        #Llama a la funcion crearobjetosdeframecargar()  y pasa como parmaetro a framecargar
        self.crearobjetosdeframecargar(self.framecargar) 
        #Llama al metodo verventana() y pasa como parametro framecargar para mostrarlo en la interfaz
        self.verventana(self.framecargar) 
#---------------------Funciones de clasificaciones----------------------
    #Funcion llamada por laframeclasificaciones()
    #Obtiene los datos de las clasificaciones y devuelve una lista con el formato deseado
    def obtenerpuntajes(self):
        #Define una lista llamada listaPunduaciones
        self.listaPuntuaciones=[]
        #Almacena los datos del archivo json clasificaciones.json en la variable data
        data=self.getlistapuntajes(self.jsonpuntaje)
        #Define el valor de i, sera la variable que funcionara como indice en la lista de mejores partidas
        i=1
        #Caracteres que se desean extraer de la cadena de texto
        caracteres=("',")
        #Entra a un ciclo for en los datos sobre la llave 'Puntajes'
        for partida in data['Puntajes']:
            #Almacena el nombre de la partida de la posicion actual en la variable temporal tempoNombre
            tempoNombre= partida['Nombre']
            #Almacena el nombre de la partida de la posicion actual en la variable temporal tempoNombre
            tempoPuntuacion=partida['Puntuacion']
            #Entra a un ciclo For que recorre la cadena almacenada en caracteres
            for x in range(len(caracteres)):
                #Remmplaza los caracteres de la cadena caracteres presentes en el nombre por un espacio
                tempNombre=tempoNombre.replace(caracteres[x], "   ")
                #convierte los datos almacenados en tempoPuntuacion a una cadena de texto
                tempPuntuacion=str(tempoPuntuacion)
                #Define a "e" como una variable que almacena en formato de cadena de texto el valor de "i"
                e=str(i)
            #Cuando termina de quitar los caracteres y darle formato a las cadenas numericas, concatena los datos
            #en la Lista Puntuaciones con el formato deseado
            self.listaPuntuaciones.append(e+". "+tempNombre+"  "+tempPuntuacion)
            #Aumenta el valor de "i"
            i+=1
        #Cuando termina de recorrer los datos almacenados en data devuelve la lista de puntuaciones
        return self.listaPuntuaciones

    #Funcion llamada por obtenerpuntajes(), abre el archivo clasificaciones.json y obtiene sus datos
    #Recibe como parametro el nombre del archivo json que se desea abrir
    def getlistapuntajes(self, json_file):
        #Con la funcion with, abre clasificaciones.json en forma de lectura
        with open(json_file) as file:
            #Descarga los datos del archivo json en e la variable data
            data = json.load(file)
            #Cierra el archivo json ya que no se va a estar utilizando
            file.close()
            #Devuelve data que almacena los datos descargados
            return data

    #Funcion llamada por las etiquetas de la ventana clasificaciones
    #recibe como parametro un numero y devuelve e dato que este en esa posicion
    def mostrarpuntaje(self, posicion):
        #Pregunta si el valor en la posicion es mayor que la cantidad de elemntos en listaPuntuaciones
        #Esto se hace por si la lista contiene menos de 5 elementos, al lamar la funcion no de Error
        if posicion>=len(self.listaPuntuaciones):
            #Si la posicion es mayor o igual al largo de la lista devuelve una cadena de texto vacia 
            return ""
        else: 
            #Si si esta en el rango del largo de lista puntuaciones, devuelve el dato de listaPuntuacion en esa posicion
            return self.listaPuntuacion[posicion]

    #Funcion llamada al declarar los valores del menu, crea el frame clasificaciones
    def crearFrameClasificaciones(self):
        #Crea un Frame llamado frameclasificaciones en el frame padre contuniv
        self.frameclasificaciones = Frame(self.contuniv, bg="Khaki")    
        
    #Funcion que imprime los 5 mejores puntajes en consola, recibe como parametro la lista
    def imprimirpuntajesconsola(self, lista):
        #Imprime un encabezado
        print("Los mejores puntajes son:")
        #Define la variable tamañolistapuntuaciones que almacena el tamaño de la lista
        tamañolistapuntuaciones=len(lista)
        #Toma la decision si el tamaño de la lista es igual o mayor que 5
        if tamañolistapuntuaciones>=5:
            #Si es asi, recorre la lista en las posiciones desde de la posicion 0 a la 4
            for posicion in range(5):
                #Imprime el valor de la lista en el indice posicion
                print(lista[posicion])
        #Si el tamño de la lista no es mayor o igual a 5 entra en el else
        else:
            #En el ciclo for se recorre la lista en el rango del largo de la lista
            for posicion in range(tamañolistapuntuaciones):
                #Imprime el valor de la lista en el indice posiciones
                print(lista[posicion])

    #Funcion llamada por el boton clasificaciones del menu
    #Llama diversos metodos para obtener los datos de las clasificaciones y construir la ventana
    def laframeclasificaciones(self):
        #Almacena en listaPuntuacion la lista de las puntuaciones con el formato deseado
        #obtenida del metodo obtenerpuntajes()
        self.listaPuntuacion= self.obtenerpuntajes()
        #LLama a imprimirpuntajeconsola() y pasa comp parametro la lista almacenada en listapuntuacion
        self.imprimirpuntajesconsola(self.listaPuntuacion)
        #Crea la ventana clasificaciones, se crea hasta este momento porque se nesesitan los datos de los
        #puntajes actualizados para funcionar de manera optima
        self.crearframeclasificaciones()
        #Llama el metodo verventana() y le pasa como parametro la ventanaclasificaiones
        #Esto mostrara la frameclasificaciones en la interfaz
        self.verventana(self.frameclasificaciones)
#---------------------Funciones Instrucciones---------------------------
    #Llamada al ejecutar frameinstrucciones(), recibe como parametro el frame instrucciones
    def crearobjetosdeframeinstrucciones(self, framedeinstrucciones):
        #Crea el framey en framedeinstrucciones
        self.framey=Frame(framedeinstrucciones,  bg="Khaki")
        #Abre el archico txt de instrucciones y lo almacena en datos
        datos=open("Instrucciones.txt", 'r')
        #Lee las lineas del txt y las acuula
        self.texto=datos.readlines()
        #llamada por:rearlistboxinstrucciones()
        self.crearlistboxinstrucciones()
        

    def crearlistboxinstrucciones(self):
        #Crear una barra de deslizamiento con orientación vertical llamada scrollbar
        scrollbar = Scrollbar(self.framey, orient=VERTICAL,  bg="LightSalmon4"  )
        #Se crea una caja de lista en el framey llamada listbox, y le anexa la barra de desplazamiento scrollbar
        listbox = Listbox(self.framey, yscrollcommand=scrollbar.set, selectmode=False,fg="LightSalmon4", bg="Khaki", font=("Constantia",17, "bold"), width=55, height=14 )
        #Entra a un ciclo for donde recorre los datos de textolista
        for i in self.texto:
            #Inserta las lineas de texto al final de la lista
            listbox.insert(END, i)
        #Se configura scroolbar
        scrollbar.config(command=listbox.yview)
        #Ubicarla a la derecha.
        scrollbar.pack(side=RIGHT, fill=Y)
        #Almacena los valores de listbox  en cajalista
        self.cajalista=listbox
        #Empaqueta listbox
        listbox.pack()
        #Empaqueta el frame y con el metodo .grid(row, column) con fila 1 y columna 1
        self.framey.grid(row=1, column=1)
#------------------------Confirmacion de Salida-------------------------
    #Funcion llamada por el boton salir
    def confirmarsalir(self):
        #Se muestra un cuadro de mensaje y se obtiene el valor de la respuesta
        valor = messagebox.askquestion("Salir", "¿Esta seguro?")
        #Comprueva si la decision es si (yes)
        if valor == "yes":
            #Si el valor obtenido es si cierra la raiz
            self.raiz.destroy()

#----------------------Funciones de JSON------------------------
#Clase encargada de administrar los datos de las partidas en los json
class adminjson:
    #Es el constructor de la clase, recibe como parametro el punteje del jugador
    def __init__(self, jugador1, jugador2):
        #Llama la varaible global jugador1Global
        global jugador1Global
        #Llama la varaible global jugador2Global
        global jugador2Global
        #Almacena en nombre del archico que almacena los datos de las partidas en json_file
        self.json_file= "partidas.json"
        #Almacena en nombre del archico que almacena los datos de las partidas en json_file
        self.json_puntaje = "clasificaciones.json"
        #Almacena el valor de la variable jugador1Global en nombrejugador1
        self.nombrejugador1=jugador1Global
        #Almacena el valor de la variable jugador2Global en nombrejugador2
        self.nombrejugador2=jugador2Global
        #Crea una variable de texto llamada NombreNuevaPartida
        self.NombreNuevaPartida=StringVar()
        #Asigna el valor del puntaje1 a puntajejugador1
        self.jugador1=jugador1
        #Asigna el valor del puntaje2 a puntajejugador2
        self.jugador2=jugador2
        #imprime el puntaje del jugador1
        print("el puntaje del jugador1 es: ", self.jugador1.puntaje)
        #Obtiene el nombre del jugador1 y lo imprime
        print("el nombre del jugador 1 es: ",self.nombrejugador1.get())
        #imprime el puntaje del jugador2
        print("el puntaje del jugador2 es: ", self.jugador2.puntaje)
        #Obtiene el nombre del jugador2 y lo imprime
        print("el nombre del jugador 2 es: ",self.nombrejugador2.get())

    #Funcion que guarda una partida con los valores actuales de las variables en el archivo partidas.json
    def GuardarPartida(self, data,json_file):
        #Abre el archivo partidas.json en forma de escritura
        with open(self.json_file,'w') as file:
            #Vuelca los datos almacenados en data en el archivo partidas.json con una identacion de 4, 
            #esto le añade estetica al guardar los datos  
            json.dump(data, file, indent = 4)
            #Cierra el archivo partidas.json
            file.close()

    #Funcion que guarda una partida con los valores actuales de las variables en el archivo clasificaciones.json
    def GuardarPuntajes(self, puntajes,json_puntaje):
        #Abre el archivo partidas.json en forma de escritura
        with open(self.json_puntaje,'w') as file:
            #Vuelca los datos almacenados en data en el archivo partidas.json con una identacion de 4, 
            #esto le añade estetica al guardar los datos  
            json.dump(puntajes, file, indent = 4)
            #Cierra el archivo partidas.json
            file.close()

    #Funcion que serializa los datos de la clase para que se puedan almacenar en un diccionario
    #Es llamada por datospuntajes para obtener los datos de las partidas en forma de diccionario
    def encoder_puntajes(self):
        #Comprueba si el objeto es de la clase adminjson()
        if isinstance(self, adminjson):
            #Crea una lista llamada puntaje auxiliar
            puntajesaux=[]
            #Crea un diccionario llamado puntaje
            puntaje={}
            #Imprime en consola las listas de los nombres y la puntuacion-----------¬
            print("Esta es la lista de los nombres: ", self.listaNombres)          #|
            print("Esta es la lista de las puntuaciones: ",self.listaPuntuacion)   #|
            #------------------------------------------------------------------------
            #Obtiene el largo de l a lista y lo almacena en tamañolista
            tamañolista=len(self.listaPuntuacion)
            #Entra a un for donde el iterador hace funcion de indice y recorre el largo de la lista
            for iterador in range(tamañolista):
                #Agrega a travez de metodo .append() los datos de listanombre y listapuntuacion de acuerdo
                #al valor del iterador en la lista puntajesaux
                #Almacena los datos obtenidos de listaNombres bajo el indice de diccionario 'Nombre'
                #Almacena los datos obtenidos de listaPuntuacion bajo el indice de diccionario 'Puntuacion'
                puntajesaux.append({'Nombre': self.listaNombres[iterador] ,'Puntuacion':self.listaPuntuacion[iterador]})
                #Actualiza los valores del diccionario puntaje, bajo el indice "Puntajes" en donde almacena la lista con
                #los datos de listaNombres y listaPuntuacion
                puntaje["Puntajes"]=puntajesaux
            #devuelve el diccionario puntaje
            return puntaje
        #Si el objeto no es del tipo adminjson entra en el else
        else:
            #Obtiene una exepcion y sube en su lugar la informacion deseada
            raise TypeError(f'Objeto {self} no es de tipo sdminjson')

    #Funcion lamada por el metodo ListarMejoresJugadores()
    #Se encarga de obtener el diccionario de los puntajes y luego guardarlos en el archivo json clasificaciones.json
    def datospuntajes(self):
        #Le asigna el valor obtenido del metodo encoder_puntajes() a diccionariountajes
        self.diccionarioPuntajes = self.encoder_puntajes()
        #Llama al metodo GuardarPuntajes y pasa como parametros los datos almacenados en diccionarioPuntajes y json_puntajes
        self.GuardarPuntajes(self.diccionarioPuntajes, self.json_puntaje)


    #Funcion que es llamada por verificarnombre() para agregar la nueva partida en el archivo partidas.json
    def datos(self):
        #Akmacena el nombre de la partida en nombrePartida
        self.nombrePartida=self.getnombrepartida()
        print("Este es el nombre de la partida: ", self.nombrePartida.get())
        #Abr json_file el cual almacena el nombre del archivo json que ontiene los datos de las partidas
        with open(self.json_file) as file:
            #Almacena los datos del archivo partidas.json en la variable data
            data=json.load(file)
            #Almacena los valores de los datos bajo el indice partidas del archivo json en tempo
            tempo=data["partidas"]
            #Llama el metodo encoder_partida() y obtiene los datos de la nueva partida en forma de diccionario,
            #el cuale almacena en la variable partida
            partida=self.encoder_partida()
            #Imprime los valores de la nueva partida almacenadops en la variable partida
            print(partida)
            #Concatena el diccionario con los datos almacenados en la variable partida a los datos del diccionario de las 
            tempo.append(partida)
            #Almacena la varible tempo con los datos actualizados de las partidas en data bajo el indice "partidas" 
            data["partidas"]=tempo
            #Cierra el archivo partidas.json
            file.close()
        #Devuelve data, el cual contiene los datos nuevos de las partidas
        return data
    
    #Funcion que serializa los datos de la clase para que se puedan almacenar en un diccionario
    #Es llamada por datos() para obtener los datos de las partidas en forma de diccionario
    def encoder_partida(self):
        #Le asigna un valor a la variable pista
        pista = 2
        #Comprueba si el objeto es de la clase adminjson()
        if isinstance(self, adminjson):
            #Imprime el nombre del jugador2 en consola
            print(self.nombrejugador1.get())
            #Imprime el nombre del jugador1 en consola
            print(self.nombrejugador2.get())
            velocidad1=self.jugador1.velocidad
            velocidad2=self.jugador2.velocidad
            return {'Nombre Partida':self.nombrePartida.get(), 'Jugador1':self.nombrejugador1.get(), 'Puntuacion1':self.jugador1.puntaje,'Posicion1':self.jugador1.rect.center, 'Rotacion1':self.jugador1.rotacion, 'Aceleracion1':self.jugador1.aceleracion, "Velocidad1":velocidad1,
             'Jugador2':self.nombrejugador2.get(), 'Puntuacion2':self.jugador2.puntaje, 'Posicion2':self.jugador2.rect.center, 'Rotacion2':self.jugador2.rotacion, 'Aceleracion2': self.jugador2.aceleracion,"Velocidad2":velocidad2, 'Etapa':pista}
        #Si no es de clase adminjson() captura el error y devuelve un mensaje personalizado
        raise TypeError(f'Objeto {self} no es de tipo sdminjson')

    #Funcion que serializa los datos de la partida en curso para que se puedan almacenar en un diccionario
    #Es llamada por pausar() para obtener los datos de la partida en forma de diccionario
    def encoder_partida_aux(self):
        #Le asigna un valor a la variable pista
        pista = 2
        #Comprueba si el objeto es de la clase adminjson()
        if isinstance(self, adminjson):
            #Imprime el nombre del jugador2 en consola
            print(self.nombrejugador1.get())
            #Imprime el nombre del jugador1 en consola
            print(self.nombrejugador2.get())

            return {'Jugador1':self.nombrejugador1.get(), 'Puntuacion1':self.jugador1.puntaje,'Posicion1':self.jugador1.rect.center, 'Rotacion1':self.jugador1.rotacion, 'Aceleracion1':self.jugador1.aceleracion,
             'Jugador2':self.nombrejugador2.get(), 'Puntuacion2':self.jugador2.puntaje, 'Posicion2':self.jugador2.rect.center, 'Rotacion2':self.jugador2.rotacion, 'Aceleracion2': self.jugador2.aceleracion, 'Etapa':pista}
        #Si no es de clase adminjson() captura el error y devuelve un mensaje personalizado
        raise TypeError(f'Objeto {self} no es de tipo sdminjson')

    #Funcion que lee el json y retorna un diccionario con los datos
    def LeerPartida(self, json_file):
        #Abre json_file en modo lectura, el cual contiene el nombre del archivo json donde se han almacenado las partidas
        with open(json_file) as file:
            #Obtiene todos los datos del archivo json y los almacena en data
            self.data = json.load(file)
            #Cierra el archivo
            file.close
            #Devuelve data el cual continene los datos del archivo partidas.json
            return self.data

    #Funcion que valida si una partida se puede guardar, valida que el nombre no de la 
    #partida por guardar no exista en el archivo partidas.json, en caso de que exista una partida con el mismo
    #nombre no se guarda la partida, recibe como parametro el nombre de la partida
    def ValidarNombreNuevaPartida(self, nombreNuevaPartida):
        #Llama la funcion LeerPartida y alamacena los datos en dic
        dic = self.LeerPartida(self.json_file)
        #Entra a un for en el cual recorre todos los datos del indice 'partidas' en dic
        for partida in dic['partidas']:
            #Pregunta si el dato almacenado bajo el indice 'Nombre Partida' es igual que el nombre de la nueva partida
            if(partida['Nombre Partida']==nombreNuevaPartida):
                #Si es son iguales imprime que el nombre no es valido
                print("Nombre no valido")
                #Y devueleve el valor booleano False
                return False
        #Si termina de recorrer los datos de las partidas guardadas y el nombre de la nueva partida no es igual
        #al de una partida guardada anteriormente, imprime que el nombre es valido
        print("Nombre valido")
        #Y devuelve el valor booleano True
        return True

    #Metodo llamado por el botong de la ventanagaurdar que verifica si se puede guardar la partida, y llama la funcion de guardar
    def verificarnombre(self):
        #Almacena en datas el valor obtenido del metodo datos()
        datas = self.datos()
        #Almacena en nombrePartida el nombre de la partida obtenido en getnombrepartida()
        self.nombrePartida=self.getnombrepartida()
        #Imprime en consola el nombre de la partida
        print("Nombre de partida: ", self.nombrePartida)
        #Llega al if en el cual llama el metodo ValidarNombreNuevaPartida() y pasa como parametro
        #el nombre de la partida, obriene de este metodo un valor booleano, si es True entra en el if
        if(self.ValidarNombreNuevaPartida(self.nombrePartida)):
            #Llama el metodo GuardarPartida() y pasa como parametro los datos y json_file
            #que almacena el nombre del archivo json donde se guardaran los datos
            self.GuardarPartida(datas, self.json_file)
            #Llama al metodo ListarNombresPartidas() que crea una lista con los nombres de las partidas
            self.ListarNombresPartidas()
            #Llama al metodo ListarMejoresJugadores() que crea una lista con los nombres de los jugadores 
            #y sus puntuaciones ordenada de forma descendente de acuerdo a sus puntajes
            self.ListarMejoresJugadores()
            #Cierra la ventana guardar y queda la ventana pausa
            self.ventanaguardar.destroy()
            #Imprime en consola que si se guardo la partida
            print("Se guardo la partida")
        #Si el valor obtenido  de ValidarNombreNuevaPartida es False entra al else
        else:
            #Este else imprime en consola "No se guardo la partida"
            print("No se guardo la partida")

    #Funcion que retorna una lista de los nombres de todas las partidas
    def ListarNombresPartidas(self):
        #Lee el json mediante la funcion LeerPartida() y lo almacena en partidas
        partidas = self.LeerPartida(self.json_file) 
        #Crea una lista vacia llamada lista
        lista = []
        #Recorre los datos guardados en el indice 'partidas' 
        for partida in partidas['partidas']:
            #Agrega a la lista lod datos dcon el indice 'Nombre Partida' los cuales corresponden a los nombres de las partidas guardadas
            lista.append(partida['Nombre Partida'])
        #Cuando sale del coclo for, imprime la lista
        return print(lista)

    #Funcion que lee el json y extrae una lista de los nombres y otra de los puntajes
    #Se ordena la lista de los puntajes en paralelo a la de nombres mediante el
    #algoritmo de ordenamiento por inserción, luego se retornan ambas listas
    #Primero la de nombres y luego la de puntajes
    def ListarMejoresJugadores(self):
        #Almacena los datos obtenidos de partidas.json
        partidas = self.LeerPartida(self.json_file) 
        #Crea una lista vacia llamada listaNombres
        listaNombres = []
        #Crea una lista vacia llamada listaNombres
        listaPuntuacion = []
        #Recorre partidas en el indice 'partidas'
        for partida in partidas['partidas']:
            #Concatena  los datos bajo el indice 'Jugador' en listaNombres
            listaNombres.append(partida['Jugador1'])
            #Concatena  los datos bajo el indice 'Puntuacion' en listaPuntuacion
            listaPuntuacion.append(partida['Puntuacion1'])
            #Concatena  los datos bajo el indice 'Jugador' en listaNombres
            listaNombres.append(partida['Jugador2'])
            #Concatena  los datos bajo el indice 'Puntuacion' en listaPuntuacion
            listaPuntuacion.append(partida['Puntuacion2'])


        #Almacena el largo de listaPuntuacion en la variable tamaño
        tamaño = len(listaPuntuacion)
        #Entra al for donde itera i en el rango de 1 al tamaño 
        for i in range(1, tamaño):
            #Almacena el dato almacenado en la posicion i de listaPuntuacion en puntuacion
            puntuacion = listaPuntuacion[i]
            #Almacena el dato almacenado en la posicion i de listaNombres en nombre
            nombre = listaNombres[i]
            #Asigna el valor de i a j
            j = i
            #Entra al ciclo while donde no saldrá mientras j sea mayor que 0 y el valor en listapuntuacion anterior sea mayor
            #al valor de puntuacion, esto con el objetivo de ordenar las listas de menor a mayor segun los valores de listaPuntuacion
            while j > 0 and listaPuntuacion[j-1] > puntuacion:
                #Cambia el valor de listapuntuacion en el indice j con el valor anterior en la lista 
                listaPuntuacion[j] = listaPuntuacion[j-1]
                #Paralelo a esto hace lo mismo con la listaNombres, para que el valor de listaNombre en la posicion j 
                #sea el correspondiente al de listaPuntuacion
                listaNombres[j] = listaNombres[j-1]
                #Reduce j en 1
                j -= 1
            #En la posicion j de listaPuntuacion almacena el dato puntuacion
            listaPuntuacion[j] = puntuacion
            #En la posicion j de listaPuntuacion almacena el dato nombre
            listaNombres[j] = nombre
        #Reordena listaNombres del valor mayor a menor
        listaNombres.reverse()
        #Reordena lisaPuntuacion del valor mayor a menor
        listaPuntuacion.reverse()
        #Almacena la listaNombres en la variable listaNombres
        self.listaNombres=listaNombres
        #Almacena la listaPuntuacion en la variable listaPuntuacion
        self.listaPuntuacion=listaPuntuacion
        #Llama el metodo datospuntajes(), el cual obtiene los datos de los puntajes y 
        #luego los guarda en el archivo clasificaciones,json
        self.datospuntajes()
        #Imprime la lista pbtenida de nonbres y puntuaciones y los imprime en consola
        return print([listaNombres, listaPuntuacion])

    #Funcion que contruye la ventana de guardar partida
    #Es llamado por la funcion pausar()
    def guardar(self):
        #Imprime en la consola que si se guardara la partida
        print("Si va a guardar")
        #Crea una ventana mediante el metodo .Toplevel() llamada ventana guardar, con el fondo verde
        self.ventanaguardar=Toplevel(bg="Green")
        #Personaliza el nombre del titulo a "Guardar Partida"
        self.ventanaguardar.title("Guardar partida")
        #Define las dimensiones de la ventana
        self.ventanaguardar.geometry("600x400")
        #Crea una etiqueta con el titulo en la ventana, le aplica formato, lo acomoda en el centro y lo empaqueta
        etiqueta=Label(self.ventanaguardar,text="Introduzca un nombre para ", bg="Green",font=("Constantia",18, "bold"), justify="center").pack()
        #Crea una etiqueta con la segunda parte del titulo en la ventana, le aplica formato, lo acomoda en el centro y lo empaqueta
        etiqueta1=Label(self.ventanaguardar,text=" guardar la partida", bg="Green",font=("Constantia",18, "bold"), justify="center").pack()
        #Crea un etiqueta que funcionara como espacio y lo empaqueta
        espacio1=Label(self.ventanaguardar, text="", bg="Green").pack()
        #Crea una caja de texto en la ventanaguardar, almacena el texto en NombreNuevaPartida, le aplica formato al texto y lo empaqueta
        nombrepartida=Entry(self.ventanaguardar,textvariable=self.NombreNuevaPartida, width=20, font=("Constantia",20, "bold"), justify="center" ).pack()
        #Crea un etiqueta que funcionara como espacio y lo empaqueta
        espacio2=Label(self.ventanaguardar, text="", bg="Green").pack()
        #Crea un boton llamado botong en ventanaguardar el cual se muestra en la interfaz
        #con el nombre Guardar, llama la funcion verificarnombre() y se empaqueta
        botong=Button(self.ventanaguardar, text="Guardar", width=10, relief= "raised",font=("Constantia",18, "bold"), command=self.verificarnombre).pack()
        #Aplica el metodo .trasient() el cual recibe como parametro la raiz y sobrepone la ventana sobre las demas
        self.ventanaguardar.transient(raiz)
    
    #Metodo que devuelve el nombre de la partida
    #Es llamada por datos() y verificarnombre()
    def getnombrepartida(self):
        #Devuelve el valor almacenado en NombreNuevaPartida
        return self.NombreNuevaPartida

#clase meta
class Meta(pygame.sprite.Sprite):#recibe como parametro la clase padre pygame.sprite.Sprite
    def __init__(self):#define el init com parametros vacios
        #hereda init de la clase
        super().__init__()
        self.imagen = pygame.image.load("imagenes/Meta.png") #cargar la imagen de la meta
        self.rect=self.imagen.get_rect() #obtiene el rectangulo de la meta
        self.rect.x = 0# se define el rectangulo en x de la clase
        self.rect.y = 0 # se define el rectangulo en x de la clase
        self.velocidad_y = 5  # da una velocidad para que la meta desaparezca

    def update(self):# se define el metodo update

        # actualiza la velocidad de la meta
        self.rect.y += self.velocidad_y  # suma pixeles a la posicion de la meta para que se desplace junto al fondo

#calse mina
class Mina(pygame.sprite.Sprite):#recibe como parametro la clase padre pygame.sprite.Sprite
    def __init__(self): #define el constructor sin parametros
        super().__init__()#hereda el constructor del pygame.sprite.Sprite
        self.image = pygame.image.load("imagenes/Mina.png") #cargar la imagen de la mina
        self.rect=self.image.get_rect() #obtiene el rectangulo de las minas
        self.rect.x = random.randrange((920 + 100)) # da una ubicacion random sin que salga de los bordes
        self.rect.y = random.randrange(360) # da una ubicacion random si que entre en el campo de inicio del jugador
        self.velocidad_y = 5  # da una velocidad para que las minas desaparzcan con el movimiento del fondo


    def update(self):# define el metodo update

        # actualiza la velocidad del dummie
        self.rect.y += self.velocidad_y  # suma pixeles a la posicion de las minas para que se mueva

#clase arbol
class Arbol(pygame.sprite.Sprite):# define la clase Arbol recibiendo como parametro la clase padre pygame.sprite.Sprite
    def __init__(self):#define el constructor, el cual no recibe parametros
        super().__init__() # se hereda la super clase de la clase padre pygame.sprite.Sprite
        self.image = pygame.image.load("imagenes/Arbol.png") #cargar la imagen de los arboles
        self.rect=self.image.get_rect() #obtiene el rectangulo de los arboles
        self.rect.x = random.randrange((920 + 100)) # da una ubicacion random sin que salga de los bordes
        self.rect.y = random.randrange(360) # da una ubicacion random si que entre en el campo de inicio del jugador
        self.velocidad_y = 5  # da una velocidad para que los arboles desaparzcan con el movimiento del fondo

    def update(self): # se define el metodo update

        # actualiza la velocidad del dummie
        self.rect.y += self.velocidad_y  # suma pixeles a la posicion delos arboles para que se mueva

class Dummies1(pygame.sprite.Sprite):#define la clase Dummies1 recibiendo como parametro la clase padre pygame.sprite.Sprite
    def __init__(self):#define el constructor, el cual no recibe parametros
        super().__init__()# se hereda la super clase de la clase padre pygame.sprite.Sprite
        self.image= pygame.image.load("imagenes/enemis_level1.png") #cargar la imagen del enemigo
        self.rect=self.image.get_rect() #obtiene el rectangulo de la imagen del enemigo
        self.rect.x = random.randrange((800 + 100)) # da una ubicacion random sin que salga de los bordes
        self.rect.y = random.randrange(360) # da una ubicacion random si que entre en el campo de inicio del jugador
        self.velocidad_x = random.randrange(2, 3)  # da una velocidad random para el dummie
        self.rect.center = (self.rect.x, self.rect.y) #centra el rectangulo de colisiones con respecto a la posicion de la sprite en self.rect.x y self.rect.y
    def update(self):# define el metodo update

        # actualiza la velocidad del dummie
        self.rect.x += self.velocidad_x  # suma pixeles a la posicion de dummie para que se mueva
        if self.rect.x < (100 + self.rect.width):  # si el dummie baja de la posicion 100 en x le suma la velocidad a la posicion
            self.velocidad_x += random.randrange(1, 2)# la velocidad varia en el random de 1 a 2 pixeles por segundo y se le suma en el eje x 
        if self.rect.x > 900:  # si el dummie supera la posicion 900 en x le resta la velocidad a la posicion
            self.velocidad_x -= random.randrange(1, 2)# la velocidad varia en el random de 1 a 2 pixeles por segundo y se le resta en el eje x

class Dummies2(pygame.sprite.Sprite):#define la clase Dummies2 recibiendo como parametro la clase padre pygame.sprite.Sprite
    def __init__(self):#define el constructor, el cual no recibe parametros
        super().__init__()# se hereda la super clase de la clase padre pygame.sprite.Sprite
        self.image = pygame.image.load("imagenes/enemis2_level1.png")  # cargar la imagen del enemigo
        self.rect = self.image.get_rect()  # obtiene el rectangulo de la imagen del enemigo
        self.rect.x = random.randrange((800 + 100)) # da una ubicacion random sin que salga de los bordes
        self.velocidad_x = random.randrange(2, 3)  # da una velocidad random para el dummie
        self.rect.center = (self.rect.x, self.rect.y)#centra el rectangulo de colisiones con respecto a la posicion de la sprite en self.rect.x y self.rect.y
    def update(self):# define el metodo update

        # actualiza la velocidad del dummie
        self.rect.x += self.velocidad_x  # suma pixeles a la posicion de dummie para que se mueva
        if self.rect.x < (100 + self.rect.width):  # si el dummie baja de la posicion 100 en x le suma la velocidad a la posicion
            self.velocidad_x += random.randrange(1, 2)# la velocidad varia en el random de 1 a 2 pixeles por segundo y se le suma en el eje x 
        if self.rect.x > 900:  # si el dummie supera la posicion 900 en x le resta la velocidad a la posicion
            self.velocidad_x -= random.randrange(1, 2)# la velocidad varia en el random de 1 a 2 pixeles por segundo y se le resta en el eje x

class Dummies3(pygame.sprite.Sprite):#define la clase Dummies3 recibiendo como parametro la clase padre pygame.sprite.Sprite
    def __init__(self):#define el constructor, el cual no recibe parametros
        super().__init__()# se hereda la super clase de la clase padre pygame.sprite.Sprite
        self.image= pygame.image.load("imagenes/enemis3_level1.png") #cargar la imagen del enemigo
        self.rect=self.image.get_rect() #obtiene el rectangulo de la imagen del enemigo
        self.rect.x = random.randrange((800 + 100)) # da una ubicacion random sin que salga de los bordes
        self.rect.y = random.randrange(360) # da una ubicacion random si que entre en el campo de inicio del jugador
        self.velocidad_x = random.randrange(2, 3) # da una velocidad random para el dummie de 2 a 3 pixeles por segundo
        self.rect.center = (self.rect.x,self.rect.y)#centra el rectangulo de colisiones con respecto a la posicion de la sprite en self.rect.x y self.rect.y
    def update(self):# define el metodo update

        # actualiza la velocidad del dummie
        self.rect.x += self.velocidad_x # suma pixeles a la posicion de dummie para que se mueva
        if self.rect.x < (100 + self.rect.width): # si el dummie baja de la posicion 100 en x le suma la velocidad a la posicion
            self.velocidad_x += random.randrange(1, 2)# la velocidad varia en el random de 1 a 2 pixeles por segundo y se le suma en el eje x 
        if self.rect.x > 900: # si el dummie supera la posicion 900 en x le resta la velocidad a la posicion
            self.velocidad_x -= random.randrange(1, 2)# la velocidad varia en el random de 1 a 2 pixeles por segundo y se le resta en el eje x

# clase jugador 1
class Jugador1(pygame.sprite.Sprite):# define la clase Jugador1 la cual recibe como parametro la clase padre pygame.sprite.Sprite
    def __init__(self, datospartida):# define el constructor el cual recibe como parametros
        # la posicion en x la posicion en y,el angulo del vehiculo, el largo del vehiculo, la maxima_rotacion del vehiculo y la maxima aceleracion del mismo.
        super().__init__() # hereda la superclase del pygame.sprite.Sprite
        self.posicion=[]
        self.posicion.append(datospartida["Posicion1"])
        self.x=self.posicion[0][0]
        self.y=self.posicion[0][1]
        self.imagen = pygame.image.load("imagenes/Jugador 1.png") #carga la imagen del jugador
        self.rect = self.imagen.get_rect() # define un rectangulo al jugador
        self.rect.center = (self.x, self.y)# centra el cuadro de colisiones en las posiciones x y.
        self.posicion = Vector2(self.x, self.y)# la posicion la recibe el vector2 con el fin de tenerla en una sola variable y poder modificarle
        self.velocidad = Vector2(0.0, 0.0)# la velocidad se posiciona en un vector con el fin de poder manipularla en una sola variable en ambos ejes
        self.angulo = 0.0# se define el angulo de la clase
        self.largoVehiculo = 3# se define el largo de la clase
        self.maxima_aceleracion = 200.0# se define la maxima aceleracion de la clase
        self.maxima_rotacion = 30 #se define la maxima aceleracion de la clase
        self.maxima_velocidad = 200#se define la maxima velocidad de la clase
        self.romper_desaceleracion = 200 # se define a la velocidad al iniciar la aceleracion
        self.desaceleracion_libre = 2 # se define la desaceleracion al dejar de moverse
        self.arranque = pygame.mixer.Sound("sonido/acelerar.mp3")# se define los archivos de sonido de aceleracion del jugador1
        self.frenado = pygame.mixer.Sound("sonido/frenando.mp3")# se define los archivos de sonido de  frenado del jugador1
        self.puntaje=datospartida["Puntuacion1"]# se define la variable puntuacion del jugador 1
        self.aceleracion = datospartida["Aceleracion1"]# se define la variable aceleracion del jugador1
        self.rotacion = datospartida["Rotacion1"]# se define la rotacion del jugador1

    def disparo(self): # se define el metodo disparo
        bala = Disparo(self.rect.centerx, self.rect.top)# se define la posicion de salida de la bala en las coordenadas dadas en los parametros que recibio

    # actualiza el jugador 1
    def Update(self, dt): # define el metodo update que recibe como parametro la variable dt(distancia entre tiempo)
        self.velocidad += (self.aceleracion * dt, 0)# define la velocidad a la cual el jugador tendra agregandole, la variable del self aceleracion x la dt, en el eje y 0
        self.velocidad.x = max(-self.maxima_velocidad, min(self.velocidad.x, self.maxima_velocidad))# define la velocidad en x la cual sera el minimo de la velocidad entre
        # la velocidad x y la maxima velocidad del momento y el maximo entre el negatvo de la velocidad y el minimo resultante de la tupla anteriormente mencionada
        self.rect.x = self.posicion.x# rectangulo en x se posiciona en la posicion en x
        self.rect.y = self.posicion.y# rectangulo en y se posiciona en la posicion en y
        if self.rotacion:# si la rotacion 
            radio_rotacion = self.largoVehiculo / tan(radians(self.rotacion))# el radio de rotacion
            #va a ser igual a la mitad del largo del vehiculo entre el angulo tangente en radianes de la rotacion 
            velocidad_angular = self.velocidad.x / radio_rotacion# la velocidad angular sera la velocidad en x entre el radio de rotacion 
        else:# en caso contrario
            velocidad_angular = 0# que la velocidad angular sea igual a 0

        self.posicion += self.velocidad.rotate(-self.angulo) * dt# la posicion del jugador se le sumara la
        #velocidad de rotacion recibiendo como parametro el angulo negativo  para poder darle la visualizacion fisica de rotacion y para su naturalidad se multiplica por dt
        self.angulo += degrees(velocidad_angular) * dt# el angulo sera en grados recibiendo la velocidad angular para su rotacion multilicad por la distancia entre tiempo

class Disparo(pygame.sprite.Sprite):# define la clase disparo y recibe como parametro la clase padre pygame.sprite.Sprite
    def __init__(self,x,y):# define el constructor que recibe como parametros x y y
        super().__init__()# hereda el constructor de la superclase pygame.sprite.Sprite
        self.image=pygame.image.load("imagenes/bala.png")# define la imagen de la clase bala
        self.rect=self.image.get_rect()# crea el cuadro de colisiones del sprite
        self.rect.bottom=y# crea su posicion con respecto al eje y 
        self.rect.centerx=x# centra la bala en el centro del eje x
    def update(self):# metodo update
        self.rect.y=25 #define el cuadro de colision en y asi como su velocidad
        if self.rect.bottom<0:# en caso que la posicion en y sea menor a 0
            self.kill()# destruye el proyectil

# clase del jugador2
class Jugador2(pygame.sprite.Sprite):# define la clase Jugador1 la cual recibe como parametro la clase padre pygame.sprite.Sprite
    def __init__(self,datospartida):# define el constructor el cual recibe como parametros
        # la posicion en x la posicion en y,el angulo del vehiculo, el largo del vehiculo, la maxima_rotacion del vehiculo y la maxima aceleracion del mismo.
        super().__init__()# hereda la superclase del pygame.sprite.Sprite
        self.posicion=[]
        self.posicion.append(datospartida["Posicion2"])
        self.x=self.posicion[0][0]
        self.y=self.posicion[0][1]
        self.posicion = Vector2(self.x, self.y)# la posicion la recibe el vector2 con el fin de tenerla en una sola variable y poder modificarle
        self.velocidad = Vector2(0.0, 0.0)# la velocidad se posiciona en un vector con el fin de poder manipularla en una sola variable en ambos ejes
        self.image = pygame.image.load("imagenes/Jugador 2.png")#carga la imagen del jugador2
        self.rect = self.image.get_rect()# define un rectangulo al jugador
        self.rect.center = (self.x, self.y)# centra el cuadro de colisiones en las posiciones x y.
        self.angulo = 0.0# se define el angulo de la clase
        self.largoVehiculo = 3# se define el largo de la clase
        self.maxima_aceleracion =200# se define la maxima aceleracion de la clase
        self.maxima_rotacion = 30#se define la maxima aceleracion de la clase
        self.maxima_velocidad = 200#se define la maxima velocidad de la clase
        self.romper_desaceleracion = 200# se define a la velocidad al iniciar la aceleracion
        self.desaceleracion_libre = 2 # se define la desaceleracion al dejar de moverse
        self.arranque = pygame.mixer.Sound("sonido/acelerar.mp3")# se define los archivos de sonido de aceleracion del jugador2
        self.frenado = pygame.mixer.Sound("sonido/frenando.mp3")# se define los archivos de sonido de  frenado del jugador2
        self.puntaje=datospartida["Puntuacion2"]# se define la variable puntuacion del jugador 2
        self.aceleracion = datospartida["Aceleracion2"]# se define la variable aceleracion del jugador2
        self.rotacion = datospartida["Rotacion2"]# se define la rotacion del jugador2

    # actualiza el jugador2
    def update(self, dt2):# define el metodo update que recibe como parametro la variable dt(distancia entre tiempo)
        self.velocidad += (self.aceleracion * dt2, 0)# define la velocidad a la cual el jugador tendra agregandole, la variable del self aceleracion x la dt, en el eje 
        self.velocidad.x = max(-self.maxima_velocidad, min(self.velocidad.x, self.maxima_velocidad))# define la velocidad en x la cual sera el minimo de la velocidad entre
        # la velocidad x y la maxima velocidad del momento y el maximo entre el negatvo de la velocidad y el minimo resultante de la tupla anteriormente mencionada
        self.rect.x = self.posicion.x# rectangulo en x se posiciona en la posicion en x
        self.rect.y = self.posicion.y# rectangulo en y se posiciona en la posicion en y
        if self.rotacion:# si la rotacion
            radio_rotacion = self.largoVehiculo / tan(radians(self.rotacion))# el radio de rotacion
            #va a ser igual a la mitad del largo del vehiculo entre el angulo tangente en radianes de la rotacion 
            velocidad_angular = self.velocidad.x / radio_rotacion# la velocidad angular sera la velocidad en x entre el radio de rotacion 
        else:# en caso contrario
            velocidad_angular = 0# que la velocidad angular sea igual a 0

        self.posicion += self.velocidad.rotate(-self.angulo) * dt2# la posicion del jugador se le sumara la
        #velocidad de rotacion recibiendo como parametro el angulo negativo  para poder darle la visualizacion fisica de rotacion y para su naturalidad se multiplica por dt
        self.angulo += degrees(velocidad_angular) * dt2# el angulo sera en grados recibiendo la velocidad angular
         #para su rotacion multilicad por la distancia entre tiempo



# clase juego
class Juego:# se define la clase juego 
    def __init__(self):# el constructor no posee parametros
        pygame.init()# se inicia la funcion de iniciar el juego de pygame
        self.partidainicial="partidainicial.json"#Almacena el nombre de la partida inicial en partidainicial
        pygame.display.set_caption("Death Dakar") # da nombre a la ventana de juego
        ANCHO = 1080 # ancho de la pantalla
        ALTURA = 720# alto de la pantalla
        self.reloj = pygame.time.get_ticks() // 1000# se define un temporizador en la variable que se divido por 1000 para su obtencion en segundos
        self.screen = pygame.display.set_mode((ANCHO, ALTURA)) # dibuja la pantalla
        self.clock = pygame.time.Clock()# se define el reloj del juego
        self.ticks = 60# se define los fps por segundo
        self.exit = False# si para salir es falso
        self.fondo = pygame.image.load("imagenes/Fondodecarrera.png")#carga el el background del juego

    def LeerPartida(self, partidajson):
        #Abre json_file en modo lectura, el cual contiene el nombre del archivo json donde se han almacenado las partidas
        with open(partidajson) as file:
            #Obtiene todos los datos del archivo json y los almacena en data
            self.data = json.load(file)
            #Cierra el archivo
            file.close
            #Devuelve data el cual continene los datos del archivo partidas.json
            return self.data
        #Crea el menu de pausa, es llamado por la funcion pausar

    #Menu deplegado al presionar la tecla "p" durante la partida
    def menupausa(self):
        #Crea una ventana llamada ventanapausa con el metodo Toplevel
        self.ventanapausa=Toplevel(bg="Grey")
        #Define a "Juego pausado" como el titulo de la ventana
        self.ventanapausa.title("Juego pausado")
        #Define las dimensiones de la ventana, una altura de 600 y ancho de 400
        self.ventanapausa.geometry("600x400")
        #Crea una etiqueta con el texto "Pausa" en ventanapausa llamado etiqueta, le agrega formato y lo empaqueta
        etiqueta=Label(self.ventanapausa,text="Pausa", bg="Grey",font=("Constantia",18, "bold"), justify="center").pack()
        #Crea una etiqueta llamada espacio1 el cual funciona como espaciador en la ventanapausa y la empaqueta
        espacio1=Label(self.ventanapausa, text="", bg="Grey").pack()
        #Crea un boton llamado botoncontinuar en ventanapausa, con 10 de ancho, con formato y llama el metodo pausar con el parametro 1 y lo empaqueta
        botoncontinuar=Button(self.ventanapausa, text="Continuar", width=10, relief= "raised",font=("Constantia",18, "bold"), command=lambda:self.pausar(1)).pack()
        #Crea un boton llamado botoniniciar en ventanapausa, con 10 de ancho, con formato y llama el metodo pausar con el parametro 2 y lo empaqueta
        botonreiniciar=Button(self.ventanapausa, text="Reiniciar", width=10, relief= "raised",font=("Constantia",18, "bold"), command=lambda:self.pausar(2)).pack()
        #Crea un boton llamado botonguardar en ventanapausa, con 10 de ancho, con formato y llama el metodo pausar con el parametro 3 y lo empaqueta
        botonguardar=Button(self.ventanapausa, text="Guardar", width=10, relief= "raised",font=("Constantia",18, "bold"), command=lambda:self.pausar(3)).pack()
        #Crea un boton llamado botonsalir en ventanapausa, con 10 de ancho, con formato y llama el metodo pausar con el parametro 4 y lo empaqueta
        botonsalir=Button(self.ventanapausa, text="Salir", width=10, relief= "raised",font=("Constantia",18, "bold"), command=lambda:self.pausar(4)).pack()
        #Aplica el metodo .transient() que recibe como parametro la raiz y transpone la ventana sobre las demas ventanas y frames
        self.ventanapausa.transient(raiz)

    #Metodo llamado por los botones de menu pausa, recibe como parametro un numero con el cual ejecuta una opcion
    #Tambien es llamada al presionar "p" durante la partida
    def pausar(self, numeroopcion):
        #Asigna el valor True a la variable pausado
        pausado=True
        #Almacena el puntaje del jugador1 en puntaje
        #Almacena el puntaje del jugador2 en puntaje
        #Instancia el objeto tmp a la clase adminjson() con el puntaje del jugador1
        tmp=adminjson(self.jugador1, self.jugador2)
        #Guarda el numero de numeroopcion como opcion 
        self.opcion=numeroopcion
        #Obtiene los datos de la partida en curso y los almacena en partida en curso
        continuarpartida=tmp.encoder_partida_aux()
        reiniciarpartida=self.LeerPartida(self.partidainicial)
        #Mientras pausado tiene el valor booleano True
        while pausado==True:
            print("Entra a la pausa")
            #Verifica los valores de self.opcion
            #Si el valor es 1 entra en el if
            if self.opcion==1:
                #Imprime en consola la opcion que se elijio
                print("Opcion 1: Continuar")
                #Cambia el valor de pausado a False
                pausado=False
                #Cierra ventanapausa con el metodo .destroy()
                self.ventanapausa.destroy()
                #Vuelve a correr la partida
                self.correr(continuarpartida)
            
            #Si el valor es 2 entra en el elif
            elif self.opcion==2:
                #Imprime en consola la opcion que se elijio
                print("Opcion 2: Reiniciar")
                #Cambia el valor de pausado a False
                pausado=False
                #Cierra ventanapausa con el metodo .destroy()
                self.ventanapausa.destroy()
                #Vuelve a correr la partida
                self.correr(reiniciarpartida)

            #Si el valor es 3 entra en el elif   
            elif self.opcion==3:
                #Imprime en consola la opcion que se elijio
                print("Opcion 3: Guardar")
                #Aplica el metodo .guardar() al objeto tmp que es de tipo adminjson()
                tmp.guardar()

            #Si el valor es 1 entra en el if
            elif self.opcion==4:
                #Imprime en consola la opcion que se elijio
                print("Opcion 4: Salir")
                #Cambia el valor de pausado a False
                pausado=False
                #Cierra ventanapausa con el metodo .destroy()
                self.ventanapausa.destroy()
                #Cierra el juego mediante el comando pygame.quit()
                pygame.quit()

            #Si la opcion no es ningun numero del 1 al 4 entra a else
            else: 
                #Imprime en la consola que se crea menupausa()
                print("Llama a menupausa")
                #Llama a menupausa() el cual crea el menu pausa
                self.menupausa()

    def correr(self, datospartida):# define el metodo de correr el cual se encarga de darle funcionalidad al programa
        jugador1 = Jugador1(datospartida)#--
        jugador2 = Jugador2(datospartida)#  |
        enemigo1 = Dummies1()#  |
        enemigo2 = Dummies2()#  | se instancias los objetos de las diferentes clases
        enemigo3 = Dummies3()#  |
        linea_salida = Meta()#  |
        arboles=Arbol()      #  |
        minas=Mina()         #--
        y=0 # se define la variable y
        # pygmae.time.settimer(userevent+1,180000
        while not self.exit:# mientras no se use self.exit
            dt = self.clock.get_time() / 1000 # la distancia entre tiempo sera de los microsengundos divididos entre mil para definir el tiempo de movimiento
            dt2 = self.clock.get_time() / 1000# la distancia entre tiempo sera de los microsengundos divididos entre mil para definir el tiemp en movimiento
            # if pygame.event.get(userevent+1)
            # cola del evento
            for event in pygame.event.get():# mientras se obtengas los eventos en pygame
                if event.type == pygame.QUIT:# y si se presiona el quit o salir
                    self.exit = True # que la variable self.salida sea verdadero y salga del juego
            # permite la realizacion de acciones al presionar los botones designados a sus funciones, por el usuario
            pressed = pygame.key.get_pressed()# defino pressed como la variable encargada de  hacer la funcion del metodo pygame.key.get_pressed()
            if pressed[pygame.K_x]: # si preciono x
                return jugador1.disparo()# retorne el metodo del jugador1.disparo()

            elif pressed[pygame.K_p]:
                self.pausar(0)
            if pressed[pygame.K_UP]:# si presiona flecha arriba
                jugador1.arranque.play()# reprodusca el sonido instanciado en la variable arranque de jugador 1
                if jugador1.velocidad.x < 0:# si la velocidad del jugador1 es menor a cero
                    jugador1.aceleracion = jugador1.romper_desaceleracion# la aceleracion del ugador 1 sera igual a la de romper desaceleracion
                jugador1.aceleracion += 1 * dt# se le aumentara poco a poco la velocidad de un pixel por segundo 
            elif pressed[pygame.K_DOWN]:# si presiona la flecha de abajo
                if jugador1.velocidad.x > 0: #y si la velocidad del jugador1 es mayor que cero
                    jugador1.aceleracion = -jugador1.romper_desaceleracion # a la velocidad restele el romper desaceleracion 
                else:# sino
                    jugador1.aceleracion -= 1 * dt# que la aceleracion del jugador 1 se le reste un pixel por segundo
            elif pressed[pygame.K_SPACE]:# si se preciona barra espaciadora
                jugador1.frenado.play()# # reprodusca el sonido instanciado en la variable frenado de jugador 1
                if abs(jugador1.velocidad.x) > dt * jugador1.romper_desaceleracion:# si el absoluto de la velocidad del jugador 1 x es menor
                    # a la distancia entre tiempo x rimper desaceleracion
                    jugador1.aceleracion = -copysign(jugador1.romper_desaceleracion, jugador1.velocidad.x) #que la aceleracion sea la inversion
                    # de los valores de velocidad.x y la de romper desaceleracion, negativa
                else: #sino
                    jugador1.aceleracion = -jugador1.velocidad.x / dt #que la aceeracion del jugador1 sea el negativos de la velociddad entre tiempo
            else:#sino
                if abs(jugador1.velocidad.x) > dt * jugador1.desaceleracion_libre:# si el absoluto de la velocidad del jugador 1 x es menor a la distancia
                    # entre tiempo x aceleracion libre
                    jugador1.acceleration = -copysign(jugador1.desaceleracion_libre, jugador1.velocidad.x)#que la aceleracion sea la inversion
                    # de los valores de velocidad.x y la de romper desaceleracion, negativa
                else:#sino
                    if dt != 0:# si la distancia de la distancia entre tiempo es diferente a 0
                        jugador1.aceleracion = -jugador1.velocidad.x / dt# que la aceleracion de del jugador en x sea la velocidad
                        # en x entre dt
            jugador1.aceleracion = max(-jugador1.maxima_aceleracion, min(jugador1.aceleracion, jugador1.maxima_aceleracion))# que la aceleracion sea
            # el maximo de entre aceleracion y el minimo entre la aceleracion y maxima aceleracion

            if pressed[pygame.K_RIGHT]:#si se presiona flecha derecha
                jugador1.rotacion -= 30 * dt# que la rotacion del jugador se le reste 30 grados x dt
            elif pressed[pygame.K_LEFT]: # si se presiona flecha izquierda
                jugador1.rotacion += 30 * dt# que la rotacion del jugador se le sume 30 grados x dt
            else:# sino
                jugador1.rotacion = 0 # qque la rotacion sea 0
            jugador1.rotacion = max(-jugador1.maxima_rotacion, min(jugador1.rotacion, jugador1.maxima_rotacion))# que la rotacion sea el maximo entre el
            # minimo de la rotaciony maxima rotacion, y el maximo del negativo de l maxima rotacion
            pressed = pygame.key.get_pressed() #intancia la funcion pygame.key.get_pressed() en pressed

            if pressed[pygame.K_w]: #si se presiona w
                jugador2.arranque.play()# reprodusca el sonido instanciado en la variable arranque de jugador 2
                if jugador2.velocidad.x < 0:# si la velocidad del jugador2 es menor a cero
                    jugador2.aceleracion = jugador2.romper_desaceleracion # la aceleracion del jugador 2 sera igual a la de romper desaceleracion
                jugador2.aceleracion += 1 * dt2# se le aumentara poco a poco la velocidad de un pixel por segundo
            elif pressed[pygame.K_s]:# si se presiona s
                if jugador2.velocidad.x > 0:#y si la velocidad del jugador2 es mayor que cero
                    jugador2.aceleracion = -jugador2.romper_desaceleracion# a la velocidad restele el romper desaceleracion
                else:#sino
                    jugador2.aceleracion -= 1 * dt2# que la aceleracion del jugador 1 se le reste un pixel por segundo
            elif pressed[pygame.K_f]:# si se presiona f
                if abs(jugador2.velocidad.x) > dt2 * jugador2.romper_desaceleracion:# si el absoluto de la velocidad del jugador 1 x es menor
                    # a la distancia entre tiempo x rimper desaceleracion
                    jugador2.aceleracion = -copysign(jugador2.romper_desaceleracion, jugador2.velocidad.x) #que la aceleracion sea la inversion
                    # de los valores de velocidad.x y la de romper desaceleracion, negativa
                else:#sino
                    jugador2.aceleracion = -jugador2.velocidad.x / dt2 #que la aceeracion del jugador1 sea el negativos de la velociddad entre tiempo
            else:# sino
                if abs(jugador2.velocidad.x) > dt2 * jugador2.desaceleracion_libre:#que la aceleracion sea la inversion
                    # de los valores de velocidad.x y la de romper desaceleracion, negativa
                    jugador2.aceleracion = -copysign(jugador2.desaceleracion_libre, jugador2.velocidad.x)#que la aceleracion sea la inversion
                    # de los valores de velocidad.x y la de romper desaceleracion, negativa
                else: #sino
                    if dt2 != 0:# si la distancia de la distancia entre tiempo es diferente a 0
                        jugador2.aceleracion = -jugador2.velocidad.x / dt2# que la aceleracion de del jugador en x sea la velocidad
                        # en x entre dt
            jugador2.aceleracion = max(-jugador2.maxima_aceleracion, min(jugador2.aceleracion, jugador2.maxima_aceleracion)) # que la aceleracion sea
            # el maximo de entre aceleracion y el minimo entre la aceleracion y maxima aceleracion


            if pressed[pygame.K_d]:# si se presiona d
                jugador2.rotacion -= 30 * dt2# que la rotacion del jugador se le reste 30 grados x dt
            elif pressed[pygame.K_a]:# si se presiona a
                jugador2.rotacion += 30 * dt2# que la rotacion del jugador se le suma 30 grados x dt
            else: #sino
                jugador2.rotacion = 0 # que la rotacion sea 0
            jugador2.rotacion = max(-jugador2.maxima_rotacion, min(jugador2.rotacion, jugador2.maxima_rotacion)) # que la rotacion sea el maximo entre el
            # minimo de la rotaciony maxima rotacion, y el maximo del negativo de l maxima rotacion



            texto = pygame.font.SysFont("Arial", 20, True, False)# asigna a a la variable texto_puntos el tipo de letra, tamano y si esta en negrita
            informacion = texto.render("cronometro  ", 0, (0, 0, 0))# almacena el tiempo
            # y lo actualiza conforme pasa el juego y define su color el cual es negro
            texto_puntos = pygame.font.SysFont('Arial', 20, True)# asigna a a la variable texto_puntos el tipo de letra, tamano y si esta en negrita
            puntuacion = texto_puntos.render("puntaje:   " + str(jugador1.puntaje), 1, (0, 0, 0))# almacena el puntaje del jugador1
            # y lo actualiza conforme pasa el juego y su color el cual es negro


            puntuacion2 = texto_puntos.render("puntaje:   " + str(jugador2.puntaje), 1, (0, 0, 0))# almacena el puntaje del
            # jugador2 y lo actualiza conforme pasa el juego

            # grupo donde estan los objetos a colisionar teniendo como entrada los dummies y la meta, asi mismo otorga puntos al jugador que lo haga
            # crea un grupo de sprites
            sprites = pygame.sprite.Group()
            sprites.add(enemigo1)  # añade enemigo1 al grupo sprites
            sprites.add(enemigo2)  # añade enemigo2 al grupo sprites
            sprites.add(enemigo3)  # añade enemigo3 al grupo sprites

            #crea un grupo de balas
            balas = pygame.sprite.Group()

            #crea un grupo de obstaculos
            obstaculos = pygame.sprite.Group()
            obstaculos.add(arboles) # añade arboles al grupo de obstaculos
            obstaculos.add(minas) # añade minas al grupo de obstaculos

            colision = pygame.sprite.spritecollide(jugador1, sprites, True)# permite la colision de sprites del jugador2 con el grupo obstaculos, y permite desaparecer al ser destruido
            if colision:#si sucede colision
                explosion = pygame.mixer.Sound("sonido/explosion.mp3")# instancia la funcion y importa la musica
                explosion.play()# reproduce el audio contenido en la funcion
                jugador1.puntaje += 200# suma 200 puntos al colisionar el jugador con algun objeto del grupo sprite

            collision = pygame.sprite.spritecollide(jugador1, obstaculos, False)# permite la colision de sprites del jugador2 con el grupo obstaculos, y permite desaparecer al ser destruido
            if collision:# si sucede collision
                explosion = pygame.mixer.Sound("sonido/explosion.mp3")# instancia la funcion y importa la musica
                explosion.play()# reproduce el audio contenido en la funcion
                jugador1.kill()# destruye el jugador2

            colision = pygame.sprite.spritecollide(jugador2, sprites, True)# permite la colision de sprites del jugador2 con el grupo obstaculos, y permite desaparecer al ser destruido
            if colision: # si sucede collision
                explosion = pygame.mixer.Sound("sonido/explosion.mp3")# instancia la funcion y importa la musica
                explosion.play()# reproduce el audio contenido en la funcion
                jugador2.puntaje += 200 # al colisionar sumar dos puntos al jugador2
            collision = pygame.sprite.spritecollide(jugador2, obstaculos, True)# permite la colision de sprites del jugador2 con el grupo obstaculos, y permite desaparecer al ser destruido
            if collision: # si sucede collision
                explosion = pygame.mixer.Sound("sonido/explosion.mp3")# instancia la funcion y importa la musica
                explosion.play()# reproduce el audio contenido en la funcion
                jugador2.kill()# destruye el jugador2

            y_relativa = y % self.fondo.get_rect().height # se agrega una variable para que el fondo no sea estatico
            self.screen.blit(self.fondo, (0,y_relativa - self.fondo.get_rect().height))  # imprime en la ventana la imagen de fondo que se usara para el juego
            if y_relativa < 1100:  # mantiene la imagen de fondo en constante actualizacion
                self.screen.blit(self.fondo,(0, y_relativa))  # imprime la imagen de fondo contantemente para que no se vea borroso
            y+=7 # da una velocidad a la pista
            self.screen.blit(linea_salida.imagen,(linea_salida.rect.x, linea_salida.rect.y)) # imprime en la venana la linea de salida
            # logica de la actualizacion
            jugador1.Update(dt) # actualiza el jugador 1
            jugador2.update(dt2) # actualiza el jugador 2
            sprites.update() # actualiza el grupo de sprites
            obstaculos.update() # actualiza el grupo de obstaculos
            balas.update() # actualiza el grupo de balas
            linea_salida.update() # actualiza la linea de salida


            rotado = pygame.transform.rotate(jugador1.imagen, jugador1.angulo)# imprimte la rotacion segun el angulo del jugador 1
            rect = rotado.get_rect()
            self.screen.blit(rotado, jugador1.posicion)# imprime la rotacioin del jugador 1 en la poscion que se encuentre

            rotado = pygame.transform.rotate(jugador2.image, jugador2.angulo)# permite la rotacion del sprite del jugador2 dependendo del angulo pasado como parametro
            rect = rotado.get_rect()# rota la funcion
            self.screen.blit(rotado, jugador2.posicion)# imprime la rotacion del jugador 2

            self.screen.blit(puntuacion2, (16, 50)) # imprime la puntacion jugador 2
            self.screen.blit(puntuacion, (16, 30)) # imprime la puntacion jugador1
            self.screen.blit(informacion, (5, 5)) # imprime  imprime la informacion contenida en informacion

            Cronometraje = pygame.time.get_ticks() // 1000 # define el cronometro del juego en segundos
            self.clock.tick(self.ticks)# define el reloj del juego
            cronometraje = str(Cronometraje)# convierte el valor cronometraje en texto
            cronometro = texto.render(cronometraje, 100, (0, 0, 0))# variabelq que contiene el texto de la variable cronometro
            self.screen.blit(cronometro, (110, 5))#imprime el cronometro en la pantalla
            #dummies.draw(self.screen)
            sprites.draw(self.screen)# imprime todo lo integrado en el grupo sprites en la pantalla
            balas.draw(self.screen)# imprime todo lo integrado en el grupo balas en la pantalla
            obstaculos.draw(self.screen)# imprime todo lo integrado en el grupo obstaculos en la pantalla

            self.jugador1=jugador1
            self.jugador2=jugador2
            # actualiza pantalla
            pygame.display.update()#actualiza la pantalla con la funcion de pygame
            pygame.display.flip()# actualiza la pantalla
        # salir del juego
        pygame.quit()#funcion que permite quitar el juego

if __name__ == "__main__":#Define la inicializacion del juego
    root=Tk()             #Crea una ventana llamada root
    raiz = Menu(root)     #Instancia la clase Menu en la raiz
    root.mainloop()       #Aplica el metodo mainloop() para que se siga ejecutando la ventana