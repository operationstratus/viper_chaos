import math
base = 2
bit = 8
# Negative Binary representation


# 0. Unsigned form
#------------------------

def unsigned_form(x):

    
    dec = str(x)
    if dec[0] == "-":
        val = int(dec[1:])
    else:
        val = int(dec)   
    bi = ""
    
    for i in range(bit - 2, -1, -1):
        step = base ** i
        if val >= step:
            bi +=  str(math.floor(val / step))
            val -= step
        else:
            bi += "0"
        print(i)
        print(bi)
    return bi

# 1. one's complement 
#---------------------

def ones_complement(x):
    neg = False
    dec = str(x)
    if dec[0] == "-":
        neg = True
        val = int(dec[1:])
        pm = "1"
    else:
        val = int(dec)
        pm = "0"
    
    bi = ""
    
    for i in range(bit - 2, -1, -1):
        step = base ** i
        if val >= step:
            bi +=  str(math.floor(val / step))
            val -= step
        else:
            bi += "0"
    if neg:
        bi2 = ""
        for dig in bi:
            if dig == "0":
                bi2 += "1"
            else:
                bi2 += "0"
        bi = bi2
    
    return pm + bi
        

# 2. two's complement 
#---------------------

def twos_complement(x):
    neg = False
    dec = str(x)
    if dec[0] == "-":
        neg = True
        val = int(dec[1:])-1
        #print(val)
        # minus one, since the negative binary number is the inverted version of [its decimal counterpart -1]
        pm = "1"
    else:
        val = int(dec)
        pm = "0"
    
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
    
    return pm + bi
        



# 3. Sign magnitude form
#------------------------
# Easy to convert manually, see right away wich numbers are positive and wich are negative
# Numbers in this form can't be added or subtracted'


def sign_magnitude_form(x):

    
    dec = str(x)
    if dec[0] == "-":
        pm = "1"
        val = int(dec[1:])
    else:
        val = int(dec)
        pm = "0"
    
    bi = ""
    
    for i in range(bit - 2, -1, -1):
        step = base ** i
        if val >= step:
            bi +=  str(math.floor(val / step))
            val -= step
        else:
            bi += "0"

    return pm + bi

# 4. binary to decimal

def bin_to_dec(x):
    x = str(x)
    dec = 0
    exp = 0
    for i in range(len(x)-1, -1, -1):
        if i == 0:
            dec -= int(x[i]) * base**exp
        else:
            dec += int(x[i]) * base**exp
        exp += 1
    return dec

'''
            
def to_binary():
    inp = input("Convert to two:s complement base " + str(base) + ", in " + str(bit) + " bits: ")
    while not str(inp).lower() == "x":
        if not str(inp).lower == "b":
            print(twos_complement(inp))
        

def to_decimal():
    inp = input("Convert from two:s complement base " + str(base) + " in " + str(bit) + " bits to decimal: ")
    while not str(inp).lower() == "x":
        if str(inp).lower == "b":
            menue()
            exit
        print(bin_to_dec(inp))
        
def menue():
    inp = input("dec, bin, x: ")
    while not str(inp).lower() == "x":
        if not str(inp).lower() == "x":
            if str(inp).lower() == "bin":
                to_binary()
            if str(inp).lower() == "dec":
                to_decimal()
            

'''

inp = ""
'''
while not str(inp).lower() == "x":
    inp = input("Convert to two:s complement base " + str(base) + ", in " + str(bit) + " bits: ")
    if not str(inp).lower() == "x":
        print(twos_complement(inp))'''

while not str(inp).lower() == "x":
    inp = input("Convert from two:s complement base " + str(base) + " in " + str(bit) + " bits to decimal:")
    if not str(inp).lower() == "x":
        print(bin_to_dec(inp))

#print(ones_complement(input("Convert to one:s complement base " + str(base) + ", in " + str(bit) + " bits: ")))
#print(sign_magnitude_form(input("Convert to sign magnitude form, base " + str(base) + ", in " + str(bit) + " bits: ")))
#print(unsigned_form(input("Convert to unsigned form, base " + str(base) + ", in " + str(bit) + " bits: ")))
