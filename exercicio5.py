'''
Maria Cecilia Barbosa de Almeida
'''
notas = (' Matemática', 17.5,'Física', 21, 'Portugues',22.9,'História',25,'Geografia',24.2,'Química',29,'Biologia',20.3,
         'Inglês',22.3,'Espanhol',24.9,'Filosofia',18,'Sociologia',26,'Educação Física',19.2)
print('-'*40)
print('{:*^40}'.format('Boletim Escolar'))
for x in notas:
  if notas.index(x)%2 ==0:
        nome = notas[notas.index(x)]
        nota= notas[notas.index(x)+1]
        print('{:.<35}{:>5}'.format('Matemática','17.5'))
        print('{:.<35}{:>5}'.format('Física','21'))
        print('{:.<35}{:>5}'.format('Português','22.9'))
        print('{:.<35}{:>5}'.format('História','25'))
        print('{:.<35}{:>5}'.format('Geografia','24.2'))
        print('{:.<35}{:>5}'.format('Química','29'))
        print('{:.<35}{:>5}'.format('Biologia','20.3'))
        print('{:.<35}{:>5}'.format('Inglês','22.3'))
        print('{:.<35}{:>5}'.format('Espanhol','24.9'))
        print('{:.<35}{:>5}'.format('Filosofia','18'))
        print('{:.<35}{:>5}'.format('Sociologia','26'))
        print('{:.<35}{:>5}'.format('Educação Física','19.2'))
        
