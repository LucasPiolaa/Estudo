n = input('Digite algo:')
print('{} é alfabético?'.format(n), n.isalpha())
print('{} é alfanumérico?'.format(n), n.isalnum())
print('{} é numerico?'.format(n), n.isnumeric())
print('{} é decimal?'.format(n), n.isdecimal())
print('{} tem espaços?'.format(n), n.isspace())
print('{} é minusculo?'.format(n), n.islower())
print('{} é maiusculo?'.format(n), n.isupper())


