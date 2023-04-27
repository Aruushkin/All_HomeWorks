Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
del Geeks['bag']
Geeks['address'] = 'Ibraimova 103'
Geeks['number'] = '0507052018'
Geeks['instagram'] = 'geeks_edu'
new_courses = ['IOS', 'UX/UI', 'english courses', 'design courses', 'manicurist', 'drawing', 'massage']
print(set(new_courses))
Geeks['date'] = '2018 year'
Geeks['courses'] = list(Geeks['courses'])
for i in new_courses:
    Geeks['courses'].append(i)
print(Geeks['courses'])
print(len(Geeks['courses']))

for k, v in Geeks.items():
    print(k, ':', v)
