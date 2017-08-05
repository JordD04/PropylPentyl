# program that loops through integers from 0 to cap and states those numbers that can be divided by 3 and/or 5.

capString = input('Enter a Number to cap the search: ')
cap = int(capString)

print('Cap: ' + capString)

no = 1

while no < (cap+1):
    no3 = no / 3
    no3int = int(no3)
    no3dif = no3 - no3int

    no5 = no / 5
    no5int = int(no5)
    no5dif = no5 - no5int

    if no5dif == 0 and no3dif == 0:
        print(str(no) + ': ' + 'PropylPentyl')
    if no5dif == 0:
        print(str(no) + ': ' + 'Pentyl')
    if no3dif == 0:
        print(str(no) + ': ' + 'Propyl')
    pass

    no = no + 1

print('Done!')
