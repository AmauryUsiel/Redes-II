import time
import socket
import random
import pickle
import string
#---------------------------------------VARIABLES--------------------------------------------------------------------

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
buffer_size = 1024
tablero = [" "]*9
cadena = " "
tablero5 = [" "]*25
cadena5 = " "

#---------------------------------------FUNCIONES----------------------------------------------------------------------

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

def hayganador3(tablero, jugador):
    if tablero[0] == tablero[1] == tablero[2] == jugador or \
       tablero[3] == tablero[4] == tablero[5] == jugador or \
       tablero[6] == tablero[7] == tablero[8] == jugador or \
       tablero[0] == tablero[3] == tablero[6] == jugador or \
       tablero[1] == tablero[4] == tablero[7] == jugador or \
       tablero[2] == tablero[5] == tablero[8] == jugador :
        return True
    else:
        return False

def hayganador5(tablero5,jugador):
    if tablero5[0] == tablero5[1] == tablero5[2] == tablero5[3] == tablero5[4] == jugador or \
       tablero5[5] ==  tablero5[6] == tablero5[7] == tablero5[8] == tablero5[9] == jugador or \
        tablero5[10] == tablero5[11] == tablero5[12] == tablero5[13] == tablero5[14] == jugador or \
        tablero5[15] == tablero5[16] == tablero5[17] == tablero5[18] == tablero5[19] == jugador or \
        tablero5[20] == tablero5[21] == tablero5[22] == tablero5[23] == tablero5[24] == jugador or \
        tablero5[0] == tablero5[5] == tablero5[10] == tablero5[15] == tablero5[20] == jugador or \
        tablero5[1] == tablero5[6] == tablero5[11] == tablero5[16] == tablero5[21] == jugador or \
        tablero5[2] == tablero5[7] == tablero5[12] == tablero5[17] == tablero5[22] == jugador or \
        tablero5[3] == tablero5[8] == tablero5[13] == tablero5[18] == tablero5[23] == jugador or \
        tablero5[4] == tablero5[9] == tablero5[14] == tablero5[19] == tablero5[24] == jugador:
            return True
    else:
        return False

def tablero_lleno(tablero):

    for i in tablero:
        if i == " ":
            return False
        else:
            return True

def tablero_lleno5(tablero5):

    for i in tablero5:
        if i == " ":
            return False
        else:
            return True

def casilla_libre(tablero,casilla):

    return tablero[casilla] == " "

def casilla_libre5(tablero5,casilla):

    return  tablero5[casilla] == " "

def mov_maquina(tablero,jugador):
    if tablero[0] == tablero[1] == jugador and tablero[2] == " ":
        casilla = 2
    elif tablero[0] == tablero[2] == jugador and tablero[1] == " ":
        casilla = 1
    elif tablero[1] == tablero[2] == jugador and tablero[0] == " ":
        casilla = 0

    elif tablero[3] == tablero[4] == jugador and tablero[5] == " ":
        casilla = 5
    elif tablero[3] == tablero[5] == jugador and tablero[4] == " ":
        casilla = 4
    elif tablero[4] == tablero[5] == jugador and tablero[3] == " ":
        casilla = 3

    elif tablero[6] == tablero[7] == jugador and tablero[8] == " ":
        casilla = 8
    elif tablero[6] == tablero[8] == jugador and tablero[7] == " ":
        casilla = 7
    elif tablero[7] == tablero[8] == jugador and tablero[6] == " ":
        casilla = 6

    elif tablero[0] == tablero[3] == jugador and tablero[6] == " ":
        casilla = 6
    elif tablero[0] == tablero[6] == jugador and tablero[3] == " ":
        casilla = 3
    elif tablero[3] == tablero[6] == jugador and tablero[0] == " ":
        casilla = 0

    elif tablero[1] == tablero[4] == jugador and tablero[7] == " ":
        casilla = 7
    elif tablero[1] == tablero[7] == jugador and tablero[4] == " ":
        casilla = 4
    elif tablero[4] == tablero[7] == jugador and tablero[1] == " ":
        casilla = 1

    elif tablero[2] == tablero[5] == jugador and tablero[8] == " ":
        casilla = 8
    elif tablero[2] == tablero[8] == jugador and tablero[5] == " ":
        casilla = 5
    elif tablero[5] == tablero[8] == jugador and tablero[2] == " ":
        casilla = 2

    else:
        while True:
            casilla = random.randint(0,8)
            if tablero[casilla] == " ":
                break

    return casilla
# ---------------------------------------------------------------SOCKETS-----------------------------------------------
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()

    print("Elige la dificultad del Gato Dummy")

    Client_conn, Client_addr = TCPServerSocket.accept()
    with Client_conn:
        print("Conectado a", Client_addr)
        dificultad = Client_conn.recv(buffer_size)

        cadena_dificultad = dificultad.decode()

        if(cadena_dificultad == "Principiante"):
            Client_conn.sendall(b"Principiante elegido")
            cadena = pickle.dumps(tablero)
            Client_conn.send(cadena)


        elif(cadena_dificultad == "Avanzado"):
            Client_conn.sendall(b"Avanzado elegido")
            cadena5 = pickle.dumps(tablero5)
            Client_conn.send(cadena5)


        marca_jugador = Client_conn.recv(buffer_size).decode()

        if(marca_jugador == "X"):
            Client_conn.sendall(b" Primer Tiro: X ")
            marca_maquina="O"
        else:
            Client_conn.sendall(b" Segundo Tiro: O")
            marca_maquina="X"


