#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""demo_00.py - une simple demo des des fonctions de base.
   
   A saisir dans l'interpréteur Python.
   Ou saisir " from exemples.demo_00 import * " depuis l'interpréteur
 
Created by Meurisse D. <info@mchobby.be>
Licence : CC-BY-SA
"""
from init import * 

avance( 100 )
droite( 90 )
couleur_crayon( VERT )
taille_crayon( 5 )
for i in range(13):
	avance(10)
	droite(10)
	
taille_crayon( 3 )
couleur_crayon( ORANGE )
for i in range(13):
    avance(10)
    gauche(10)


