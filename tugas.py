import numpy as np

i = 0
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
            for anak in dari_graf[nodeSaatIni]:
                sedang.append(anak)
    return sudah

def mainnn():
    gatau = 0
print("Ivan Andika Surya 672019171")

if __name__ == "__main__":
    print(tampung(initVar, graf))

my_array = np.array(tampung(initVar, graf))

for i in range(1, len(tampung(initVar, graf))+1):
    print('urutan ke', i, end=("\t>> ")),
    print(my_array[i-1])

print("\n")