# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:52:49 2021

@author: nator
"""
import random

def generate_cards(n):
  numbers = []
  for i in range(1, n + 1):
    numbers += [i, i]
  
  return numbers


def build_game(array):
  front_matrix = []
  back_matrix = []

  for i in range(0, len(array), 2):
    front_matrix.append(["*", "*"])
    back_matrix.append([array[i], array[i + 1]])

  return front_matrix, back_matrix



def print_board(matrix):
  print("    0    1")
  for i in range(len(matrix)):
    print(i, matrix[i])
    


def next_turn(turn):
  if turn == 1:
    return 0

  return 1
        

def choose_card(back_board):
  while True:
    row = int(input("\nIngresa la fila: "))
    col = int(input("Ingresa la columna: "))

    if row < len(back_board) and col < len(back_board[0]):
      break

    print("Elige una coordenada valida")

  return row, col
## if o elif ???####
## falta comprobar cuando se eligen coordenadas con " "   ############################
## falta restringir elegir la misma carta para armar una pareja ##########


print("--------- Bienvenido al Memorice! ---------\n")
user_1 = input("Ingresa el nombre de usuario 1: ")
user_2 = input("Nombre de usuario 2: ")
n_pairs = int(input("\n¿Con cuántos pares de cartas van a jugar? "))

turn = 0
points = [0, 0]
players = [user_1, user_2]

while n_pairs % 2 != 0 and n_pairs > 0:
    print("Debes ingresar un número par de cartas")
    n_pairs = int(input("¿Con cuántos pares de cartas van jugar? "))

continue_playing = True

numbers = generate_cards(n_pairs)
random.shuffle(numbers)

front_board, back_board = build_game(numbers)

while continue_playing:
  print("\n-------- Es el turno de:", players[turn], "--------\n")
  aux_board = front_board[:]

  print_board(aux_board)

  # Elije una carta
  row_1, col_1 = choose_card(back_board)
  card_1 = back_board[row_1][col_1]
  aux_board[row_1][col_1] = str(card_1)
  print_board(aux_board)

  row_2, col_2 = choose_card(back_board)
  card_2 = back_board[row_2][col_2]
  aux_board[row_2][col_2] = str(card_2)
  print_board(aux_board)

  if card_1 == card_2:
    print("\nEncontraste una pareja!")
    points[turn] += 1
    aux_board[row_1][col_1] = " "
    aux_board[row_2][col_2] = " "

  else:
    print("\nPerdiste el turno")
    # aux_board = front_board
    aux_board[row_1][col_1] = "*"
    aux_board[row_2][col_2] = "*"
    turn = next_turn(turn)

  if points[0] + points[1] >= n_pairs:
    print("Terminó el juego... El ganador es:")

    if points[0] < points[1]:
      print("----", players[1], "----")
    else:
      print("----", players[0], "----")

    continue_playing = False  
    
