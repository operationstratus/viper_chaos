import math
base = 2
bit = 8


def twos_complement(x):
    negative = False
    dec = str(x)
    if dec[0] == "-":
        negative = True
        
        val = int(dec[1:])
        val = len(val)*
        pm = "1"
    else:
        val = int(dec)
        pm = "0"
    
    binary = ""
    if negative:
        val 
    
    
    '''
    bi = ""
    
    
    for i in range(bit - 2, -1, -1):
        step = base ** i
        #print("Val: " + str(val) + ", step = " + str(step))
        if val >= step:
            bi +=  str(math.floor(val / step))
            #print(bi)
            val -= step
        else:
            bi += "0"
            #print(bi)
    if neg:
        bi2 = ""
        for dig in bi:
            if dig == "0":
                bi2 += "1"
            else:
                bi2 += "0"
        bi = bi2
        #print(bi)
    
    return pm + bi'''


inp = ""
dec_to_bin = True
while not inp.lower() == "x":
    inp = input("convert: ")
    
    if inp.lower() == "b":
        base = input("base: ")
    elif inp.lower() == "n":
        bits = input("bits: ")
    elif inp.lower() == "t":
        dec_to_bin = not dec_to_bin
    
    elif dec_to_bin and not inp.lower() == "x":
        twos_complement(inp)
        
    elif not dec_to_bin and not inp.lower() == "x":
        print("bin to dec")
        
    