import pytest

@pytest.mark.smoke
def test_sum(sample_data):
    print("Running test_sum")
    assert sum(sample_data) == 15

#skip this test

def test_addition(addition_data):
    print("Running test_addition with data:", addition_data)
    a, b, expected = addition_data
    assert a + b == expected
@pytest.mark.skip(reason="Skipping multiplication test")
def test_length(sample_data):
    print("Running test_length")
    assert len(sample_data) == 5, "Length should be 5"