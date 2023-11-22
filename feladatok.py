def elso():
    szamlalo:int = 0
    for i in range(1,1001,1):
        if i % 7 == 0:
            szamlalo+=1
    return szamlalo

def masodik():
    szamlalo:int =0
    for i in range(2000,20001,1):
        if i % 12 == 0:
            szamlalo +=1
    return szamlalo

def harmadik():
    osszeg:int = 0
    for i in range(3,61,3):
        osszeg+=i**2
    return osszeg

def negyedik(szam):
    print(f"A(z) {szam} osztói: ")
    for i in range(1,szam + 1,1):
        if szam % i == 0:
            if szam != i:
                print(i, end=", ")
            else:
                print(i, end="")

def hatodik(szam):
    primindex:int = 0
    prim:str = f"A(z) {szam} egy prímszám"
    nemprim:str = f"A(z) {szam} nem egy prímszám"

    for i in range(1,szam + 1,1):
        if szam % i == 0:
            primindex+=1
    
    if primindex == 2:
        return prim
    else:
        return nemprim
       
def hetedik():
    osszegzo:int = 0
    for i in range(1,100001,1):
        negyzetindex:float = i ** 0.5
        if negyzetindex % 1 == 0:
            osszegzo+=1

    return osszegzo

def nyolcadik():
    osszegzo:int = 0
    for i in range(10000,100001,1):
        negyzetindex:float = i ** 0.5
        if negyzetindex % 1 == 0:
            osszegzo+=1

    return osszegzo

def kilencedik():
    osszegzo:int = 0
    for i in range(0,10001,1):
        negyzetindex:float = i ** 0.5
        if negyzetindex % 1 == 0:
            osszegzo+=i

    return osszegzo
