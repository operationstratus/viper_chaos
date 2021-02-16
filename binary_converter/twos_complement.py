import math
BASE = 2
BIT = 5
HEXA = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]


def twos_complement(x):
    negative = False
    dec = str(x)
    if dec[0] == "-":
        negative = True
        
        val = int(dec[1:])
        #print("1. val = " + str(val))
    else:
        val = int(dec)
        #print("1. val = " + str(val))
    
    if negative:
        val = (BASE**BIT -1)-val+1
        #print("2. val = " + str(val))
    
    bin_val = ""

        
    
    for i in range(BIT-1, -1, -1):
        #print("i = " + str(i))
        #print("val = " + str(val))
        step = BASE**i
        #print("step = " + str(step))
        '''
        if val >= step:
            
            
            
                
            bin_val += HEXA[math.floor(val/step)]
            #print("bin_val = " + str(bin_val))
            val -= step * math.floor(val/step)
        else:
            bin_val += "0"
            #print("bin_val = " + str(bin_val))
        '''
        
        bin_val += HEXA[math.floor(val/step)]
        #print("bin_val = " + str(bin_val))
        val -= step * math.floor(val/step)
        
    return bin_val
    
    '''
    bi = ""
    
    
    for i in range(BIT - 2, -1, -1):
        step = BASE ** i
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

def inp_in_range(inp):
    if not inp == "x":
        inp = int(inp)
        return inp <= BASE**(BIT-2) and inp >= -BASE**(BIT-1)
    

def bin_to_dec(x):
    negative = False
    if HEXA.index(str(x)[0]) == BASE-1:
        print("HEXA obj = " + str(HEXA.index(str(x)[0])))
        negative = True
    dec = 0
    
    for i in range(len(x)-1, -1, -1):
        dec += HEXA.index(str(x)[i])*BASE**i
        print("i = " + str(i))
        print("digit = " + str(x)[i])
        print(str(HEXA.index(str(x)[i])*BASE**i))
    if negative:
        dec = BASE**(len(str(x))+1)
    return str(dec)



def get_bits(x):
    i = 0
    while x / BASE**i < 1:
        i += 1
    print(str(i+1))
        

inp = ""
dec_to_bin = True
while not inp.lower() == "x":
    inp = input("BASE = " + str(BASE) + " with " + str(BIT) + " BITs. Convert from " + dec_to_bin*"decimal to binary" + (1-dec_to_bin)*"binary to deciaml" + ": ")
    
    if inp.lower() == "b":
        inp = 0
        while not int(inp) in range(2, 17):
            inp = input("base: ")
        BASE = int(inp)
    elif inp.lower() == "n":
        BIT = int(input("bits: "))
    elif inp.lower() == "t":
        dec_to_bin = not dec_to_bin
    
    elif dec_to_bin and not inp.lower() == "x":
        if inp_in_range(inp):
            print(twos_complement(inp))
        
    elif not dec_to_bin and not inp.lower() == "x":
        print(bin_to_dec(inp))
    elif not inp_in_range(inp) and not inp.lower() == "x":
        print(str("number too small or too large"))
        
    