echipa = ["Jucator1", "Jucator2", "Jucator3", "Jucator4", "Jucator5"]
schimbari_efectuate = 0
schimbari_max = 3

jucator_iesit = "Jucator1"
jucator_intrat = "Jucator6"

if jucator_iesit in echipa and schimbari_efectuate < schimbari_max:
    echipa.remove(jucator_iesit)
    echipa.append(jucator_intrat)
    schimbari_efectuate += 1
    print(
        f"A intrat {jucator_intrat}, a ieșit {jucator_iesit}, mai ai {schimbari_max - schimbari_efectuate} schimbări.")
elif schimbari_efectuate >= schimbari_max:
    print("Ai atins numărul maxim de schimbări permise.")
else:
    print(f"Nu se poate efectua schimbarea deoarece jucătorul {jucator_iesit} nu e în teren.")
    print(f"Mai ai {schimbari_max - schimbari_efectuate} schimbari.")
