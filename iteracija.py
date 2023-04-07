import random

def podvojitev():
    d = random.random() * 6
    return d

def harmonicnaVrsta(k,n):
    vsota = 0
    for i in range(k, n+1):
        vsota += 1 / i

    return vsota

def dvojnaIteracija(n):
    razdalja = 0
    for i in range(1, n+1):
        razdalja = harmonicnaVrsta(1,2**i)/2 - harmonicnaVrsta(1,2**(i-1))/2
        print(razdalja)

def prevozenaPot(st_postaj, gorivo):
    vsota = 0
    for i in range(0, st_postaj):
        delna_vsota = 0
        for j in range(0,i+1):
            delna_vsota += 1/(gorivo-j)
        vsota += delna_vsota
    return vsota


#print(prevozenaPot(7,8)+harmonicnaVrsta(1,8))
#print(prevozenaPot2(0,8))
#print((8+prevozenaPot(23,25) + harmonicnaVrsta(2,25)+(harmonicnaVrsta(1,8)-(harmonicnaVrsta(3,25)/2)))/8)
#print(harmonicnaVrsta(1,8))


print((prevozenaPot(5,8)+harmonicnaVrsta(4,8))/harmonicnaVrsta(4,8))
print((8 + prevozenaPot(24,25)+ harmonicnaVrsta(1,8))/8)
print((8+25 + prevozenaPot(66,67) + harmonicnaVrsta(1,25))/25)
print((8+25+67 +prevozenaPot(167,168) + harmonicnaVrsta(1,67))/67)
print((8+25+67 + 168 + prevozenaPot(403,404) + harmonicnaVrsta(1,168))/168)

def konkurencnoRazmerje(n):
    iteracije = [8,25]
    konkurencnoRazmerje = [3.652759, 3.987737]
    razdalje = [1.358929,1.907979]
    for i in range(2, n+1):
        gorivo = 4 * iteracije[i-1] - sum(iteracije)
        razdalje += [harmonicnaVrsta(1,gorivo) /2]
        konkurencnoRazmerje += [round(((sum(iteracije)+ prevozenaPot(gorivo-1,gorivo)+harmonicnaVrsta(1,iteracije[i-1]))/iteracije[i-1]),6)]
        iteracije += [gorivo]
    return iteracije, razdalje, konkurencnoRazmerje

#print(konkurencnoRazmerje(9))
#print(dvojnaIteracija(9))
print((prevozenaPot(1,2)+0.5)/0.5)
def konkurencnoRazmerjeDvojna(n):
    iteracije = [1]
    konkurencnoRazmerje = []
    razdalje = [0.5]
    dodanaRazdalja = [0]
    for i in range(1, n+1):
        gorivo = 2 * iteracije[i-1]
        razdalje += [round((harmonicnaVrsta(1,gorivo) /2),6)]
        konkurencnoRazmerje += [round(((sum(iteracije)+ prevozenaPot(gorivo-1,gorivo)+harmonicnaVrsta(1,iteracije[i-1]))/iteracije[i-1]),6)]
        iteracije += [gorivo]
        dodanaRazdalja += [round(razdalje[i]-razdalje[i-1],6)]
    return iteracije, razdalje, konkurencnoRazmerje, dodanaRazdalja
print(konkurencnoRazmerjeDvojna(12))

