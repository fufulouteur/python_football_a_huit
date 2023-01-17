import random

effectif = ['Haalaud' 'R. Sanches' 'Rashford' 'Foden',
            'Chiesa', 'Ause Fati', 'Sane', 'Mount',
            'Coman', 'A.Arnold', 'Upamecano', 'brandt',
            'Rodrygo', 'De Ligt']
equipe_A = ['Pickford (CAP)']
equipe_B = ['Mbappe (CAP)']
print("*** Selection des joueur pour un foot a 8 ***")
while len(equipe_A) < 8:
    joueur_select = random.choice(effectif)
    equipe_A.append(joueur_select)
    effectif.remove(joueur_select)

equipe_B.extend(effectif)

print(F"Equipe de {equipe_A[0]} : ")
print(*equipe_A, sep=", ")

print(F"\nEquipe de {equipe_B[0]} : ")
print(*equipe_B, sep=", ")