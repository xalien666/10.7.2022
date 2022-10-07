import funk as f

print("""
      Kalkulyator proqramina xos gelmisiniz
      -------------------------------------
      1- toplama
      2- cixma
      3- vurma
      4- tambolme
      5- qaliqlibolme
      6- quvvet
      7- ebob
      8- ekob
      9- faktoriyal
      """)

while True:
    m = input("birinci ededi daxil edin")
    n = input("ikinci ededi daxil edin")
    if (n =="q"):
        print("Proqramdan cixilir")
        break
    elif(m =="q"):
        print("Proqramdan cixilir")
        break
    
    try:
        m=int(m)
        n=int(n)
    except ValueError:
        print("Lutfen reqem girin")
    finally: 
        
        
        e=input("Emeliyyat novunu girin")
        if e=="1":
            print("Toplama emeliyyatinin neticesi:")
            print(f.toplama(m, n) )
             
        elif e=="2":
           print("Cixma emeliyyatinin neticesi:")
           print(f.cixma(m, n))
           
        elif e=="3":
           print("Vurma emeliyyatinin neticesi:")
           print(f.vurma(m, n))
           
        elif e=="4":
           print("Tam bolme emeliyyatinin neticesi:")
           print(f.tambolme(m, n))
           
        elif e=="5":
            print("Qaliqli bolme emeliyyatinin neticesi:")
            print(f.qaliqlibolme(m, n))
            
        elif e=="6":
            print("Quvvet emeliyyatinin neticesi:")
            print(f.quvvet(m, n))
            
        elif e=="7":
            print("Ebob emeliyyatinin neticesi:")
            print(f.ebob(m, n))
            
        elif e=="8":
            print("Ekob emeliyyatinin neticesi:")
            print(f.ekob(m, n))
            
        elif e=="9":
            print("Faktorial emeliyyatinin neticesi:")
            print(f.fakt(m, n))
        
       
        