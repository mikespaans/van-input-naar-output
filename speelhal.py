ToegangsPrijs = int(input('Hoeveel kost de entreeprijs '))
ToegangsPersonen = int(input('Hoeveel personen gaan er naar binnen '))
VipGameSeatPrijs = float(input('Hoeveel kost de Vip Game Seat per 1 minuut '))
VipGameSeatDuur = int(input('Hoelang wordt er in de Vip Game Seat gezeten '))
VipGameSeatPersonen = int(input('Met hoeveel personen wordt er in de Vip Game seat gezeten '))
TotalToegangsPrijs = ToegangsPrijs * ToegangsPersonen
TotalVipGameSeat = VipGameSeatDuur * VipGameSeatPrijs * VipGameSeatPersonen
print( str(TotalVipGameSeat) + str(TotalToegangsPrijs) + " cent ")