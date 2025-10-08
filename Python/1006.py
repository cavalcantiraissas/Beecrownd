A = float(input(""))
B = float(input(""))
C = float(input(""))

NOTAA = A*2
NOTAB = B*3
NOTAC = C*5

MEDIA = (NOTAA + NOTAB + NOTAC) / 10 
MEDIA_FINAL = "{:.1f}".format(MEDIA)

print("MEDIA =", MEDIA_FINAL) 
