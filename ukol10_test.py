import pytest


from ukol2_oprava import usernames

def test_ukol2_basic():

    data = {

    "students":["Adam Levine", "Monica Muller", "John Deere", "John Deere", "Adam Peichl", "Martin Novak", "Michal Kuchař", "John Deere"],
    "active":[True, False, True, True, True, False, True, True]

    }

    data_new = usernames(data)
    assert data_new == ['levinada', 'deerejoh', 'deerejo2', 'peichada', 'kuchamic', 'deerejo3']