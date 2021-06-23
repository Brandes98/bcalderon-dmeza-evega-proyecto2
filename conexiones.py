import socket
class Network: #defino la clase conexiones
    def __init__(self) : # defino el constructor de la clase sin parametros
        self.cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # se define la variable self.cliente. la cual poseera el tipo de red y la forma en que recibir los datos del self.server
        self.servidor = "192.168.100.167"  # define la red o donde iniciara el servidor
        self.puerto = 6942  # puerto de conexion
        self.address  = (self.servidor,self.puerto)# la variable de self.direccion recibe como parametros el self.server y self.puerto donde se toma como la direccion del programa
        self.posicion = self.conexion() #pasa el metodo conexion como una variable propia de conexiones definida en# en el self.id
        print(self.posicion)
    def getposicion(self):
        return self.posicion
    def conexion(self):  #define la variable conexion
        try:  # intente
            self.cliente.connect(self.address) #que a la variable cliente con el metodo connect le pasa como parametro la variable direccion
            return self.cliente.recv(2048).decode()  # devuelve la variable cliente recibiendo 2048 bits por segundo y lo decodifica para la lectura de los datos
        except:# en caso de exepcion
            pass #pase
    def enviar(self,dato):# defino la variabel enviar la ual recibe datos de la variable dato
        try: # intente
            self.cliente.send(str.encode(dato))# enviar de la variable cliente los datos en modo de str codificados
            return self.cliente.recv(2048).decode() #retorna los valores del cliente en 2048 byts de informacion y los decodifica
        except socket.error as error:# si encuentra un error
            print(error)# imprimalo
n=Network()
print(n.enviar("hola"))
print(n.enviar("hola"))