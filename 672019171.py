
# Ivan Andika Surya 672019171
# 20 Februari 2020
import numpy as np

graf = {
    'A' : ['B', 'C', 'D'],
    'B' : ['E', 'F', 'G', 'H'],
    'F' : ['O', 'P', 'Q'],
    'G' : ['R', 'S'],
    'C' : ['I', 'J', 'K'],
    'K' : ['T'],
    'D' : ['L', 'M', 'N'],
    'M' : ['U'],
}

initVar = 'A'

def tampung(inittial, dari_graf):
    sudah = []
    sedang = [inittial]

    while sedang:
        nodeSaatIni = sedang.pop(0)
        if nodeSaatIni not in sudah:
            sudah.append(nodeSaatIni)
        if nodeSaatIni in dari_graf:
            for node in dari_graf[nodeSaatIni]:
                sedang.append(node)
    return sudah

def mainnn():
    i = 0
print("\nIvan Andika Surya 672019171\n")

if __name__ == "__main__":
    print('Vertexlist : ', end=(' '))
    print(tampung(initVar, graf))

my_array = np.array(tampung(initVar, graf))
tujuan = input('\nMasukkan node tujuan : ')

for i in range(1, len(tampung(initVar, graf))+1):
    print('urutan ke', i, end=('\t>> '))

    if tujuan in my_array[i-1]:
        print('Pencarian berhenti, node saat ini adalah tujuan yaitu', end=(' '))
        print(my_array[i-1]+'\n')
        break
    print(my_array[i-1])

if tujuan not in my_array[i-1]:
    print('Pencarian berhenti, tujuan tidak ditemukan!\n')

