import math

class Converter:
    def __init__(self):
        self.__from_dec = True
        self.__base = 2
        self.__bits = 16
        self.__chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    
    def main(self):
        inp = ""
        while inp not in ["x", "b", "n", "t"]:
            if not inp == "":
                print(str(self.convert(inp)))
            promt = f"\nBase: {self.__base}\nBits: {self.__bits}\n" + self.__from_dec*"From Decimal" + (1-self.__from_dec)*"To Decimal" + "\n: "
            inp = input(promt)
    
        if inp == "b":
            self.change_base()
        if inp == "n":
            self.change_bits()
        if inp == "t":
            self.toggle_mode()
        
    def change_base(self):
        inp = 0
        while int(inp) not in range(2, 17):
            inp = input("Base: ")
        self.__base = inp
        self.main()
    
    def change_bits(self):
        inp = 0
        while int(inp) <= 1:
            inp = input("Base: ")
        self.__base = inp
        self.main()
        
    def toggle_mode(self):
        self.__from_dec = not self.__from_dec
        self.main()

    def convert(self, inp):
        if not self.__from_dec:
            if str(inp)[0]=

            '''
            negative = (str(inp)[0] == "-")
            if negative:
                inp = int(str(inp)[1:])
            for digit in str(inp):
            '''
        
        
        return ans
        

            



'''
def main():
    
   
    inp = ""
    
    while inp not in ["x", "b", "n", "t"]:
        promt = f"Base: {BASE}\nBits: {BITS}\n" + FROM_DEC*"From Decimal" + (1-FROM_DEC)*"To Decimal" + "\n: "
        inp = input(promt)
    
    if inp == "b":
        change_base()
    if inp == "n":
        change_bits()
    if inp == "t":
        toggle_mode()
    

def change_base():
    inp = 0
    while int(inp) not in range(2, 17):
        inp = input("Base: ")
    BASE = inp
    main()
    
def change_bits():
    return input("Bits: ")
    main()
    
def toggle_mode(from_dec):
    if from_dec:
        from_dec = False
    else:
        from_dec = True
    return from_dec
    main()
    
main()'''

Converter = Converter()
Converter.main()

'''
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
        
'''