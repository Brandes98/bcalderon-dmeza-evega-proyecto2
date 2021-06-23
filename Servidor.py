import socket  # Importa la libreria sockets

from _thread import *  #importa la libreria  _thread

import sys  #importa la libreria sys
servidorLocal = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #
servidor = "192.168.100.167"  # le asigna a la variable servidor una cadena de caracteres conteniendo la direccioxcn ipv4 del computador que sera servidor
puerto = 6942  # le asigna a la variable puerto un entero (55531)socket.socket recibe como parametros el socket.AF.NET
   # donde este lo que que hace es decir el tipo de red y socket.SOCK_STREAM la forma en que va a recibir el lo que se le
   #asigne a la variable server.
try:  # intente denuevo el uso de la conexion brindada en el puerto asi como el en la variable server
    servidorLocal.bind((servidor,puerto))  #recibe como parametro los datos brindados en servidor y los brindados en la variable puerto
except socket.error as FuenteError:  # en caso de error
    str(FuenteError)  #convierta en string la fuente de error en caso de que esta este dando un error en el programa

servidorLocal.listen(2)  # defino las cantidades de conexiones disponibles en cola por lo tanto,
                        # la cantidad de jugadores a los cuales les permito conectarse al server.
print("esperando una conexion,  por favor espere, inicializando servidor")  # imprime el mensaje dado en el print

def threaded_client(conn):  #funcion encargada de lo hilos del servidor y cliente,
    # recibe como parametro la conex
    conn.send(str.encode("Conectado"))  # envia que la conexion se ha logrado en un dato codificado en una string
    reply = ""  # variable reply, sele asigna como dato una cadena vacia
    while True: #mientras sea verdad o se cumpla el proceso
        try: #intente el siguiente proceso
            data = conn.recv(2048)  # que la conexion que reciba sea 2048 bits por segundo
            reply = data.encode("utf-8")   # y que decodifique la conexion para la lectura de la red a este programa en el formato utf-8
            if not data: # si no recibe datos del cliente
                print("desconectado") # imprima desconectado
                break # rompa el ciclo

            else:# en caso contrario
                print("recibido : ",reply)# imprima recibido y los datos almacenados decodificados
                print("enviando : ",reply)# imprime enviando junto a los datos decodificados
            conn.sendall(str.encode(reply)) # envia los datos codificados en bytes al lado del cliente
        except:# en caso contrario
             break # romper el ciclo para no hacr un loop infinito
    print("conexion perdida")# imprime conexion perdida
    conn.close()# cierra la conexion en caso contrario permite reabrirla


while True:  # mientras se cumpla todos los parametros anteriores, busque continuamente conexiones
    conn, address = servidorLocal.accept()  # acepta las peticiones conexion y
    # la direccion correspondiente, lo cual nos devuelve la conexion y la address o direccion.
    print("conectado a : ", address)  #imprime conectado a la direccion que reconozca o que posea la variable address.
    start_new_thread(threaded_client,(conn,))# abre un hilo que permite controlar
    # las acciones enviadas y recibidas del cliente






