n = input('Digite algo para analisar: ')
print('Seu tipo é:', type(n))

print('"{}" é alphanumerico ? '.format(n), n.isalnum())
print('"{}" é alphabético ? '.format(n), n.isalpha())
print('"{}" é decimal ? '.format(n), n.isdecimal())
print('"{}" é digito ? '.format(n), n.isdigit())
print('"{}" é tudo maiúsculo ? '.format(n), n.isupper())
print('"{}" é Capitalizada/Mai|Min ? '.format(n), n.istitle())
print('"{}" é tudo minúsculo ?'.format(n), n.islower())
print('"{}" é printável ? '.format(n), n.isprintable())
print('"{}" é indentificável ? '.format(n), n.isidentifier())
print('"{}" é espaçável ? '.format(n), n.isspace())
