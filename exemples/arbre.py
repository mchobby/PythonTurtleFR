#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""arbre.py - réalisation d'un arbre fractale.
   
   A saisir dans l'interpréteur Python.
   Ou saisir " from exemples.arbre import * " depuis l'interpréteur
 
Created by Meurisse D. <info@mchobby.be>
Licence : CC-BY-SA
"""
from init import * 

couleur_crayon( VERT )
taille_crayon( 5 )
leve_crayon()
recule( 200 )
baise_crayon()

def dessin_fractal(blen):
    if(blen<10):
    	# limiter le rappel de fractale parce 
    	# qu'il se rapelle indefiniment
        return
    else:
        avance(blen)
        gauche(30)
        dessin_fractal(3*blen/4)
        droite(60)
        dessin_fractal(3*blen/4)
        gauche(30)
        recule(blen)

# Appeler la fonction
dessin_fractal( 120 )
