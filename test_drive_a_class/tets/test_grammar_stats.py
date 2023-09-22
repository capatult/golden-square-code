from lib.grammar_stats import *

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

