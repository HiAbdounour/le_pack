# Le Mot
    
*Wordle revisité*

Le but de ce jeu est de trouver un mot choisi aléatoirement parmi une liste de mots prédéfinie. Le joueur a le choix entre des mots de 3, 4, 5 ou 6 lettres, en langue française et sans accents.\
Le joueur dispose pour cela de 6 essais. À chaque essai, des informations sont données quant aux lettres partagées avec le mot à trouver :  
- si le fond de la lettre est vert : cela signifie que la lettre est présente au bon endroit dans le mot à deviner  
- si le fond est orange : cela signifie que la lettre est dans le mot mais placé à un autre endroit (prend aussi en compte le cas des lettres présentes en double)  
- si le fond est gris foncé, cela signifie que la lettre n'apparaît pas dans le mot.  
- si un mot n'existe pas (= n'est pas présent dans la liste de mots), l'essai n'est pas comptabilisé et le message "Mot non reconnu" apparaît en bas de l'écran. Il faut attendre une seconde avant de pouvoir modifier le mot écrit. 

Les couleurs sont récapitulées dans le petit alphabet en bas de la partie.
  
La partie se termine lorsque le joueur a trouvé le mot ou lorsque les six essais n'ont pas été concluants. Après trois secondes, le joueur est renvoyé sur le menu pour pouvoir lancer une autre partie.  
 
## Sources  
  
Le Mot est une version revisitée à ma sauce du [Wordle](https://github.com/louanben/wordle-fr).   
  
Les mots utilisés dans ce jeu sont tirés de la version 6 (2012) du Dictionnaire Officiel du Scrabble. Tous les mots utilisés dans le jeu ont une longueur comprise entre 3 et 6 lettres et sont conservés dans les fichiers .txt du repo.\
Par exemple, le fichier *mots4.txt* contient tous les mots valides de 4 lettres.