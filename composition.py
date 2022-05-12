# -*- coding: utf-8 -*-
"""
Created on Wed May 11 21:10:17 2022

@author: salome
"""
import itertools as it

#Définitions variables 
nbr_joueurs=15
nbr_sur_terrain=11

#Définition de la classe joueurs
class Joueurs:  
    def __init__(self, nom, post, maillot):  
        self.nom = nom  
        self.post = post
        self.maillot = maillot
        
#Définition des joueurs 
list = []  
  
list.append( Joueurs('Maubleu', 'Gardien', 1) ) 
list.append( Joueurs('Monfray', 'DéfenseurCD', 5) ) 
list.append( Joueurs('Nestor', 'DéfenseurCG', 14) ) 
list.append( Joueurs('Néry', 'ArrièreLD', 17) )
list.append( Joueurs('Gersbach', 'ArrièreLG', 20) ) 
list.append( Joueurs('Bambock', 'MilieuCD', 16) ) 
list.append( Joueurs('Michel', 'MilieuCG', 10) ) 
list.append( Joueurs('Gaspar', 'MilieuD', 12) )
list.append( Joueurs('Abdallah', 'MilieuG', 29) ) 
list.append( Joueurs('Sanyang', 'AvantCD', 2) ) 
list.append( Joueurs('Anani', 'AvantCG', 11) )
list.append( Joueurs('Perez', 'MilieuCD', 4) ) 
list.append( Joueurs('DeIriondo', 'MilieuD', 18) ) 
list.append( Joueurs('Tchaptchet', 'DéfenseurCG', 21) ) 
list.append( Joueurs('Ravet', 'MilieuG', 22) )

#Positionnement des joeurs sans remplaçants
Postes=['Gardien', 'DéfenseurCD', 'DéfenseurCG', 'ArrièreLD','ArrièreLG',
        'MilieuCD', 'MilieuCG', 'MilieuD', 'MilieuG', 'AvantCD', 'AvantCG']
P=[]    
for i in range (nbr_joueurs) :
    P.append(list[i].post) #On créer une liste des postes des joueurs disponibles

SR=[] #Sans remplaçants
R=[] #Remplaçants
for poste in Postes:
    if P.count(poste)==1:
        k=P.index(poste)
        SR.append(list[k]) 
    else:
        k=P.index(poste)
        l=P.index(poste, k+1) #Le code ne marcherait pas si on a plus de deux joueurs sur le même poste
        R.append([list[k], list[l]])
        
compoR=[]
for I in it.product(R[0], R[1], R[2], R[3]):
    compoR.append(I) #Liste des compositions des remplaçants possible

#Compositions possibles
compo=[]
compoF=[]
for m in range (len(compoR)):
    for l in range (len(SR)):
        compo.append(SR[l])
    for n in range (len(R)):
        compo.append(compoR[m][n])
    compoF.append(compo)
    compo=[]  
 
#Affichage des compositions     
print('Il y a %d compositions possible' %len(compoF))
for k in range (len(compoF)):
    print('\n Composition %d :' %(k+1))
    for l in range (len(compoF[1])):
        print('%s : %d - %s' %(compoF[k][l].post, compoF[k][l].maillot, compoF[k][l].nom))
