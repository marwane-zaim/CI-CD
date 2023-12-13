"""
CI/CD
"""
import pandas as pd


def main():
    """
    Main
    """
    data = import_data()
    rename_columns(data)

    extrait_du_dataSet(data)

    multiplier_dataset(data)

    
def import_data() -> pd.DataFrame :
    """
    Import csv file as a dataframe
    Output: data [pd.DataFrame]
    """
    data = pd.read_csv("data/iris.csv")
    print(data.shape)
    return data


def rename_columns(data : pd.DataFrame) -> pd.DataFrame :
    """
    Input
        - data (pd.DataFrame): Le DataFrame d'entrée avec des noms de colonnes éventuellement non standard.
 
    Output
        - pd.DataFrame: Un nouveau DataFrame avec des colonnes renommées selon des noms standard.
 
    Description:
        Cette fonction prend en input le dataFrame et renomme ses colonnes avec des noms standard
        Les noms standard des colonnes sont :
        - 'sepal_length' pour la colonne 'sepal.length'
        - 'sepal_width' pour la colonne 'sepal.width'
        - 'petal_length' pour la colonne 'petal.length'
        - 'petal_width' pour la colonne 'petal.width'
 
        La fonction utilise la méthode `rename` de pandas pour effectuer le renommage des colonnes.
    """
    data_renamed = data.rename(columns={"sepal.length": 'sepal_length',
                                "sepal.width": 'sepal_width',
                                "petal.length": 'petal_length',
                                "petal.width": 'petal_width'})
    
    return data_renamed


def extrait_du_dataSet(data : pd.DataFrame)-> pd.DataFrame :

    """
    Cette fonction prend en entrée un DataFrame 'data' et renvoie un nouvel échantillon
    de 50 lignes sélectionnées de manière aléatoire à partir du DataFrame d'origine.
 
    Input:
        data (pd.DataFrame): Le DataFrame de données à partir duquel extraire l'échantillon.
 
    Output:
        pd.DataFrame: Un nouveau DataFrame contenant un échantillon de 50 lignes du DataFrame d'origine.

    """
    data_sample = data.sample(50)

    return data_sample


def multiplier_dataset(data : pd.DataFrame)-> pd.DataFrame :

    """
    une fonction qui multiplie le nombre d'échantillons dans un DataFrame.
 
   INPUT
    - data (pd.DataFrame): Le DataFrame d'entrée contenant les données à multiplier.
 
    Output
    - pd.DataFrame: Un nouveau DataFrame avec le contenu répété trois fois.
 
    Description:
    Cette fonction prend un DataFrame pandas en entrée, extrait un échantillon à l'aide de la fonction `extrait_du_dataSet`,
    puis réplique cet échantillon trois fois à l'aide de la fonction `pd.concat` avec l'option `ignore_index=True`.

    """

    data_sample = extrait_du_dataSet(data)

    data_triple = pd.concat([data_sample] * 3, ignore_index=True)

    return data_triple


if __name__ == '__main__':
    """
    Doc
    """
    main()