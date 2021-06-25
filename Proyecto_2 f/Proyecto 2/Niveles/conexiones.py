import socket
class Network: #defino la clase conexiones
    def __init__(self) : # defino el constructor de la clase sin parametros
        self.cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # se define la variable self.cliente. la cual poseera el tipo de red y la forma en que recibir los datos del self.server
        self.servidor = "192.168.100.25"  # define la red o donde iniciara el servidor
        self.puerto = 49887  # puerto de conexion
        self.address  = (self.servidor,self.puerto)# la variable de self.direccion recibe como parametros el self.server y self.puerto donde se toma como la direccion del programa
        self.id = self.conexion() #pasa el metodo conexion como una variable propia de conexiones definida en# en el self.id
        print(self.id)  # solo tiene la funcion de ver si se conecta
    def conexion(self):  #define la variable conexion
        try:  # intente
            self.cliente.connect(self.address) #que a la variable cliente con el metodo connect le pasa como parametro la variable direccion
            return self.cliente.recv(2048).decode()  # devuelve la variable cliente recibiendo 2048 bits por segundo y lo decodifica para la lectura de los datos
        except:# en caso de exepcion
            pass #pase
    def enviar(self,data):
        try:
            self.cliente.send(str.encode(data))
            return self.cliente.recv(2048).decode()
        except socket.error as error:
            print(error)
n = Network()
print(n.enviar("hello"))
print(n.enviar("working"))
