# Le Pack

/* rendre beau cette partie un peu plus tard */-\
/* 📢 zone breaking changes ? */

Le Pack est une **compilation de mini-jeux simplistes** basés sur le module PyGame. Il reprend des concepts de mini-jeux de réflexion phares en une version simple en design.

Le Pack est constitué des jeux suivants :
- Le Mot (version revisitée du Wordle)
- Le Nombre (version revisitée du Juste Prix)

À terme, il contiendra /* à compléter */ mini-jeux. 

## 🎮 Jouer 🎮 

### 📋 Les prérequis
Le Pack est conçu avec Python (et en particulier la librairie PyGame).\
Il est nécessaire d'avoir un ordinateur équipé d'une version de Python (au moins 3.11) et d'avoir installer la librairie PyGame.\
Liens utiles :
- [télécharger Python](https://www.python.org/downloads/)
- [installer PyGame](https://pypi.org/project/pygame/) (une version de PyGame Community Edition est également possible)

### ⬇️ Obtenir le jeu
Une fois les prérequis satisfaits, vous pouvez obtenir le jeu de deux manières différentes.

Vous pouvez **télécharger un dossier ``.zip``** dans l'onglet **Releases** situé sur la droite. Plus bas, une explication du fonctionnement des releases.\
Lorsque le téléchargement est terminé, dézipper le dossier puis faîtes tourner le fichier ``main.py`` avec un IDE ou l'instruction ``python main.py`` (cette instruction doit être écrite dans un terminal ouvert depuis le dossier dézippé).

Si vous avez Git installé sur votre machine, vous pouvez aussi écrire les instructions suivantes sur un terminal de commande :
```bash
git clone  git@github.com:HiAbdounour/le_pack.git --branch <nom de la release>
cd le_pack
python main.py
```

*Remarque : pour obtenir la dernière version du jeu (dont les modifications pas encore publiées sous forme de releases), vous pouvez remplacer la première instruction par ``git clone https://github.com/HiAbdounour``.*

## Les règles
Chaque jeu contient un fichier ``README.md`` où sont exposés les règles.\
Dans le navigateur, **cliquez sur un dossier** (chaque dossier contient un mini-jeu); les règles apparaîtront en bas après la liste des fichiers du dossier.

## Fonctionnement des releases
La nomination des releases pour ce projet est la suivante :\
/* met moi ça sous une belle image */

                                                             v2.1.2
                                                              |  | ∟ nombre de patchs, corrections de bug (ex: 2e patch)
                                                              |  ∟ nombre de changements importants (ex: 1er changement: ajout d'un système de points)
                                                              ∟ nombre de mini-jeux (ex: 2 mini-jeux)

## Licence
L'ensemble du projet est soumis et publié sous la licence GNU GPL v3. Plus d'infos dans le fichier ``LICENSE``.
