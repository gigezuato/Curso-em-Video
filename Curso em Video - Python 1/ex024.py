cidade = ((str(input('Em que cidade você nasceu?:'))).lower()).strip()
c = cidade.split()
print('santo' in c[0])

# outra forma:
'''cid = str(input('Em que cidade você nasceu?)).strip()
    print(cid[:5].upper()) == 'SANTO') '''
