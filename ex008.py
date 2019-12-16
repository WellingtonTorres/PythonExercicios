d = float(input('Distância em metros: '))

km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d * 1000
print('A medida de {:.1f}m corresponde a:'.format(d))
print(' {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'.format(km, hm, dam, dm, cm, mm))
