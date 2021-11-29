def lenkuParbaude(len1, len2, len3) :
 rezultats = False
 if len1 + len2 + len3 == 180:
   rezultats = True
   return rezultats 


Len1 = int(input("Īevadiet 1 lenki: "))
Len2 = int(input("Īevadiet 2 lenki: "))
Len3 = int(input("Īevadiet 3 lenki: "))
rez = lenkuParbaude(Len1, Len2, Len3)
if rez:  
 print("Trissturis eksiste!")
else:
 print("Trissturis neekste!")