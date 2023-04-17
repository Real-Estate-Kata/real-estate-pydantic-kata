import pytest
from validate import House, read_csv


def test_csv_read():
    df = read_csv()
    assert len(df) == 1460

@pytest.mark.skip(reason="unskip according to the tasklist")
def test_columns():
    df = read_csv()
    assert set(df.columns.values) == set(
        ["Id", "Street", "YearBuilt", "Fireplaces", "FireplaceQu", "1stFlrSF", "2ndFlrSF"]
    )


def create_house():
    d = {
        "YearBuilt": 1800,
        "Id": 1,
        "Fireplaces": 0,
        "FireplaceQu": None,
        "Street": "Sesame",
        "1stFlrSF": 100,
        "2ndFlrSF": 50,
    }

    return House(**d)


def test_create_house_YearBuilt():
    house = create_house()
    assert house.YearBuilt == 1800
