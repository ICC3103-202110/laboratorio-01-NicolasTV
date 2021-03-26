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
    front_matrix.append(['*', '*'])
    back_matrix.append([array[i], array[i + 1]])

  return front_matrix, back_matrix
    


        
      

    
print('--------- Bienvenido al Memorize! ---------\n')
user_1 = input("Ingresa el nombre de usuario 1: ")
user_2 = input("Nombre de usuario 2: ")
n_pairs = int(input("\n¿Con cuántos pares de cartas van a jugar? "))

turn = 0
points = [0, 0]
players = [user_1, user_2]

while n_pairs % 2 != 0 and n_pairs > 0:
    print("Debes ingresar un número par de cartas")
    n_pairs = int(input("¿Con cuántos pares de cartas a jugar? "))

   
    
