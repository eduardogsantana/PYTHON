# Set - CONJUNTOS.

set01 = set('Eduardo')
print(set01)
set02 = {'João', 'Eduardo', 'Gomes', 'Santana'}
print(set02)
set02.add('Elvis')
print(set02)
print('Eduardo' in set02)
print('Chefe' not in set02)
set02.update('Eduardo')
print(set02)



set03 = {1,2,3,4,5}
set04 = {4,5,6,7,8}

set05 = set03 | set04 #União de Conjuntos
print(set05)
set05 = set03 & set04 #Interseção de Conjuntos
print(set05)
set05 = set03 - set04 #Diferença de Conjuntos
print(set05)