import time
import socket
import pickle

# HOST = "127.0.0.1"  The server's hostname or IP address
PORT = 65432  # The port used by the server
buffer_size = 1024

def mostrartablero3(tablero):

    print(" {} | {} | {} " .format(tablero[0],tablero[1],tablero[2]))
    print("----+----+----")
    print(" {} | {} | {} " .format(tablero[3],tablero[4],tablero[5]))
    print("----+----+----")
    print(" {} | {} | {} " .format(tablero[6],tablero[7],tablero[8]))

def mostrartablero5(tablero5):

    print(" {} | {} | {} | {} | {}" .format(tablero5[0],tablero5[1],tablero5[2],tablero5[3],tablero5[4]))
    print("----+----+----+----+----")
    print(" {} | {} | {} | {} | {}" .format(tablero5[5],tablero5[6],tablero5[7],tablero5[8],tablero5[9]))
    print("----+----+----+----+----")
    print(" {} | {} | {} | {} | {}" .format(tablero5[10],tablero5[11],tablero5[12],tablero5[13],tablero5[14]))
    print("----+----+----+----+----")
    print(" {} | {} | {} | {} | {}" .format(tablero5[15],tablero5[16],tablero5[17],tablero5[18],tablero5[19]))
    print("----+----+----+----+----")
    print(" {} | {} | {} | {} | {}" .format(tablero5[20],tablero5[21],tablero5[22],tablero5[23],tablero5[24]))

def mov_jugador(tablero):

    casillas = ["1","2","3","4","5","6","7","8","9"]
    posicion = None
    while True:
        if posicion not in casillas:
            posicion = input("Elige del 1-9  ")
        else:
            posicion = int(posicion)
            return posicion - 1



host = input("Ingrese la direccion IP del servidor:  ")
puerto = int(input("Ingrese el puerto que recibira solicitudes de conexion:  "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((host, puerto))

    opcion = ""
    while opcion != "Principiante" and opcion != "Avanzado":
        opcion = input("Elige la dificultad: Principiante / Avanzado  ")

    opcion = opcion.encode()

    marca_jugador = ""
    while marca_jugador != "X" and marca_jugador != "O":
        marca_jugador = input("Elige la marca: X/O  ")

    marca_jugador = marca_jugador.encode()

    TCPClientSocket.sendall(opcion)
    TCPClientSocket.sendall(marca_jugador)

    print("Esperando una respuesta...")

    data = TCPClientSocket.recv((buffer_size))
    #tablero = pickle.loads(data)
    mostrartablero3(data)

    # mostrartablero5()


