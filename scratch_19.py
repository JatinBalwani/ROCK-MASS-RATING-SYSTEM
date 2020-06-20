print('*****ROCK MASS RATING SYSTEM CALCULATOR*****')
a1 = input('Enter Uniaxial Compressive Strength(MPa) = ')
a = int(a1)
if a > 250:
    r1 = 15
elif (a > 100) and (a <= 250):
    r1 = 12
elif (a > 50) and (a <= 100):
    r1 = 7
elif (a > 25) and (a <= 50):
    r1 = 4
elif (a > 5) and (a <= 25):
    r1 = 2
elif (a > 1) and (a <= 5):
    r1 = 1
else:
    r1 = 0
# print(r1,'Rating for Uniaxial Compressive Strength(MPa)')

# 2
b1 = input('Enter Drill Rock Quality[RQD](%) = ')
b = int(b1)
if (b > 90) and (b <= 100):
    r2 = 20
elif (b > 75) and (b <= 90):
    r2 = 17
elif (b > 50) and (b <= 75):
    r2 = 13
elif (b > 25) and (b <= 50):
    r2 = 8
elif (b <= 25):
    r2 = 3
# print(r2,'Rating for Drill Rock Quality[RQD](%)')

# 3
c1 = input('Enter Spacing of Discontunities(mm) = ')
c = int(c1)
if c > 2000:
    r3 = 20
elif (c > 600) and (c <= 2000):
    r3 = 15
elif (c > 200) and (c <= 600):
    r3 = 10
elif (c > 60) and (c <= 200):
    r3 = 8
elif (c <= 25):
    r3 = 5
# print(r3,'Rating for Spacing of Discontunities(mm)')

# 4
print('*Find the condition of discontinuities and fill the number written in front of them in the response:')
print('*Very rough surfaces Not continuous of discontinuities No separation Unweathered wall rock ~ 5')
print('*Slightly rough surfaces Separation <1 mm Slightly weathered walls ~ 4')
print('*Slightly rough surfaces Separation < 1 mm Highly weathered wals ~ 3')
print('*Slickensided surface or Gouge <5 mm thick or Separation 1-5 mm Continuous ~ 2')
print('*Soft gouge >5 mm thick or Separation > 5 mm Continuous ~ 1')
d1 = input('Enter Number Assigned to Condition of Discontunities = ')
d = int(d1)
if d == 5:
    r4 = 30
elif d == 4:
    r4 = 25
elif d == 3:
    r4 = 20
elif d == 2:
    r4 = 10
elif d == 1:
    r4 = 0
# print(r4,'Rating for Number Assigned to Condition of Discontunities')

# 5
print('Find the General Conditions of Ground Water and Enter them in the response:')
print('*Compeletly Dry')
print('*Damp')
print('*Wet')
print('*Dripping')
print('*Flowing')
e1 = input('Enter the General Conditions of Ground Water = ')
# e = int(e1)
e = e1.lower()
if e == 'completely dry':
    r5 = 15
elif e == 'damp':
    r5 = 10
elif e == 'wet':
    r5 = 7
elif e == 'dripping':
    r5 = 4
elif e == 'flowing':
    r5 = 0
else:
    print('Groundwater Condition cannot be identified')
# ALL ratings for checking
print('ALL RATINGS ACCORDING TO DATA ENTERED -')
print(r1, 'Rating for Uniaxial Compressive Strength(MPa)')
print(r2, 'Rating for Drill Rock Quality[RQD](%)')
print(r3, 'Rating for Spacing of Discontunities(mm)')
print(r4, 'Rating for Number Assigned to Condition of Discontunities')
print(r5, 'Rating for General Conditions of Ground Water')
print("GIVEN SAMPLE IS A-")

r = r1 + r2 + r3 + r4 + r5
#print(r)
if (r == 100) and (r < 81):
    print('Very Good Rock')
elif (r > 61) and (r <= 80):
    print('Good Rock')
elif (r > 41) and (r <= 60):
    print('Fair Rock')
elif (r > 21) and (r <= 40):
    print('Poor Rock')
elif (r <= 21):
    print('Very Poor Rock')
