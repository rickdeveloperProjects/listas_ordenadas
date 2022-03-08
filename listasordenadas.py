#listas ordenadas
#trabalho ciclo 2 Estrutura de Dados 

lista = []
for n in range (0, 5):
    valor = int(input('Digite um valor: '))
    if n == 0 or valor > lista[-1]:
        lista.append(valor)
    else: 
        pos = 0 
        while pos < len(lista): 
            if valor <= lista[pos]: 
                lista.insert(pos, valor)
                break
            pos += 1
print ('-=' * 30)
print (f'Os valores digitados ordenados foram: {lista}')
