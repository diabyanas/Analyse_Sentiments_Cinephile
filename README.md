___
# Brief : Analyse de critiques de films
___

Dans ce brief, il s'agit de créer une application web (via Flask), basée sur le Machine Learning, permettant d'anaylser une critique de film laissée par un utilisateur et déterminer si elle est positive ou négative.

Pour ce projet, nous devons partir de rien, c'est à dire, créer nous même notre base de données, la nettoyer et la préparer afin de l'entraîner sur un modèle de Machine Learning. 

Les étapes du projet :

### 1. Le Web Scrapping

Cette première étape va nous permettre de créer notre base de données. Nous allons récupérer des avis et notes de films sur le site Allociné grâce au Web Scrapping. Nous sélectionnant uniquement la note laissée par l'utilisateur et son commentaire afin de créer notre base de données. On sauvegarder les données récoltées dans un fichier CSV.

### 2. Préparation de la dataset

Ici il s'agit de charger et traiter la dataset. Il faut d'abord vérifier qu'il n'y a pas de valeurs nulles, si oui les supprimer. Encoder les valeurs nécessaires et enfin créer les deux classes 'avis positifs' et 'avis négatifs'. On aura déterminer que les avis négatifs sont ceux qui ont récolté une note inférieure ou égale à 3 et les avis positifs sont ceux qui ont récoltés une note supérieure à 3. On finit par représenter graphiquement la répartition des deux classes.

### 3. Mise en place du Machine Learning

On va séparer directement le dataset en Train Set et Test Set afin de ne pas entraîner le modèle sur toute la dataset et donc de fausser les résultats. On observe aussi que la répartition des deux classes n'est pas bonne, ayant beaucoup plus d'avis positifs que négatifs. Il sera nécessaire de fraire une Data Augmentation afin de rajouter des commentaires négatifs pour le rééquilibrage.
On termine par standardiser et tokéniser les commentaires du Train Set (enregistrés dans un corpus) afin de les réduire à l'essentiel (suppression, caractères spéciaux, chiffres, ponctuation, stopwords, réduction à la racine du mot). On finira par vectoriser le corpus afin de créer les nuages de mots positifs et de mots négatifs.

### 4. Création du modèle

Dans ce projet, on utilise la Logistic Regression. On calcul notre score sur le jeu de test et nous créons notre matrice de confusion afin de déterminer la précision du modèle. On teste manuellement le modèle via une phrase écrite à la main.

### 5. Sauvegarde du modèle pour intégrationà Flask

Une fois le modèle fonctionnel, il nous suffit de le suvegarder via Pickle afin de l'intégrer à l'application Flask, créée en parallèle. Dans cette même application, nous auront 2 pages, la 1ère dans laquelle l'utilisateur peut écrire son commentaire. En cliquant sur 'Predict', il basculera sur la 2ème, sur laquelle s'affichera la prédiction.