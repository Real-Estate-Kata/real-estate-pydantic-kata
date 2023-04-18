- [ ] read csv
    - [x] write failing test for row count
    - [ ] let it pass
    - [ ] unskip the failing test for column names
    - [ ] make the test pass

- [ ] Create the data object from a dict
    - [ ] read the passing test `test_create_valid_house` in `test_validate.py`. It creates a valid house object and checks yearbuilt is correctly populated.
    - [ ] add a new assert to `test_create_valid_house` to check if `Id` field is populated correctly as `1`
    - [ ] make it pass by adding an attribute to the class `House`
    - [ ] one by one add more tests for each field: `Street = 'Sesame'`, `Fireplaces=0`, `FireplaceQu=None` to the test and let it pass each time

- [ ] Data object with first floor and second floor footage
    - [ ]  Write a failing test for creating House with 1stFlrSF=100, 
    - [ ] It is tricky to add it to the `House` class as it starts with a not-a-letter character!
    - [ ] In the House class, use Pydantic `Field(alias='..')` function to give it a valid name
    - [ ] make it pass. 
    - [ ] Same for 2ndFlrSF=50.

- [ ] Refactor
    - [ ] once on green, think about refactoring. Would you like to rename fields to have more readable names? Do they have to be the same as CSV column names?
    - [ ] In the House class, rename the property `FireplaceQu` to be `FireplaceQuality` using Pydantic `Field` function
    - [ ] Do you want to rename any functions?
    

- [ ] Let's move to data validation. Let's start with validation of the YearBuilt field
    - [ ] write a failing test `test_YearBuilt_error` for creating a House object with yearbuilt 2000. The test expects a `ValidationError` stating YearBuilt is the issue
    - [ ] make the test pass by adding a pydantic validator for the field `YearBuilt` to the `House` class
    - [ ] Refactor on green. Is there any duplicate code in tests? Maybe add default values as params of `create_house` function in `test_validate.py`? 
    - [ ] Use more invalid year values with `@pytest.mark.parametrize("invalid_year",[1600,1700,1900,2000])` annotation for `test_YearBuilt_error`


- [ ] validation firstfloor is at least one third of the 2nd floor
    - [ ] write a failing test for creating a House object with  1stFlrSF=10, 2ndFlrSF=50. Expect a validation error using `pytest.raises(ValidationError)`.
    - [ ] make it pass by adding a validator `check_first_floor_at_least_third_of_second` to House class. Which field should it be added to - FirstFloorSquareFeet or SecondFloorSquareFeet? The order of fields is important in Pydantic class.
    - [ ] Parametrize the test with `@pytest.mark.parametrize("first_floor_square_feet,second_floor_square_feet",[(5, 20), (10, 50),(10, 30),])`



- [ ] validation FireplaceQuality is one of 'Ex', 'Gd', 'TA', 'Fa', 'Po', None
  - [ ] write a regression test for creating a House object with Fireplaces=5 and  fireplacequality being 'Ex'. Expect creation of a valid object.
  - [ ] write a failing test for creating a House object with Fireplaces=5 and  fireplacequality being 'OK'. Expect a validation error.
  - [ ] make it pass by creating a new class `FireplaceQualityEnum` 

- [ ] validation if Fireplaces is greater than 0, FireplaceQu is required.
   - [ ] write a failing test for creating a House object with  fireplacequality being empty while Fireplaces is 1
  - [ ] make it pass. Return a validation error
  - [ ] check can still create a House object with fireplacequality empty while Fireplaces is 0

- [ ] create a HouseList class to hold multiple houses
    - write a failing test creating a list of two houses
    - make it pass 

- [ ] unique Id validation
    - write a failing test creating a list of two houses with same Id
    - make it pass - Return a validation error

- [ ] HouseList only of valid houses
    - write a failing test creating a list of two houses where one of them is invalid. Check it returns a list with only one valid house.
    - make it pass 

- [ ] HouseList only of valid houses from csv
    - write a failing test to read csv in data/train.csv and only return valid houses. can you assert on number of houses?
    - do you have an error for fireplacequality being NA? what does pandas use for the missing value? is it different to what pydantic expects as the missing value for FireplaceQuality? what is the best way to fix that? 







