chiffres = []
lettres = []

with open('fichier') as f:
    lignes = f.readlines()

print(lignes)

for l in lignes:
    ligneSplit = l.split()
    print(ligneSplit)
    print(ligneSplit[0])
    print(ligneSplit[1])
    chiffres.append(ligneSplit[0])
    lettres.append(ligneSplit[1])

print(chiffres)
print(lettres)
