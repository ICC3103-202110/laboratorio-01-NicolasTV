# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:52:49 2021

@author: nator
"""
import random 
import numpy as np


user_1=input("Hola! Ingresa el nombre de usuario 1: ")
user_2=input("Nombre de usuario 2: ")

n_cards=int(input("¿Con cuántas cartas van a jugar? "))
while n_cards % 2 != 0:
    print("Debes ingresar un número par de cartas")
    n_cards=int(input("¿Con cuántas cartas van a jugar? "))

row = int(n_cards/2) 
column = int(n_cards/2)

matrix_1 = []
matrix_2 = []

for i in range(row):
    a=i+1
    matrix_1.append([a])
    for j in range(column):
        b=j+1
        matrix_1.append([b])
        
print(matrix_1)
       
   
    
