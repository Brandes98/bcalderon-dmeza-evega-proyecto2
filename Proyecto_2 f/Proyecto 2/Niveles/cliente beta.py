from tkinter import *           # importa todas las librerias de pygame
from tkinter import messagebox  # importa messagebox de tkinter
from tkinter import filedialog  # importa filedialog de tkinter
import os                       # importa os
import pygame                   # importa pygame
from math import tan, radians, degrees, copysign #importa tan, radians, degrees, copysign dela libreria de math
from pygame.math import Vector2 # importa Vector2 pygame.math
import json                     # importa la librerias json
import random                   # importa la libreria random
from conexiones_del_juego import Network
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
class Jugador1(pygame.sprite.Sprite):# define la clase Jugador1 la cual recibe como parametro la clase padre pygame.sprite.Sprite
    def __init__(self, x, y, angulo=0.0, largoVehiculo=3, maxima_rotacion=30, maxima_aceleracion=200.0):# define el constructor el cual recibe como parametros
        # la posicion en x la posicion en y,el angulo del vehiculo, el largo del vehiculo, la maxima_rotacion del vehiculo y la maxima aceleracion del mismo.
        super().__init__() # hereda la superclase del pygame.sprite.Sprite
        self.x=x #instancia x en la clase
        self.y= y  #instancia y en la clase
        self.imagen = pygame.image.load("imagenes/Jugador 1.png") #carga la imagen del jugador
        self.rect = self.imagen.get_rect() # define un rectangulo al jugador
        self.rect.center = (x, y)# centra el cuadro de colisiones en las posiciones x y.
        self.posicion = Vector2(x, y)# la posicion la recibe el vector2 con el fin de tenerla en una sola variable y poder modificarle
        self.velocidad = Vector2(0.0, 0.0)# la velocidad se posiciona en un vector con el fin de poder manipularla en una sola variable en ambos ejes
        self.angulo = angulo# se define el angulo de la clase
        self.largoVehiculo = largoVehiculo# se define el largo de la clase
        self.maxima_aceleracion = maxima_aceleracion# se define la maxima aceleracion de la clase
        self.maxima_rotacion = maxima_rotacion #se define la maxima aceleracion de la clase
        self.maxima_velocidad = 200#se define la maxima velocidad de la clase
        self.romper_desaceleracion = 200 # se define a la velocidad al iniciar la aceleracion
        self.desaceleracion_libre = 2 # se define la desaceleracion al dejar de moverse
        self.arranque = pygame.mixer.Sound("sonido/acelerar.mp3")# se define los archivos de sonido de aceleracion del jugador1
        self.frenado = pygame.mixer.Sound("sonido/frenando.mp3")# se define los archivos de sonido de  frenado del jugador1
        self.puntaje = 0# se define la variable puntuacion del jugador 1
        self.aceleracion = 100.0 # se define la variable aceleracion del jugador1
        self.rotacion = 0.0 # se define la rotacion del jugador1
    def move(self):
        pressed = pygame.key.get_pressed()  # defino pressed como la variable encargada de  hacer la funcion del metodo pygame.key.get_pressed()
        if pressed[pygame.K_x]:  # si preciono x
            return self.disparo()  # retorne el metodo del jugador1.disparo()
        if pressed[pygame.K_UP]:  # si presiona flecha arriba
            self.arranque.play()  # reprodusca el sonido instanciado en la variable arranque de jugador 1
            if self.velocidad.x < 0:  # si la velocidad del jugador1 es menor a cero
                self.aceleracion = self.romper_desaceleracion  # la aceleracion del ugador 1 sera igual a la de romper desaceleracion
            self.aceleracion += 1 * dt  # se le aumentara poco a poco la velocidad de un pixel por segundo
        elif pressed[pygame.K_DOWN]:  # si presiona la flecha de abajo
            if self.velocidad.x > 0:  # y si la velocidad del jugador1 es mayor que cero
                self.aceleracion = -self.romper_desaceleracion  # a la velocidad restele el romper desaceleracion
            else:  # sino
                self.aceleracion -= 1 * dt  # que la aceleracion del jugador 1 se le reste un pixel por segundo
        elif pressed[pygame.K_SPACE]:  # si se preciona barra espaciadora
            self.frenado.play()  # # reprodusca el sonido instanciado en la variable frenado de jugador 1
            if abs(self.velocidad.x) > dt * self.romper_desaceleracion:  # si el absoluto de la velocidad del jugador 1 x es menor
                # a la distancia entre tiempo x rimper desaceleracion
                 self.aceleracion = -copysign(self.romper_desaceleracion,
                                                 self.velocidad.x)  # que la aceleracion sea la inversion
                # de los valores de velocidad.x y la de romper desaceleracion, negativa
            else:  # sino
                self.aceleracion = -self.velocidad.x / dt  # que la aceeracion del jugador1 sea el negativos de la velociddad entre tiempo
        else:  # sino
            if abs(self.velocidad.x) > dt * self.desaceleracion_libre:  # si el absoluto de la velocidad del jugador 1 x es menor a la distancia
                # entre tiempo x aceleracion libre
                self.acceleration = -copysign(self.desaceleracion_libre,
                                                  self.velocidad.x)  # que la aceleracion sea la inversion
                # de los valores de velocidad.x y la de romper desaceleracion, negativa
            else:  # sino
                if dt != 0:  # si la distancia de la distancia entre tiempo es diferente a 0
                    self.aceleracion = -self.velocidad.x / dt  # que la aceleracion de del jugador en x sea la velocidad
                    # en x entre dt
        self.aceleracion = max(-self.maxima_aceleracion,min(self.aceleracion, self.maxima_aceleracion))  # que la aceleracion sea
        # el maximo de entre aceleracion y el minimo entre la aceleracion y maxima aceleracion

        if pressed[pygame.K_RIGHT]:  # si se presiona flecha derecha
            self.rotacion -= 30 * dt  # que la rotacion del jugador se le reste 30 grados x dt
        elif pressed[pygame.K_LEFT]:  # si se presiona flecha izquierda
            self.rotacion += 30 * dt  # que la rotacion del jugador se le sume 30 grados x dt
        else:  # sino
            self.rotacion = 0  # qque la rotacion sea 0
        self.rotacion = max(-self.maxima_rotacion,
                                min(self.rotacion, self.maxima_rotacion))  # que la rotacion sea el maximo entre el
        # minimo de la rotaciony maxima rotacion, y el maximo del negativo de l maxima rotacion
        self.update() # actualiza el jugador1
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


def leerPos(str): # define el metodo getPos qie recibe como parametros str
    str= str.split(",") #define la variable str conteniendo str.split que recibira las coordernadas de los jugadores
    return int(str[0]), int(str[1])
def hacerPos(tup):
    return str(tup[0])+","+str(tup[1])
# clase juego
class Juego:# se define la clase juego
    def __init__(self):# el constructor no posee parametros
        pygame.init()# se inicia la funcion de iniciar el juego de pygame

        pygame.display.set_caption("Death Dakar") # da nombre a la ventana de juego
        ANCHO = 1080 # ancho de la pantalla
        ALTURA = 720# alto de la pantalla
        self.reloj = pygame.time.get_ticks() // 1000# se define un temporizador en la variable que se divido por 1000 para su obtencion en segundos
        self.screen = pygame.display.set_mode((ANCHO, ALTURA)) # dibuja la pantalla
        self.clock = pygame.time.Clock()# se define el reloj del juego
        self.ticks = 60# se define los fps por segundo
        self.exit = False# si para salir es falso
        self.fondo = pygame.image.load("imagenes/Fondo de carrera.png")#carga el el background del juego


    def correr(self):# define el metodo de correr el cual se encarga de darle funcionalidad al programa
        n = Network()  # instancia la clase network
        startPos = leerPos(n.getposicion())#obtiene la posicion de los jugadores
        jugador1 = Jugador1(startPos[0],startPos[1])#---
        jugador2= Jugador1(0,0) #instancia el jugador 2
        enemigo1 = Dummies1()                       #  |
        enemigo2 = Dummies2()                       #  | se instancias los objetos de las diferentes clases
        enemigo3 = Dummies3()                       #  |
        linea_salida = Meta()                       #  |
        arboles=Arbol()                             #  |
        minas=Mina()                                #---



        y=0 # se define la variable y
        # pygmae.time.settimer(userevent+1,180000
        while not self.exit:# mientras no se use self.exit
            dt = self.clock.get_time() / 1000 # la distancia entre tiempo sera de los microsengundos divididos entre mil para definir el tiempo de movimiento
            dt2 = self.clock.get_time() / 1000# la distancia entre tiempo sera de los microsengundos divididos entre mil para definir el tiemp en movimiento
            # if pygame.event.get(userevent+1)
            posicionjugador2=leerPos((n.send(hacerPos(jugador1.x,jugador1.y))))# define posiciones del jugador2
            jugador2.x=posicionjugador2[0] # define la posicion en las coordenadas x
            jugador2.y= posicionjugador2[1]# define la posicion en las coordenadas y
            jugador2.update()
            # cola del evento
            for event in pygame.event.get():# mientras se obtengas los eventos en pygame
                if event.type == pygame.QUIT:# y si se presiona el quit o salir
                    self.exit = True # que la variable self.salida sea
            jugador1.move()
            texto = pygame.font.SysFont("Arial", 20, True,False)  # asigna a a la variable texto_puntos el tipo de letra, tamano y si esta en negrita
            informacion = texto.render("cronometro  ", 0, (0, 0, 0))  # almacena el tiempo
            # y lo actualiza conforme pasa el juego y define su color el cual es negro
            texto_puntos = pygame.font.SysFont('Arial', 20,True)  # asigna a a la variable texto_puntos el tipo de letra, tamano y si esta en negrita
            puntuacion = texto_puntos.render("puntaje:   " + str(jugador1.puntaje), 1,(0, 0, 0))  # almacena el puntaje del jugador1
            # y lo actualiza conforme pasa el juego y su color el cual es negro
            # grupo donde estan los objetos a colisionar teniendo como entrada los dummies y la meta, asi mismo otorga puntos al jugador que lo haga
            # crea un grupo de sprites
            sprites = pygame.sprite.Group()
            sprites.add(enemigo1)  # añade enemigo1 al grupo sprites
            sprites.add(enemigo2)  # añade enemigo2 al grupo sprites
            sprites.add(enemigo3)  # añade enemigo3 al grupo sprites

            # crea un grupo de balas
            balas = pygame.sprite.Group()

            # crea un grupo de obstaculos
            obstaculos = pygame.sprite.Group()
            obstaculos.add(arboles)  # añade arboles al grupo de obstaculos
            obstaculos.add(minas)  # añade minas al grupo de obstaculos

            colision = pygame.sprite.spritecollide(jugador1, sprites,True)  # permite la colision de sprites del jugador2 con el grupo obstaculos, y permite desaparecer al ser destruido
            if colision:  # si sucede colision
                explosion = pygame.mixer.Sound("sonido/explosion.mp3")  # instancia la funcion y importa la musica
                explosion.play()  # reproduce el audio contenido en la funcion
                jugador1.puntaje += 200  # suma 200 puntos al colisionar el jugador con algun objeto del grupo sprite

            collision = pygame.sprite.spritecollide(jugador1, obstaculos,False)  # permite la colision de sprites del jugador2 con el grupo obstaculos, y permite desaparecer al ser destruido
            if collision:  # si sucede collision
                explosion = pygame.mixer.Sound("sonido/explosion.mp3")  # instancia la funcion y importa la musica
                explosion.play()  # reproduce el audio contenido en la funcion
                jugador1.kill()  # destruye el jugador2

            y_relativa = y % self.fondo.get_rect().height  # se agrega una variable para que el fondo no sea estatico
            self.screen.blit(self.fondo, (0, y_relativa - self.fondo.get_rect().height))  # imprime en la ventana la imagen de fondo que se usara para el juego
            if y_relativa < 1100:  # mantiene la imagen de fondo en constante actualizacion
               self.screen.blit(self.fondo,(0, y_relativa))  # imprime la imagen de fondo contantemente para que no se vea borroso
            y += 7  # da una velocidad a la pista
            self.screen.blit(linea_salida.imagen,(linea_salida.rect.x, linea_salida.rect.y))  # imprime en la venana la linea de salida
            # logica de la actualizacion

            sprites.update()  # actualiza el grupo de sprites
            obstaculos.update()  # actualiza el grupo de obstaculos
            balas.update()  # actualiza el grupo de balas
            linea_salida.update()  # actualiza la linea de salida

            rotado = pygame.transform.rotate(jugador1.imagen, jugador1.angulo)  # imprimte la rotacion segun el angulo del jugador 1
            rect = rotado.get_rect()
            self.screen.blit(rotado, jugador1.posicion)  # imprime la rotacioin del jugador 1 en la poscion que se encuentre

            self.screen.blit(puntuacion, (16, 30))  # imprime la puntacion jugador1
            self.screen.blit(informacion, (5, 5))  # imprime  imprime la informacion contenida en informacion

            Cronometraje = pygame.time.get_ticks() // 1000  # define el cronometro del juego en segundos
            self.clock.tick(self.ticks)  # define el reloj del juego
            cronometraje = str(Cronometraje)  # convierte el valor cronometraje en texto
            cronometro = texto.render(cronometraje, 100, (0, 0, 0))  # variabelq que contiene el texto de la variable cronometro
            self.screen.blit(cronometro, (110, 5))  # imprime el cronometro en la pantalla
            # dummies.draw(self.screen)
            sprites.draw(self.screen)  # imprime todo lo integrado en el grupo sprites en la pantalla
            balas.draw(self.screen)  # imprime todo lo integrado en el grupo balas en la pantalla
            obstaculos.draw(self.screen)  # imprime todo lo integrado en el grupo obstaculos en la pantalla
            # actualiza pantalla
            pygame.display.update()  # actualiza la pantalla con la funcion de pygame
            pygame.display.flip()  # actualiza la pantalla
            # salir del juego


pygame.quit()  # funcion que permite quitar el juego

if __name__ == "__main__":  # define la iniciacion del juego
    juego = Juego()  # itera la funcion Juego() en juego
    juego.correr()  # llama la funcion correr del juego