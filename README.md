# CI-CD
ZAIM SASSI Marwane<br>
AMIAR Sarah<br>
CHAIR Roa<br>

<h1>Fonction Rennomage </h1><br>
    Input<br>
    - data (pd.DataFrame): Le DataFrame d'entrée avec des noms de colonnes éventuellement non standard.<br>
    Output<br>
    - pd.DataFrame: Un nouveau DataFrame avec des colonnes renommées selon des noms standard.<br>
    Description:<br>
    Cette fonction prend en input le dataFrame et renomme ses colonnes avec des noms standard<br>
    Les noms standard des colonnes sont :<br>
    - 'sepal_length' pour la colonne 'sepal.length'<br>
    - 'sepal_width' pour la colonne 'sepal.width'<br>
    - 'petal_length' pour la colonne 'petal.length'<br>
    - 'petal_width' pour la colonne 'petal.width'<br>
    La fonction utilise la méthode `rename` de pandas pour effectuer le renommage des colonnes.<br>

<h1>Fonction Sample 50 lignes </h1><br>
    Cette fonction prend en entrée un DataFrame 'data' et renvoie un nouvel échantillon<br>
      de 50 lignes sélectionnées de manière aléatoire à partir du DataFrame d'origine.<br>
       Input:<br>
        data (pd.DataFrame): Le DataFrame de données à partir duquel extraire l'échantillon.<br>
       Output:<br>
        pd.DataFrame: Un nouveau DataFrame contenant un échantillon de 50 lignes du DataFrame d'origine.<br>

<h1>Fonction multiplication 150 lignes</h1><br>  
une fonction qui multiplie le nombre d'échantillons dans un DataFrame.<br>
 
   INPUT<br>
    - data (pd.DataFrame): Le DataFrame d'entrée contenant les données à multiplier.<br>
    Output<br>
    - pd.DataFrame: Un nouveau DataFrame avec le contenu répété trois fois. <br>
    Description:<br>
    Cette fonction prend un DataFrame pandas en entrée, extrait un échantillon à l'aide de la fonction `extrait_du_dataSet`,<br>
    puis réplique cet échantillon trois fois à l'aide de la fonction `pd.concat` avec l'option `ignore_index=True`.<br>
    
