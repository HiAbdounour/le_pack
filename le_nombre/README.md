
# Le Nombre  

*Juste Prix revisité*
  
Le but du jeu est de trouver un nombre choisi aléatoirement. Le joueur a le choix entre des nombres de 1, 2, 3 ou 4 chiffres. Le joueur dispose d'un nombre illimité* d'essais pour trouver le nombre caché.\
À chaque essai, le nombre renseigné par le joueur s'affiche dans une liste d'essais avec une certaine couleur :  
- rouge si le nombre renseigné est strictement plus petit que le nombre caché  
- bleu si le nombre renseigné est strictement plus grand que le nombre caché  
- vert si le nombre a été trouvé  
  
La partie se termine lorsque le joueur a trouvé le nombre caché. Ensuite, elle ramène au menu du jeu.  
  
*\*En théorie, les essais sont illimités. En pratique, la liste des nombres essayés devient si grande qu'elle dépasse la taille de la fenêtre graphique. À partir de ce moment, il devient difficile de trouver le nombre caché.*  
  
## Sources  
  
Le Nombre est une version revisitée du Jeu du Juste Prix.\  
La génération aléatoire du nombre est gérée par le module ``random`` de Python.