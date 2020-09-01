
from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_multi_bracket_validation():
    actual=multi_bracket_validation('[][[]]')
    expected=True
    assert expected==actual

def test_multi_bracket_validation_2():
    actual=multi_bracket_validation('[{{hello}]')
    expected='error unmatched opening { remaining.'
    assert expected==actual




def test_multi_bracket_validation_3():
    actual=multi_bracket_validation('[{{hello}}}]')
    expected='error unmatched closing }'
    assert expected==actual

def test_multi_bracket_validation_4():
    actual=multi_bracket_validation('[{{mu name}is yazan]}]')
    expected='error unmatched closing ]'
    assert expected==actual




def test_multi_bracket_validation_5():
    actual=multi_bracket_validation('([{{mu name}is yazan]}]')
    expected='error unmatched opening ( remaining.'
    assert expected==actual



def test_multi_bracket_validation_6():
    actual=multi_bracket_validation('([{{mu name}is yazan]}]))')
    expected='error unmatched closing )' 
    assert expected==actual
