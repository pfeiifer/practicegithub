import pytest
import main

@pytest.mark.parametrize("input_values,expected_a,expected_b", [
    (["3", "4"], 3, 4),
    (["0", "0"], 0, 0),
    (["-5", "10"], -5, 10),
    (["100", "200"], 100, 200),
])
def test_user_input(monkeypatch, input_values, expected_a, expected_b):
    # Create an iterator from the input values
    input_iterator = iter(input_values)
    # Patch input() to return values from our iterator
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
    # Call the function
    a, b = main.user_input()
    # Assert the results
    assert a == expected_a
    assert b == expected_b