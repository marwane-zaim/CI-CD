"""
Tests
"""
from run import import_data, rename_columns, extrait_du_dataSet

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
    Doc
    """
    data =  import_data()
    data_extrait =  extrait_du_dataSet(data)

    assert len(data_extrait) == 50

