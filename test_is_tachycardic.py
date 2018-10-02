import pytest


@pytest.mark.parametrize("candidate,expected", [
    ('tachycardic', True),
    ('   tachycardic', True),
    ('tachycardic   ', True),
    ('TACHYCARDIC', True),
    ('.tachycardic', True),
    ('tachycardic.', True),
    ('Tachycardic', True),
    ('TachyCARDIC', True),
    ('TACHYcardic', True),
    ('Tachy.cardic', True),
    ('Tachy8..8 cardic', True),
    ('     Tachy    cardic', True),
    ('Tachycard....ic', True),
    ('tach', False),
    ('mark', False),
    ('tachycar', False),
    ('TACHYcard', False),
])
def test_is_tachycardic(candidate, expected):
    from is_tachycardic import is_tachycardic
    assert is_tachycardic(candidate) == expected
