# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:52:49 2021

@author: nator
"""
import random 

user_1=input("Hola! Ingresa el nombre de usuario 1: ")
user_2=input("Nombre de usuario 2: ")

n_cards=int(input("¿Con cuántas cartas van a jugar? "))
while n_cards % 2 != 0:
    print("Debes ingresar un número par de cartas")
    n_cards=int(input("¿Con cuántas cartas van a jugar? "))

row = int(n_cards/2) 
column = int(n_cards/2)


def Front_cards():
    numbers=[]
    a=1
    for i in range(row): 
        numbers.append([a])
        a+=1  
    return numbers*2

for r in range(row):
    for c in range(column):
        print(Front_cards[r][c],end=" ")
      

    

   
    
