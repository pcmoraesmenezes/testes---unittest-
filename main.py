from calculator import sum

try:
    print(sum('10', 15))

except AssertionError as error:
    print(f'Invalid account: {error}')

print('\nInserting another exception:\n')

try:
    print(sum(10, '15'))

except AssertionError as error:
    print(f'Invalid account: {error}')

print('\nExceptions do not break the code ')
