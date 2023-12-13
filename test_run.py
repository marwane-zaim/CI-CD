"""
Tests
"""
from run import import_data, rename_columns, extrait_du_dataSet, multiplier_dataset


def test_import_data():
    """
    Test
    """
    data = import_data()
    assert data.shape[0] > 0


def test_rename_columns():
    """
    Doc
    """
    data = import_data()
    data_renamed = rename_columns(data)
    assert "sepal_length" in data_renamed.columns


def test_extrait_du_dataSet():
    """
    Vérifier si les lignes prises égales à 50 lignes
    """
    data = import_data()
    data_extrait = extrait_du_dataSet(data)
    assert len(data_extrait) == 50


def test_multiplier_dataset():
    """
    Verifier si les lignes sont multipliés est égal à 150 lignes
    """
    data = import_data()
    data_triple = multiplier_dataset(data)
    assert len(data_triple) == 150
