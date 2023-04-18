import pytest

from pydantic import ValidationError

from validate import House, read_csv



def test_csv_read():
    df = read_csv()
    assert len(df) == 1460


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
    assert house.Id == 1
    assert house.Fireplaces == 0
    assert house.FireplaceQuality == None
    assert house.Street == "Sesame"
    assert house.FirstFlrSF == 100
    assert house.SecondFlrSF == 50

@pytest.mark.parametrize("invalid_year",[1600,1700,1900,2000])
def test_create_house_YearBuilt_error(invalid_year):
    with pytest.raises(ValidationError):
        d = {
            "YearBuilt": invalid_year,
            "Id": 1,
            "Fireplaces": 0,
            "FireplaceQu": None,
            "Street": "Sesame",
            "1stFlrSF": 100,
            "2ndFlrSF": 50,
        }
    
        house = House(**d)
    
def test_create_house_invalid_sf():
    with pytest.raises(ValidationError):
        d = {
            "YearBuilt": 1800,
            "Id": 1,
            "Fireplaces": 0,
            "FireplaceQu": None,
            "Street": "Sesame",
            "1stFlrSF": 10,
            "2ndFlrSF": 50,
        }
    
        house = House(**d)


def test_create_house_FireplaceQuality_valid_Ex():
    d = {
            "YearBuilt": 1800,
            "Id": 1,
            "Fireplaces": 5,
            "FireplaceQu": "Ex",
            "Street": "Sesame",
            "1stFlrSF": 100,
            "2ndFlrSF": 50,
        }
    
    house = House(**d)
    assert house.YearBuilt == 1800
    assert house.Id == 1
    assert house.Fireplaces == 5
    assert house.FireplaceQuality == "Ex"
    assert house.Street == "Sesame"
    assert house.FirstFlrSF == 100
    assert house.SecondFlrSF == 50

def test_create_house_FireplaceQuality_invalid():
    with pytest.raises(ValidationError):
        d = {
                "YearBuilt": 1800,
                "Id": 1,
                "Fireplaces": 5,
                "FireplaceQu": "OK",
                "Street": "Sesame",
                "1stFlrSF": 100,
                "2ndFlrSF": 50,
            }
        
        house = House(**d)
