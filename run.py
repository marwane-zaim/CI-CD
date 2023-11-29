"""
CI/CD
"""
import pandas as pd

def main():
    """
    Main
    """
    data = import_data()
    renommage_colonnes(data)

    
def import_data():
    """
    Import csv file as a dataframe
    Output: data [pd.DataFrame]
    """
    data = pd.read_csv("data/iris.csv")
    print(data.shape)
    return data

def renommage_colonnes(data:pd.DataFrame)-> pd.DataFrame:
    """
    Rennomage des colonnes
    Import:csv file as a dataframe
    Output: data [pd.DataFrame]
    """
    data_renomme = data.rename({"sepal.length":"sepal_length",
                                "sepal.width":"sepal_width",	
                                "petal.length":"petal_length", 
                                "petal.width":"petal_width",
                                "variety":"variety"
                                })
    return data_renomme


if __name__ == '__main__':
    """
    Doc
    """
    main()