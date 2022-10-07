dogru_sifre = 1234;

while True:
    sifre = input("Lutfen pin kodu daxil edin")
    if (sifre =="q"):
        print("Proqramdan cixilir")
        break
    try:
        sifre=int(sifre)
    except ValueError:
        print("Lutfen reqem girin")
    finally: 

        if sifre == dogru_sifre:
            print(
                """
                Bankomat
      
                Proqramdan cixmaq istedikde "q" ya basin
      
                Proses:
                        1-Pul sorgula
                        2-Pul yatirma
                        3-Pul cekme
                        """
                    )
            hesabdakipul = 1000
            while True:
                proses = input("Prosesi daxil edin")
    
                if (proses =="q"):
                    print("Proqramdan cixilir")
                    break
    
                elif (proses == "1"):
                    print(hesabdakipul)
    
                elif (proses=="2"):
                    mebleg = int(input("Yatirmag istediyiniz meblegi girin"))
                
                    hesabdakipul = hesabdakipul + mebleg
                    print(hesabdakipul)
        
                elif (proses=="3"):
                    mebleg = int(input("Cekmek istediyiniz meblegi girin"))
                    hesabdakipul=hesabdakipul-mebleg
                    if hesabdakipul<0:
                        print("Hesabinizda yeterli mebleg yoxdur")
                        hesabdakipul=hesabdakipul+mebleg
                    
                else:
                    print("Prosesi duzgun girin")

            else:
                    print("Lutfen sifreni duzgun girin")
               
        