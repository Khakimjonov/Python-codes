import os
os.system("cls")
from datetime import datetime
while 1:
    
  tugilgan_yil = input("tug'ilgan yilingizni kiriting :  ")
  Bugun = datetime.today()
  natija = Bugun.year- int(tugilgan_yil)
  print(" Hozir Sizning yoshingiz  - " , natija , "da")
else:
    print("Sizga berilgan miqdor tugadi")
    break
