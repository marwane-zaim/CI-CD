"""
Tests
"""
from run import import_data, renommage_colonnes

def test_import_data():
    """
    Test
    """
    data = import_data()
    assert data.shape[0] > 0


def test_renommage_colonnes():
    """
    Test
    """
    data = import_data()
    data_renomme = renommage_colonnes(data)

    assert "sepal_length" in data_renomme.columns
