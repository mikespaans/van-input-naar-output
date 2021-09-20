PrijsCroissantjes = int(input('Wat is de prijs van een croissantje '))
HoeveelheidCroissantjes = int(input('Hoeveel croissantjes heb je '))
PrijsStokbroden = int(input('Wat is de prijs van een stokbrood '))
HoeveelheidStokbroden = int(input('Hoeveel stokbroden heb je '))
Kortingsbon = int(input('Hoeveel korting geeft een kortingsbon '))
HoeveelKortingsbonnen = int(input('Hoeveel kortingsbonnen heb je '))
TotalCroissantjes = PrijsCroissantjes * HoeveelheidCroissantjes
TotalStokbroden = PrijsStokbroden * HoeveelheidStokbroden
TotalKortingsbon = Kortingsbon * HoeveelKortingsbonnen
TotalEten = TotalCroissantjes + TotalStokbroden
TotalBedrag = TotalEten - TotalKortingsbon
print( str(TotalBedrag) + " cent " )