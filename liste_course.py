#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

LISTE = []

MENU_CHOICES = ["1", "2", "3", "4", "5"]

MENU = """ faire un choix parmi les 5 options suivantes :
1-ajouter un élement a la liste
2-retirer un élement de la liste
3-afficher la liste
4-vider la liste
5-quitter
votre choix ?
"""
while True:
    user_choice = input(MENU)
    if user_choice not in MENU_CHOICES:
        print("Veuillez choisir une option valide...")
        continue

    
    
    if user_choice == "1":  # Ajouter un élément
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste.")
    elif user_choice == "2":
        item = input("entrez le nom de l'element à retirer de la liste :")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élément {item} a bien été supprimé de la liste :")
        else:
                print(f"l'élement {item} n'est pas dans la liste.")	
    elif user_choice == "3":
    	if LISTE:
    		print("voici le contenu de votre liste :")
    		for i, item in enumerate(LISTE, 1):
		       print(f"{i}- {item} ") 
    	else:
    			print("votre liste est vide. ")
    if user_choice == "4":
    	LISTE.clear()
    	print("laliste est vide")

    if user_choice == "5":
    	print("au revoir")

    	sys.exit()
print("_" *30)
