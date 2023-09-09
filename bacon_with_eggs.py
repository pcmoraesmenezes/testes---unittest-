"""
Will recieve a number and check if the number is integer and
will check if number is multiple 3 and/or 5
"""


def bacon_with_eggs(integer):
    assert isinstance(integer, int), 'the number send must be integer'

    if integer % 3 == 0 and integer % 5 == 0:
        return 'Bacon with eggs'

    if integer % 3 == 0:
        return 'Bacon'

    if integer % 5 == 0:
        return 'Eggs'

    return 'Hungry'
