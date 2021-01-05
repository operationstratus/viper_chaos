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
    inp = int(inp)
    return inp <= BASE**(BIT-2) and inp >= -BASE**(BIT-1)
    

def bin_to_dec(x):
    x = str(x)
    dec = 0
    exp = 0
    for i in range(len(x)-1, -1, -1):
        if i == 0:
            dec -= int(x[i]) * BASE**exp
        else:
            dec += int(x[i]) * BASE**exp
        exp += 1
    return str(dec)

inp = ""
dec_to_bin = True
while not inp.lower() == "x":
    inp = input("BASE = " + str(BASE) + " with " + str(BIT) + " BITs. Convert from " + dec_to_bin*"decimal to binary" + (1-dec_to_bin)*"binary to deciaml" + ": ")
    
    if inp.lower() == "b":
        inp = 0
        while not int(inp) in [2, 3, 4, 5, 6, 7, 8, 9, 10, 16]:
            inp = input("base: ")
        BASE = int(inp)
    elif inp.lower() == "n":
        BIT = int(input("bits: "))
    elif inp.lower() == "t":
        dec_to_bin = not dec_to_bin
    
    elif dec_to_bin and not inp.lower() == "x" and inp_in_range(inp):
        print(twos_complement(inp))
        
    elif not dec_to_bin and not inp.lower() == "x" and inp_in_range(inp):
        print(bin_to_dec(inp))
    elif not inp_in_range(inp):
        print(str("number too small or too large"))
        
    