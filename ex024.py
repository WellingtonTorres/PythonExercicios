city = str(input('What city do you borne? or Where you were born? ')).upper()
city = city.split()
checker = str('SANTO')
if city[0] == checker:
     print('TRUE')
else:
    print('FALSE')
#print(city[0])
