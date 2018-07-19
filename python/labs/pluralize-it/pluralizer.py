x = input("Give me a number: ")
y = input ("Give me a word: ")
out = "Output: "+str(x)+" "+str(y)

if x == 0 or x > 1:
    if y[-2:] ==('ly'):
        out = out [:-1]+'ies'
    elif y[-2:] == "us":
        out = out[:-2]+"i"
    elif y[-2:] == "sh" or y[-2:] == "ch":
        out += "es"
    else:
        out +="s"
    
print (out)
