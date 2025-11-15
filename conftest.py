import pytest
@pytest.fixture
def sample_data():
    print("Setting up sample data")
    yield [1, 2, 3, 4, 5]
    print("Tearing down sample_data")