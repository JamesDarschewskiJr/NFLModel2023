import csv

data = []
with open('NFL Relative Strength v3 - 2023.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for line in reader:
        data.append(line)

data = data[1:]

cardinals = data[0]
falcons = data[1]
ravens = data[2]
bills = data[3]
panthers = data[4]
bears = data[5]
bengals = data[6]
browns = data[7]
cowboys = data[8]
broncos = data[9]
lions = data[10]
packers = data[11]
texans = data[12]
colts = data[13]
jaguars = data[14]
chiefs = data[15]
raiders = data[16]
chargers = data[17]
rams = data[18]
dolphins = data[19]
vikings = data[20]
patriots = data[21]
saints = data[22]
giants = data[23]
jets = data[24]
eagles = data[25]
steelers = data[26]
niners = data[27]
seahawks = data[28]
buccaneers = data[29]
titans = data[30]
commanders = data[31]

def win_probability(a, b):
    if a > b:
        a *= 100
        print('Win Probability: ' + format(a,'.1f') + '%')
    elif b > a:
        b *= 100
        print('Win Probability: ' + format(b, '.1f') + '%')
    else:
        print('Win Probability: 50%')

def moneyline(a,b):
    if a > b:
        x = b/a
    elif b > a:
        x = a/b
    else:
        x = 1.0
    if x >= 1.0:
        m = int(100 * x)
        ml = '+' + str(m)
        return ml
    else:
        ml = int(-1 * (100/x))
        return str(ml)


def matchup(teama, teamb):
    totalstrength = int(teama[1]) + int(teamb[1])
    srsa = int(teama[1])/totalstrength
    srsb = int(teamb[1])/totalstrength
    a = (float(teama[2]) + float(teama[3]) + float(teamb[2]) + float(teamb[3]))/2
    x = srsa * a
    y = srsb * a
    x1 = (100 + float(teama[4]) + float(teamb[5]) - float(teama[5]))/100
    y1 = (100 + float(teamb[4]) + float(teama[5]) - float(teamb[5]))/100
    score1 = x * x1
    score2 = (y * y1) + 3
    away = teama[0] + ': ' + str(round(score1))
    home = teamb[0] + ': ' + str(round(score2))
    print(away)
    print(home)
    if srsa > srsb:
        print('Predicted Favorite: ' + teama[0])
        win_probability(srsa, srsb)
        print('Suggested Moneyline: ' + moneyline(srsa, srsb))
    elif srsb > srsa:
        print('Predicted Favorite: ' + teamb[0])
        win_probability(srsa, srsb)
        print('Suggested Moneyline: ' + moneyline(srsa, srsb))
    else:
        print('Toss Up')
        win_probability(srsa, srsb)
        print('Suggested Moneyline: ' + moneyline(srsa, srsb))
    print()

matchup(chiefs, ravens)
matchup(lions, niners)

# matchup(niners, ravens)