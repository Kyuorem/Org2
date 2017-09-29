import struct
import sys

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColuna = 5

if (sys.argv) != 2:
	tam = 10000
else:
	tam = sys.argv[1]

arquivo = 699307
reg = (arquivo/tam)

lis1 = []

for i in range(0, reg):
	lis1.append(tam)

if (reg * tam != arquivo):
	reg += 1
	lis1.append(arquivo - (reg * tam))	

f = open("cep.dat", "r")
f2 = open("newfile.txt", "w")

line = f.read(registroCEP.size)
j = 0
data = []
while j < arquivo:
	linha = registroCEP.unpack(line)
	data.append([linha[cepColuna], j * 300])
	line = f.read(registroCEP.size)
	j+=1


k = 0


while k < reg:
	print k
	lisord = []
	u = 0	
	while u < lis1[k]: 
		lisord.append(data[u + (k * tam)])
		u+=1
	lisord.sort()
	quase = 0
	while quase < lis1[k]:
		#print (lisord[quase])[1]
		f.seek((lisord[quase])[1])
		linha = f.read(registroCEP.size)
		f2.write(linha)
		quase += 1
	k+=1

print "CABO"

"""
Vou escrever o que eu preciso
	1. Abrir o arquivo
	2. Armazenar em uma outra lista tudo da linha
	3. Ordenar os blocos
	4. Armazenar os blocos ordenados em f2
	5. Pensar na possibilidade de escrever "r+" 


"""
