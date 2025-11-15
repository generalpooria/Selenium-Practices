import pytest
@pytest.fixture
def sample_data():
    print("Setting up sample data")
    yield [1, 2, 3, 4, 5]
    print("Tearing down sample_data")

#parameterized fixture example
@pytest.fixture(params=[(1,2,3),(4,5,9),(10,20,30)])
def addition_data(request):
    yield request.param
    print("Tearing down addition_data")

