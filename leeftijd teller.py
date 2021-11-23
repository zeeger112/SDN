from statistics import mean
leeftijden =[18,22,20,19,21,22,22]
leeftijd =int(input('Geef leeftijd op :'))
leeftijden.append(leeftijd)


for ding in leeftijden:
    print('Leeftijd: '+ str(ding))
gem =  mean(leeftijden)
print('het gemiddelde is: '+ str(gem))
if gem < 20:
    print('Allemaal tieners?')
elif gem > 65:
    print('bejaardensoos')
else:
    print('Geen jongeren of Ouderen')