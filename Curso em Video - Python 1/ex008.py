m = float(input('Uma distância em metros:'))
km = m/1000
hm = m/100
dam = m/10
dm = m * 10
cm = m * 100
mm = m * 1000

print('A medida de {} metros corresponde a \n{:.0f}mm \n{:.0f}cm'.format(m, mm, cm))
print('{:.0f}dm \n{}dam \n{}hm \n{}km'.format(dm, dam, hm, km))
