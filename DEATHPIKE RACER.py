import pygame
import random
from math import tan, radians, degrees, copysign
from pygame.math import Vector2
class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load()
        self.rect=self.image.get_rect()

class minas(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load()
        self.rect=self.image.get_rect()
class meta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x=500
        self.y=145
        self.image= pygame.image.load("imagenes/MetaPista1.png")
        self.rect= self.image.get_rect()
        self.rect.center=(self.x,self.y)
 #clase jugador 1
class Jugador1(pygame.sprite.Sprite):
    def __init__(self, x=220, y=150, angulo=0.0, largoVehiculo=3, maxima_rotacion=30, maxima_aceleracion=200.0):
        super().__init__()
        self.imagen = pygame.image.load("imagenes/RedCar.png")
        self.rect = self.imagen.get_rect()
        self.rect.center = (x, y)
        self.posicion = Vector2(x, y)
        self.velocidad = Vector2(0.0, 0.0)
        self.angulo = angulo
        self.largoVehiculo = largoVehiculo
        self.maxima_aceleracion = maxima_aceleracion
        self.maxima_rotacion = maxima_rotacion
        self.maxima_velocidad= 200
        self.romper_desaceleracion = 200
        self.desaceleracion_libre = 2
        self.arranque = pygame.mixer.Sound("sonido/acelerar.mp3")
        self.frenado = pygame.mixer.Sound("sonido/frenando.mp3")
        self.puntaje=0
        self.aceleracion = 100.0
        self.rotacion = 0.0
    def Update(self, dt):
        self.velocidad+= (self.aceleracion * dt, 0)
        self.velocidad.x = max(-self.maxima_velocidad, min(self.velocidad.x, self.maxima_velocidad))
        self.rect.x = self.posicion.x
        self.rect.y = self.posicion.y
        if self.rotacion:
            radio_rotacion = self.largoVehiculo / tan(radians(self.rotacion))
            velocidad_angular = self.velocidad.x / radio_rotacion
        else:
            velocidad_angular = 0

        self.posicion += self.velocidad.rotate(-self.angulo) * dt
        self.angulo += degrees(velocidad_angular) * dt
class Juego:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("death race")
        ANCHO= 1280
        ALTURA = 720
        self.reloj= pygame.time.get_ticks()//1000
        self.screen = pygame.display.set_mode((ANCHO,ALTURA))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False
        self.pista1=pygame.image.load("imagenes/pista1.PNG")
        self.pista1D = pygame.image.load("imagenes/pista1borders.png")
        self.pista2= pygame.image.load("imagenes/pista2.png")
        self.pista2D = pygame.image.load("imagenes/pista2borders.png")
        def level1(self):
            jugador1 = Jugador1()
            Meta=meta()
            Minas=minas()
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_UP]:
                jugador1.arranque.play()
                if jugador1.velocidad.x < 0:
                    jugador1.aceleracion = jugador1.romper_desaceleracion
                jugador1.aceleracion += 1 * dt
            elif pressed[pygame.K_DOWN]:
                if jugador1.velocidad.x > 0:
                    jugador1.aceleracion = -jugador1.romper_desaceleracion
                else:
                    jugador1.aceleracion -= 1 * dt
            elif pressed[pygame.K_SPACE]:
                jugador1.frenado.play()
                if abs(jugador1.velocidad.x) > dt * jugador1.romper_desaceleracion:
                    jugador1.aceleracion = -copysign(jugador1.romper_desaceleracion, jugador1.velocidad.x)
                else:
                    jugador1.aceleracion = -jugador1.velocidad.x / dt
            else:
                if abs(jugador1.velocidad.x) > dt * jugador1.desaceleracion_libre:
                    jugador1.acceleration = -copysign(jugador1.desaceleracion_libre, jugador1.velocidad.x)
                else:
                    if dt != 0:
                        jugador1.aceleracion = -jugador1.velocidad.x / dt
            jugador1.aceleracion = max(-jugador1.maxima_aceleracion,
                                       min(jugador1.aceleracion, jugador1.maxima_aceleracion))

            if pressed[pygame.K_RIGHT]:
                jugador1.rotacion -= 30 * dt
            elif pressed[pygame.K_LEFT]:
                jugador1.rotacion += 30 * dt
            else:
                jugador1.rotacion = 0
            jugador1.rotacion = max(-jugador1.maxima_rotacion, min(jugador1.rotacion, jugador1.maxima_rotacion))

            texto = pygame.font.SysFont("Arial", 20, True, False)
            informacion = texto.render("cronometro", 0, (0, 0, 0))
            texto_puntos = pygame.font.SysFont('Arial', 20, True)
            puntuacion = texto_puntos.render("puntaje: " + str(jugador1.puntaje), 1, (0, 0, 0))
            Cronometraje = pygame.time.get_ticks() // 1000
            self.clock.tick(self.ticks)
            cronometraje = str(Cronometraje)
            cronometro = texto.render(cronometraje, 100, (0, 0, 0))
            texto_pausa = pygame.font.SysFont('Fixedsys', 40, True)
            infopausa = texto_pausa.render("Presione (P) para pausar", 21, True)

            for minados in range(12):
                Minas.rect.x= random.randrange(ALTURA)
                Minas.rect.y = random.randrange(ANCHO)
            objetos = pygame.sprite.Group()
            objetos.add(Meta)
            objetos.add(Minas)
            collision = pygame.sprite.spritecollide(jugador1, objetos, False)
            if collision:
                metasound = pygame.mixer.Sound("sonido/meta.mp3")
                metasound.play()
                jugador1.puntaje += 200

            # logica de actualizacion
            jugador1.update(dt)
            self.screen.blit(self.pista1, (0, 0))
            self.screen.blit(self.pista1D, (0, 0))
            rotated = pygame.transform.rotate(jugador1.image, jugador1.angle)
            rect = rotated.get_rect()
            self.screen.blit(rotated, jugador1.position)
            objetos.draw(self.screen)
            self.screen.blit(puntuacion, (16, 30))
            self.screen.blit(informacion, (5, 5))
            self.screen.blit(infopausa, (850, 15))
            self.screen.blit(cronometro, (110, 3))


            # actualiza la pantalla a  la cantidad de fps que se le asigno a la variable self.ticks
            pygame.display.flip()

            self.clock.tick(self.ticks)