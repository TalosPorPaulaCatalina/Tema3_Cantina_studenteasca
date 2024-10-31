meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]
tavi = ["tava"] * 7
istoric_comenzi = []

numar_comenzi = {"papanasi": 0, "ceafa": 0, "guias": 0}

preturi_comanda = {produs[0]: produs[1] for produs in preturi}

print("Procesarea comenzilor:")
while studenti and comenzi and tavi:
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    tava = tavi.pop()
    istoric_comenzi.append(comanda)
    numar_comenzi[comanda] += 1
    print(f"{student} a comandat {comanda}.")


print(f"S-au comandat {numar_comenzi['guias']} guias, {numar_comenzi['ceafa']} ceafa, {numar_comenzi['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")
print(f"Mai este ceafa: {'ceafa' in meniu and meniu.count('ceafa') - numar_comenzi['ceafa'] > 0}.")
print(f"Mai sunt papanasi: {'papanasi' in meniu and meniu.count('papanasi') - numar_comenzi['papanasi'] > 0}.")
print(f"Mai sunt guias: {'guias' in meniu and meniu.count('guias') - numar_comenzi['guias'] > 0}.")

print("\n3. Finanțe:")
incasari_totale = sum(preturi_comanda [comanda] for comanda in istoric_comenzi)
produse_ieftine = [produs for produs, pret in preturi_comanda.items() if pret <= 7]
print(f"Incasări totale: {incasari_totale} lei.")
print(f"Produse care costă cel mult 7 lei: {', '.join(produse_ieftine)}.")
