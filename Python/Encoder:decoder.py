#encryption using the ascii code


msg = input("Enter a message to encrypt: ") #Asking for input
encmsg = "" #Transfering input to variable 'encmsg'
for ch in msg: #Looping through each character in encrypted message
    asc = ord(ch) + 3 
    ench = chr(asc)
    encmsg += ench
encmsg= encmsg[::-1]
print("The encrypted message is:",encmsg)




