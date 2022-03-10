# Rendu Romain PANI

Bienvenue dans le rendu de Romain PANI en B3-B pour le projet python.<br />
Dans ce README vous trouvez le détail de chaque parties, comment les démarrer et comment lancer les tests. 

## Sommaire

1. [Partie 1](#part1)
    1. [Tester la partie 1](#part1test)
2. [Partie 2](#Partie 2)
    1. [Tester la partie 2](#part2test)
3. [Partie 3](#Partie 3)
    1. [Tester la partie 3](#part3test)
4. [Partie 4](#Partie 4)
    1. [Tester la partie 4](#part4test)
5. [Partie 5](#Partie 5)
    1. [Tester la partie 5](#part5test)

##  <a name="part1">Partie 1</a>
Pour cette partie, veuillez vous mettre dans le dossier part1. <br/>
La racine de votre terminal de commande doit finir par :
```
\part1
```
Création du fichier txt : 
- Le fichier txt "insertion.txt" se crée automatiquement en lançant le fichier python insertion.py

Pour insérer des mots dans le fichier, il suffit de lancer le fichier python insertion.py avec : 

```
py insertion.py
```
Une fois le programme lancé, vous pouvez insérer des mots. <br/> 
Pour arrêter l'insertion, vous devez insérer le mot "--fin"
<br/>
<br/>
Pour obtenir le rapport des mots dans le fichier insertion.txt, il suffit de lancer le fichier python rapport.py avec :
```
py rapport.py
```
# <a name="part1test">Tester la partie 1</a>
Pour tester la partie 1, il suffit de lancer cette commande : 
```
coverage run -m unittest all_test.py
```
Ensuite, pour obtenir le taux de coverage, il suffit de lancer la commande : 
```
coverage report 
```
##  <a name="part2">Partie 2</a>
Pour cette partie, veuillez vous mettre dans le dossier part2. <br/>
La racine de votre terminal de commande doit finir par :
```
\part2
```
Création de la base de données : 
- Le base de données sqlite3 "insertion.sql" NE SE CREE PAS automatiquement.
 - Pour le faire, il faut décommenter le code situé en haut du fichier insertion.py

Pour insérer des mots dans la base de données sqlite3, il suffit de lancer le fichier python insertion.py avec : 

```
py insertion.py
```
Une fois le programme lancé, vous pouvez insérer des mots. <br/> 
Pour arrêter l'insertion, vous devez insérer le mot "--fin"
<br/>
<br/>
Pour obtenir le rapport des mots dans la base de données sqlite3, il suffit de lancer le fichier python rapport.py avec :
```
py rapport.py
```
# <a name="part2test">Tester la partie 2</a>
Pour tester la partie 2, il suffit de lancer cette commande : 
```
coverage run -m unittest all_test.py
```
Ensuite, pour obtenir le taux de coverage, il suffit de lancer la commande : 
```
coverage report 
```

##  <a name="part3">Partie 3</a>
Pour cette partie, veuillez vous mettre dans le dossier part3. <br/>
La racine de votre terminal de commande doit finir par :
```
\part3
```
Création de la base de données : 
- Le base de données sqlite3 "insertion.sql" NE SE CREE PAS automatiquement.
 - Pour le faire, il faut décommenter le code situé en haut du fichier insertion.py

Pour insérer des mots dans la base de données sqlite3, il suffit de lancer le fichier python insertion.py avec : 

```
py insertion.py
```
Une fois le programme lancé, vous pouvez insérer des mots. <br/> 
Pour arrêter l'insertion, vous devez insérer le mot "--fin"
<br/>
<br/>
Pour obtenir le rapport des mots dans la base de données sqlite3, il suffit de lancer le fichier python rapport.py avec :
```
py rapport.py
```
Pour obtenir le rapport précédent mais avec les caractères plutôt que les mots, il suffit de lancer le fichier python rapport.py avec l'option -c :
```
py rapport.py -c
```
# <a name="part3test">Tester la partie 3</a>
Pour tester la partie 3, il suffit de lancer cette commande : 
```
coverage run -m unittest all_test.py
```
Ensuite, pour obtenir le taux de coverage, il suffit de lancer la commande : 
```
coverage report 
```

##  <a name="part4">Partie 4</a>
Pour cette partie, veuillez vous mettre dans le dossier part4. <br/>
La racine de votre terminal de commande doit finir par :
```
\part4
```
Création de la base de données : 
- Le base de données sqlite3 "insertion.sql" NE SE CREE PAS automatiquement.
 - Pour le faire, il faut décommenter le code situé en haut du fichier insertion.py

Pour cette partie, il faut ouvrir deux terminaux de commande. 
Dans le premier, on va lancer le serveur avec la commande : 
```
py main.py
```
Normalement il devrait être affiché : 
```
Server running at localhost:8080...
```
Désormais, les commandes suivantes devront être rentré dans le second terminal.
Pour insérer des mots dans la base de données sqlite3, il suffit de lancer la commande curl localhost:8080/integration -d "" avec entre les guillemets les mots que vous souhaitez insérer : 

```
curl localhost:8080/integration -d " "
```

<br/>
<br/>
Pour obtenir le rapport des mots dans la base de données sqlite3, il suffit de lancer la commande curl localhost:8080/rapport :

```
curl localhost:8080/rapport
```
# <a name="part4test">Tester la partie 4</a>
Pour tester la partie 4, il suffit de lancer cette commande : 
```
coverage run -m unittest all_test.py
```
Ensuite, pour obtenir le taux de coverage, il suffit de lancer la commande : 
```
coverage report 
```


##  <a name="part5">Partie 5</a>
Pour cette partie, veuillez vous mettre dans le dossier part5. <br/>
La racine de votre terminal de commande doit finir par :
```
\part5
```
Création de la base de données : 
- Le base de données sqlite3 "insertion.sql" NE SE CREE PAS automatiquement.
 - Pour le faire, il faut décommenter le code situé en haut du fichier insertion.py

Pour cette partie, il faut ouvrir deux terminaux de commande. 
Dans le premier, on va lancer le serveur avec la commande : 
```
py main.py
```
Normalement il devrait être affiché : 
```
Server running at localhost:8080...
```
Désormais, les commandes suivantes devront être rentré dans le second terminal.
Pour insérer des mots dans la base de données sqlite3, il suffit de lancer la commande curl localhost:8080/integration -d "" avec entre les guillemets les mots que vous souhaitez insérer : 

```
curl localhost:8080/integration -d " "
```

<br/>
<br/>
Pour obtenir le rapport des mots dans la base de données sqlite3, il suffit de lancer la commande curl localhost:8080/rapport :

```
curl localhost:8080/rapport
```
Pour obtenir le mot le plus souvent associé à un autre, il suffit de lancer la commande curl localhost:8080/suivant?mot=test où test est le mot de votre choix :

```
curl localhost:8080/suivant?mot=test
```
# <a name="part5test">Tester la partie 5</a>
Pour tester la partie 5, il suffit de lancer cette commande : 
```
coverage run -m unittest all_test.py
```
Ensuite, pour obtenir le taux de coverage, il suffit de lancer la commande : 
```
coverage report 
```