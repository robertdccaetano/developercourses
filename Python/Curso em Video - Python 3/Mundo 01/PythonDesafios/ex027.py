nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
dividido = nome.split()
print('Seu primeiro nome é {} '.format(dividido[0]))
print('Seu último nome é {} '.format(dividido[len(dividido) - 1]))
