#hexstring.py em
def bincon(decimal):
    print("decimal")
    print("bin ********")
    binstr="" #binstr is a string
    for i in range(8):
        bin = decimal % 2
        decimal = decimal // 2
        #print (bin)
        binstr = binstr + str(bin)
        #print(binstr)
    print("-----")
    print(binstr)[::-1]

def hexcon(decimal):
    print(decimal)
    print(" HEX ********")
    # dividend/divisor=quotient
    hexstr = ""
    #----------------------------
    remainder = decimal % 16
    if (remainder == 10):
        
