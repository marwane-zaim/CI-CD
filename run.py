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

    
def import_data() -> pd.DataFrame:
    """
    Import csv file as a dataframe
    Output: data [pd.DataFrame]
    """
    data = pd.read_csv("data/iris.csv")
    print(data.shape)
    return data

def rename_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Doc
    """
    data_renamed = data.rename(columns={"sepal.length": 'sepal_length',
                                "sepal.width": 'sepal_width',
                                "petal.length": 'petal_length',
                                "petal.width": 'petal_width'})
    
    return data_renamed


def extrait_du_dataSet(data :pd.DataFrame)-> pd.DataFrame:

    """
    Une fonction qui retourne 50  lignes de notre dataset
    Input : csv file as a dataframe
    Output : data [pd.DataFrame] qui retourne les 50 lignes

    """
    data_sample = data.sample(50)

    return data_sample


def multiplier_dataset(data :pd.DataFrame)-> pd.DataFrame:

    """
    Une fonction qui multiplie les 50 lignes qu'on a pris dans la fonction precedente et il multiplie ces lignes trois fois
    Input : csv file as a dataframe
    Output : data [pd.DataFrame] qui retourne les 150 lignes

    """

    data_sample = extrait_du_dataSet(data)

    data_triple = pd.concat([data_sample] * 3, ignore_index=True)

    return data_triple

if __name__ == '__main__':
    """
    Doc
    """
    main()