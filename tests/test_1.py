import pytest

from main import ballance

@pytest.mark.parametrize(
    'a, expected',
    (
        ['(((([{}]))))',"Сбалансированно"],
        ['{{[(])]}}', "Несбалансированно"],
     )
)

def test_ballance(a, expected):
    actual = ballance(a)
    assert actual == expected