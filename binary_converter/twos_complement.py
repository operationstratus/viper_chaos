import math
base = 2
bit = 3


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
        val = (base**bit -1)-val+1
        #print("2. val = " + str(val))
    
    bin_val = ""

        
    
    for i in range(bit-1, -1, -1):
        #print("i = " + str(i))
        #print("val = " + str(val))
        step = base**i
        #print("step = " + str(step))
        if val >= step:
            bin_val += str(math.floor(val/step))
            #print("bin_val = " + str(bin_val))
            val -= step
        else:
            bin_val += "0"
            #print("bin_val = " + str(bin_val))
        
    return bin_val
    
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
    inp = input("base = " + str(base) + " with " + str(bit) + " bits. Convert from " + dec_to_bin*"decimal to binary" + (1-dec_to_bin)*"binary to deciaml" + ": ")
    
    if inp.lower() == "b":
        inp = 0
        while not int(inp) in [2, 3, 4, 5, 6, 7, 8, 9, 10, 16]:
            inp = input("base: ")
        base = int(inp)
    elif inp.lower() == "n":
        bit = int(input("bits: "))
    elif inp.lower() == "t":
        dec_to_bin = not dec_to_bin
    
    elif dec_to_bin and not inp.lower() == "x":
        print(twos_complement(inp))
        
    elif not dec_to_bin and not inp.lower() == "x":
        print(decimal_val(inp))
        
    