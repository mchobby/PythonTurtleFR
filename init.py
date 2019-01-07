#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""init.py - prepare un Python Turtle en Français pour Python
 
Created by Meurisse D. <info@mchobby.be>
Licence : CC-BY-SA
"""
from turtle import *

# constante
TORTUE = "turtle"
FLECHE = "arrow"

# redefinir des fonctions en français
leve_crayon = pu
lc = pu
baise_crayon = pd
bc = pd 
avance = fd
av = fd
recule = bk
re = bk 
droite = rt
dr = rt
gauche = lt
taille_crayon = pensize
tc = pensize
couleur_crayon = pencolor
cc = pencolor
forme = shape

def origine():
	home()
	lt( 90 ) # pointer vers le haut

efface = clear

def init(): # équivalent du reset
	reset()
	lt( 90 ) # pointer vers le haut

# prépare une configuration par défaut
setup( 640, 480 )
colormode( 255 ) # passe en RGB 0..255
forme( TORTUE )
init()
print( 'Bienvenu sur le Python Turtle Francophile!')