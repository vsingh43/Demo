# test_sample.py

from modules.sample_module import sample_function
import pytest


def test_sample_function():
    """Test the normal case for sample_function."""
    result = sample_function()
    assert result == "Hello, World!"


def test_empty_string():
    """
    Example for testing if the function handles an empty string input.
    Although sample_function does not take input, it's a good template for functions that do.
    """
    # Simulating a hypothetical function that takes an input
    # Assuming function_that_handles_input("") should return a default or error message
    # Uncomment and implement if needed
    # result = function_that_handles_input("")
    # assert result == "Expected Value"


def test_performance(benchmark):
    """Test the performance of the sample_function by using the pytest benchmark fixture."""
    result = benchmark(sample_function)
    assert result == "Hello, World!"
