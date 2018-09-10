'''
Maria Cecilia Barbosa de Almeida
'''
futebol=('Flamengo','São Paulo','Internacional','Grêmio','Atlético MG','Palmeiras',
         'Corinthians','Cruzeiro','Fluminense','América MG','Botafogo','Vasco','Sport','Vitória','Chapecoense','Santos','Bahia','Atlético PR','Paraná','Ceará')
cinco= futebol[:5]
print('Os 5 primeiros colocados são:',cinco)

ultimos= futebol[-4:]
print('Os 4 últimos colocados são:',ultimos)

alfa=sorted(futebol)
print('Os times em ordem alfabetica:',alfa)

posi=(futebol.index('Chapecoense'))+1
print('A posição do time Chapecoense é',posi)
