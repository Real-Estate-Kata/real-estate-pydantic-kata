from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field, validator
import pandas as pd

def read_csv():
    df = pd.read_csv('data/train.csv',usecols=["Id", "Street", "YearBuilt", "Fireplaces", "FireplaceQu", "1stFlrSF", "2ndFlrSF"])
    return df

class FireplaceQualityEnum(str, Enum):
    Ex = "Ex"
    Gd = "Gd"
    TA = "TA"
    Fa = "Fa"
    Po = "Po"

class House(BaseModel):
    YearBuilt: int
    Id: int
    Fireplaces: int
    FireplaceQuality: Optional[FireplaceQualityEnum] = Field(alias="FireplaceQu")
    Street: str
    FirstFlrSF: int = Field(alias="1stFlrSF")
    SecondFlrSF: int = Field(alias="2ndFlrSF")

    @validator("YearBuilt")
    def check_year_built_within_range(cls, v):
        assert (v>1700) and (v < 1900 ), "Yearbuilt not in range of 1700-1900"
        return v

    @validator("SecondFlrSF")
    def check_first_floor_at_least_third_of_second(cls, v, values,  **kwargs):
        
        assert (values["FirstFlrSF"] >= (v /3) ), "First floor must be at least one third of second"
        return v
