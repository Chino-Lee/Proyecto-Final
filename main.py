import utils
from time import sleep 
# Yonghan Lee
# 20210579
# Proyecto Final

def main():

    NAME = "Yonghan Lee "
    print("------- Empezando tic-tac-toe bot -------")

    x = utils.is_x()

    while not x:
        print("------- Abriendo registro -------")
        sleep(3)
        x = utils.is_x()

    y = utils.register_user(NAME)
    print("Registrado como : {}, ID de jugador es: {}".format(NAME, y))
    sleep(2)

    z = utils.does_z()

    while z:

        a = utils.is_a(y)
        
        while not a:
            print("Esperando por su turno...")
            sleep(3)
            a = utils.is_a(y)

        board = utils.read_board()
        utils.print_board(board)

        legal = False

        while not legal:

            print("Jugando turno...")
            q = utils.q(board, y)
            legal = utils.validate_move(board, q)

        print("Puesto en linea: {} , columna: {}".format(q[0], q[1]))

        utils.send_move(y, q)

        sleep(3)
        z = utils.does_game_continue()

    print("FIN DE JUEGO, Revisar API para ver si gano.")

if __name__ == "--- main ---'":
    main()