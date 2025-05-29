def ChkPrime(iNo):
    stop = int(iNo / 2)
    bFlag = True
    for i in range(2, stop + 1):
        if((iNo % i) == 0):
            bFlag = False
    
    return bFlag

