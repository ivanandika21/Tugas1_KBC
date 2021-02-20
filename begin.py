dic = {
    'a' : ['g', 'z'],
    'g' : ['r', 'l', 'u'],
    'z' : ['t'],
    'l' : ['o', 'q']
}

initVar = 'a'

# contoh
# saiki = [z, l, u, t]
# [a, g, z]

def yoks(inittial, diccc):
    uwis = []
    saiki = [inittial]

    while saiki:
        nodeSaatIni = saiki.pop(0)
        if nodeSaatIni not in uwis:
            uwis.append(nodeSaatIni)
        if nodeSaatIni in diccc:
            for anak in diccc[nodeSaatIni]:
                saiki.append(anak)
    return uwis

def mainnn():
    lis = [i for i in input().split()]
    print(lis)

if __name__ == "__main__":
    print(yoks(initVar, dic))