from ctypes.wintypes import HACCEL
from errno import EFAULT
from random import randint
from re import A, X
from tkinter import E
import requests
from urllib.parse import unquote


API_URL = "http://127.0.0.1:8000"


def is_registry_open() -> bool:
    """
    Checks if registry is available via API.
    """
    try:
        url = "{}/registry".format(API_URL)
        res = requests.get(url)

        if res.text == "true":
            return True
        elif res.text == "false":
            return False

    except:
        return False


def register_user(name: str) -> str:
    """
    Registers user in API game.
    """
    url = "{}/register_player/{}".format(API_URL, name)
    res = requests.post(url)
    player_id = res.text[1]
    return player_id


def is_my_turn(player_id: str) -> bool: 
    """
    Checks if it is our turn via API.
    """
    url = "{}/turn/{}".format(API_URL, player_id)
    res = requests.get(url)
    
    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def read_board() -> list:
    """
    Gets game board via API.
    """
    url = "{}/board".format(API_URL)
    res = requests.get(url)
    board_str = res.text
    board = [
        [board_str[1], board_str[2], board_str[3]], 
        [board_str[4], board_str[5], board_str[6]], 
        [board_str[7], board_str[8], board_str[9]]
    ]

    return board


def decide_move(board: list, player_id: str) -> list[int, int]:
    """
    Decides next move to make. 
    """
    rival_id = "X"
    if player_id == "X":
        rival_id = "O"



    A = board[0][0]
    B = board[0][1]
    C = board[0][2]
    D = board[1][0]
    E = board[1][1]
    F = board[1][2]
    G = board[2][0]
    H = board[2][1]
    I = board[2][2]







    if A == rival_id and B == rival_id and C == "-":
        row = 0
        column = 2
        return [row, column]
    elif D == rival_id and E == rival_id and F == "-":
        row = 1
        column = 2
        return [row, column]
    elif G == rival_id and H == rival_id and I == "-":
        row = 2
        column = 2
        return [row, column]
    elif A == rival_id and C == rival_id and B == "-":
        row = 0
        column = 1
        return [row, column]
    elif D == rival_id and F == rival_id and E == "-":
        row = 1
        column = 1
        return [row, column]
    elif G == rival_id and I == rival_id and H == "-":
        row = 2
        column = 1
        return [row, column]
    elif B == rival_id and C == rival_id and A == "-":
        row = 0
        column = 0
        return [row, column]
    elif E  == rival_id and F == rival_id and D == "-":
        row = 1
        column = 0
        return [row, column]
    elif H == rival_id and I == rival_id and G == "-":
        row = 2
        column = 0
        return [row, column]


    if A == rival_id and D == rival_id and G == "-":
        row = 2
        column = 0
        return [row, column]
    elif B == rival_id and E == rival_id and H == "-":
        row = 2
        column = 1
        return [row, column]
    elif C == rival_id and F == rival_id and I == "-":
        row = 2
        column = 2
        return [row, column]
    if A == rival_id and G == rival_id and D == "-":
        row = 1
        column = 0
        return [row, column]
    elif B == rival_id and H == rival_id and E == "-":
        row = 1
        column = 1
        return [row, column]
    elif C == rival_id and I == rival_id and F == "-":
        row = 1
        column = 2
        return [row, column]
    if D == rival_id and G == rival_id and A == "-":
        row = 0
        column = 0
        return [row, column]
    elif E == rival_id and H == rival_id and B == "-":
        row = 0
        column = 1
        return [row, column]
    elif F == rival_id and I == rival_id and C == "-":
        row = 0
        column = 2
        return [row, column]


    if E == rival_id and I == rival_id and A == "-":
        row = 0
        column = 0
        return [row, column]
    elif A == rival_id and I == rival_id and E == "-":
        row = 1
        column = 1
        return [row, column]
    elif A == rival_id and E == rival_id and I == "-":
        row = 2
        column = 2
        return [row, column]

    if E == rival_id and G == rival_id and C == "-":
        row = 0
        column = 2
        return [row, column]
    elif C == rival_id and G == rival_id and E == "-":
        row = 1
        column = 1
        return [row, column]
    elif C == rival_id and E == rival_id and G == "-":
        row = 2
        column = 0
        return [row, column]




    else: 
        if A == player_id and B == player_id and C == "-":
            row = 0
            column = 2
            return [row, column]
        elif D == player_id and E == player_id and F == "-":
            row = 1
            column = 2
            return [row, column]
        elif G == player_id and H == player_id and I == "-":
            row = 2
            column = 2
            return [row, column]
        elif A == player_id and C == player_id and B == "-":
            row = 0
            column = 1
            return [row, column]
        elif D == player_id and F == player_id and E == "-":
            row = 1
            column = 1
            return [row, column]
        elif G == player_id and I == player_id and H == "-":
            row = 2
            column = 1
            return [row, column]
        elif B == player_id and C == player_id and A == "-":
            row = 0
            column = 0
            return [row, column]
        elif E  == player_id and F == player_id and D == "-":
            row = 1
            column = 0
            return [row, column]
        elif H == player_id and I == player_id and G == "-":
            row = 2
            column = 0
            return [row, column]


        if A == player_id and D == player_id and G == "-":
            row = 2
            column = 0
            return [row, column]
        elif B == player_id and E == player_id and H == "-":
            row = 2
            column = 1
            return [row, column]
        elif C == player_id and F == player_id and I == "-":
            row = 2
            column = 2
            return [row, column]
        if A == player_id and G == player_id and D == "-":
            row = 1
            column = 0
            return [row, column]
        elif B == player_id and H == player_id and E == "-":
            row = 1
            column = 1
            return [row, column]
        elif C == player_id and I == player_id and F == "-":
            row = 1
            column = 2
            return [row, column]
        if D == player_id and G == player_id and A == "-":
            row = 0
            column = 0
            return [row, column]
        elif E == player_id and H == player_id and B == "-":
            row = 0
            column = 1
            return [row, column]
        elif F == player_id and I == player_id and C == "-":
            row = 0
            column = 2
            return [row, column]

        if E == player_id and I == player_id and A == "-":
            row = 0
            column = 0
            return [row, column]
        elif A == player_id and I == player_id and E == "-":
            row = 1
            column = 1
            return [row, column]
        elif A == player_id and E == player_id and I == "-":
            row = 2
            column = 2
            return [row, column]

        if E == player_id and G == player_id and C == "-":
            row = 0
            column = 2
            return [row, column]
        elif C == player_id and G == player_id and E == "-":
            row = 1
            column = 1
            return [row, column]
        elif C == player_id and E == player_id and G == "-":
            row = 2
            column = 0
            return [row, column]


        if E == "-":
            row = 1
            column = 1
            return [row, column]
        elif A == "-":
            row = 0
            column = 0
            return [row, column]
        elif C == "-":
            row = 0
            column = 2
            return [row, column]
        
        return [row, column]


def validate_move(board: list, move: list) -> bool:
    row, col = move[0], move[1]

    if board[row][col] == "-":
        return True

    return False


def send_move(player_id: str, move: list) -> None:
    row, col = move[0], move[1]
    url = "{}/move/{}/{}/{}".format(API_URL, player_id, row, col)
    res = requests.post(url)
    return None


def does_game_continue() -> bool:
    url = "{}/continue".format(API_URL)
    res = requests.get(url)

    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def print_board(board: list) -> None:
    print("\nCurrent board: \n")
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("----------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("----------")
    print(board[2][0], "|", board[2][1], "|", board[2][2], "\n")