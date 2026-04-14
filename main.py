import random
import math

proizvodi = [
    "Laptop",
    "Mis",
    "Tastatura",
    "Kamera",
    "USB",
    "Stampac",
    "Monitor",
    "Slusalice"
]

cene = {
    "Laptop": 950.99,
    "Mis": 19.99,
    "Tastatura": 42.50,
    "Kamera": 67.59,
    "USB": 11.49,
    "Stampac": 135.20,
    "Monitor": 220.00,
    "Slusalice": 58.99
}

print("Dostupni proizvodi i njihove cene:")
for proizvod in proizvodi:
    print(f"- {proizvod} - {cene[proizvod]:.2f} €")

budzet = float(input("\nUnesite vas budzet: "))

print("\nProizvodi koje mozete da kupite u okviru tog budzeta:")
ima = False

for proizvod in proizvodi:
    if cene[proizvod] <= budzet:
        print(f"- {proizvod} - {cene[proizvod]:.2f} €")
        ima = True

if not ima:
    print("Nema nijedan proizvod u okviru vaseg budzeta.")

def najskuplji_proizvod(recnik_cena):
    return max(recnik_cena, key=recnik_cena.get)

najskuplji = najskuplji_proizvod(cene)
print(f"\nNajskuplji proizvod je: {najskuplji} - {cene[najskuplji]:.2f} €")

nasumican_proizvod = random.choice(proizvodi)
print(f"\nKorisniku je privukao paznju proizvod: {nasumican_proizvod}")

zbir_cena = sum(cene.values())
prosecna_cena = zbir_cena / len(cene)
prosecna_cena = math.floor(prosecna_cena * 100 + 0.5) / 100

print(f"\nProsecna cena svih proizvoda je: {prosecna_cena:.2f} €")

prodati_komadi = [5, 20, 12, 7, 10, 8, 30, 4]

ukupan_prihod = 0
for i in range(len(proizvodi)):
    ukupan_prihod += cene[proizvodi[i]] * prodati_komadi[i]

print(f"\nUkupan prihod od prodaje svih proizvoda je: {ukupan_prihod:.2f} €")

novi_proizvod = "Tablet"
nova_cena = 299.99

proizvodi.append(novi_proizvod)
cene[novi_proizvod] = nova_cena

print("\nAzurirana lista proizvoda:")
for proizvod in proizvodi:
    print(f"- {proizvod}")

sortirani = sorted(cene.items(), key=lambda x: x[1])

print("\nProizvodi sortirani po ceni:")
for proizvod, cena in sortirani:
    print(f"- {proizvod} - {cena:.2f} €")