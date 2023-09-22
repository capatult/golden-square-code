import pytest
from lib.grammar_stats import *
GrammarStats = GrammarStats  # helps with pylance linter

def tests_can_create_grammar_stats_object():
    stats = GrammarStats()
    assert True

def test_check_a_grammatically_correct_string_passes():
    stats = GrammarStats()
    result = stats.check("Hello, world!")
    assert result == True

def test_check_text_starting_with_lowercase_letter_fails():
    stats = GrammarStats()
    result = stats.check("hello, world!")
    assert result == False

def test_check_text_ending_with_non_punctuation_character_fails():
    stats = GrammarStats()
    result = stats.check("Hello, world")
    assert result == False

def test_can_call_percentage_good_on_new_grammar_stats_instance():
    stats = GrammarStats()
    with pytest.raises(Exception) as e:
        stats.percentage_good()
    error_message = str(e.value)
    assert error_message == "No texts checked so far."

def test_one_incorrect_text_causes_percentage_good_to_return_0():
    stats = GrammarStats()
    stats.check("hello, world")
    # __ = stats.check("hello, world")
    assert stats.percentage_good() == 0

def test_one_correct_text_causes_percentage_good_to_return_100():
    stats = GrammarStats()
    stats.check("Hello, world!")
    assert stats.percentage_good() == 100

def test_one_each_of_correct_and_incorrect_gives_50_percent_good():
    stats = GrammarStats()
    stats.check("This one is correct.")
    stats.check("this one is incorrect")
    assert stats.percentage_good() == 50

def test_two_correct_and_one_incorrect_gives_67_percent_good():
    stats = GrammarStats()
    texts = [
        "First correct text.",
        "Second correct text.",
        "first incorrect text",
    ]
    for text in texts:
        stats.check(text)
    assert stats.percentage_good() == 67

def test_one_correct_and_two_incorrect_gives_33_percent_good():
    stats = GrammarStats()
    texts = [
        "First correct text.",
        "first incorrect text",
        "second incorrect text",
    ]
    for text in texts:
        stats.check(text)
    assert stats.percentage_good() == 33
