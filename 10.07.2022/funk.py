def toplama(m,n):
    return m+n

def cixma(m,n):
    return m-n

def vurma(m,n):
    return m*n

def tambolme(m,n):
    return m//n

def qaliqlibolme(m,n):
    return m/n

def quvvet(m,n):
    return m*n

def ebob(m,n):
    
    if n == 0:
        return m
    else:
        return ebob(n,m%n)
    
    m = int(input("Ebob Birinci ededi girin"))
    n = int(input("Ebob Ikinci ededi girin"))

    print(ebob(m, n))

def ekob(m,n):
   if m > n:
       boyuk = m
   else:
       boyuk = n

   while(True):
       if ((boyuk % m == 0) and (boyuk % n == 0)):
           ekobb = boyuk
           break
       boyuk += 1

   return ekobb

def fakt(m,n):
    x = m+n
    sayi = 1
    while x > 1:
        sayi = sayi * x
        x-=1
    return sayi

