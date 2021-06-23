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
        self.vida=1000
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
            cactus=Cactus()
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
            if pressed[pygame.K_w]:
                jugador2.arranque.play()
                if jugador2.velocidad.x < 0:
                    jugador2.aceleracion = jugador2.romper_desaceleracion
                jugador2.aceleracion += 1 * dt2
            elif pressed[pygame.K_s]:
                if jugador2.velocidad.x > 0:
                    jugador2.aceleracion = -jugador2.romper_desaceleracion
                else:
                    jugador2.aceleracion -= 1 * dt2
            elif pressed[pygame.K_f]:
                if abs(jugador2.velocidad.x) > dt2 * jugador2.romper_desaceleracion:
                    jugador2.aceleracion = -copysign(jugador2.romper_desaceleracion, jugador2.velocidad.x)
                else:
                    jugador2.aceleracion = -jugador2.velocidad.x / dt2
            else:
                if abs(jugador2.velocidad.x) > dt2 * jugador2.desaceleracion_libre:
                    jugador2.aceleracion = -copysign(jugador2.desaceleracion_libre, jugador2.velocidad.x)
                else:
                    if dt2 != 0:
                        jugador2.aceleracion = -jugador2.velocidad.x / dt2
            jugador2.aceleracion = max(-jugador2.maxima_aceleracion,
                                       min(jugador2.aceleracion, jugador2.maxima_aceleracion))

            if pressed[pygame.K_d]:
                jugador2.rotacion -= 30 * dt2
            elif pressed[pygame.K_a]:
                jugador2.rotacion += 30 * dt2
            else:
                jugador2.rotacion = 0
            jugador2.rotacion = max(-jugador2.maxima_rotacion, min(jugador2.rotacion, jugador2.maxima_rotacion))

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
            for catus in range(12):
                cactus.rect.x= random.randrange(ALTURA)
                cactus.rect.y = random.randrange(ANCHO)

            objetos = pygame.sprite.Group()
            objetos.add(Meta)
            carros=pygame.sprite.group()
            carros.add(jugador1)
            carros.add(jugador2)
            choque = pygame.sprite.spritecollide(cactus, carros, True)
            if jugador1.vida==0:
                jugador1.destroy()
            if choque:
                explosion=pygame.mxer.sound("sonido/explosion.mp3")
                explosion.play()
                jugador1.vida-=1000
            collision = pygame.sprite.spritecollide(jugador1, objetos, False)
            if collision:
                metasound = pygame.mixer.Sound("sonido/meta.mp3")
                metasound.play()
                jugador1.puntaje += 200
            collision = pygame.sprite.spritecollide(jugador2, objetos, False)
            if collision:
                metasound = pygame.mixer.Sound("sonido/meta.mp3")
                metasound.play()
                jugador2.puntaje += 200
            # logica de actualizacion
            jugador1.update(dt)
            jugador2.update(dt2)
            self.screen.blit(self.pista1, (0, 0))
            self.screen.blit(self.pista1D, (0, 0))
            rotado = pygame.transform.rotate(jugador1.imagen, jugador1.angulo)
            rect = rotado.get_rect()
            self.screen.blit(rotado, jugador1.posicion)

            rotado = pygame.transform.rotate(jugador2.image, jugador2.angulo)
            rect = rotado.get_rect()
            self.screen.blit(rotado, jugador2.posicion)

            self.screen.blit(puntuacion2, (16, 50))
            self.screen.blit(puntuacion, (16, 30))
            self.screen.blit(informacion, (5, 5))

            Cronometraje = pygame.time.get_ticks() // 1000
            self.clock.tick(self.ticks)
            cronometraje = str(Cronometraje)
            cronometro = texto.render(cronometraje, 100, (0, 0, 0))
            self.screen.blit(cronometro, (110, 5))
            dummies.draw(self.screen)
            objetos.draw(self.screen)


            # actualiza la pantalla a  la cantidad de fps que se le asigno a la variable self.ticks
            pygame.display.flip()

            self.clock.tick(self.ticks)
if __name__=__main__:
    juego=Juego()
    