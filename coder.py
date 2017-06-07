##Coding Decoding
codedWord=input('Enter the coded word:')
code=list(codedWord)
print(code)
codelen=len(code)   
print(codelen)
#for stp in range(codelen):
    #print(code[stp])
##

    
print(code)





for step in range(codelen):
    if code[step] == 'a':
        code[step] = 1
    elif code[step] == 'b':
        code[step] = 2
    elif code[step] == 'c':
        code[step] = 3
    elif code[step] == 'd':
        code[step] = 4
    elif code[step] == 'e':
        code[step] = 5
    elif code[step] == 'f':
        code[step] = 6
    elif code[step] == 'g':
        code[step] = 7
    elif code[step] == 'h':
        code[step] = 8
    elif code[step] == 'i':
        code[step] = 9
    elif code[step] == 'j':
        code[step] = 10
    elif code[step] == 'k':
        code[step] = 11
    elif code[step] == 'l':
        code[step] = 12
    elif code[step] == 'm':
        code[step] = 13
    elif code[step] == 'n':
        code[step] = 14
    elif code[step] == 'o':
        code[step] = 15
    elif code[step] == 'p':
        code[step] = 16
    elif code[step] == 'q':
        code[step] = 17
    elif code[step] == 'r':
        code[step] = 18
    elif code[step] == 's':
        code[step] = 19
    elif code[step] == 't':
        code[step] = 20
    elif code[step] == 'u':
        code[step] = 21
    elif code[step] == 'v':
        code[step] = 22
    elif code[step] == 'w':
        code[step] = 23
    elif code[step] == 'x':
        code[step] = 24
    elif code[step] == 'y':
        code[step] = 25
    elif code[step] == 'z':
        code[step] = 26


print(code)

#################
deCodedWord=input('Enter the Decoded Word:')
deCode=list(deCodedWord)
deCodeLen= len(deCode)
for step in range(codelen):
    if deCode[step] == 'a':
        deCode[step] = 1
    elif deCode[step] == 'b':
        deCode[step] = 2
    elif deCode[step] == 'c':
        deCode[step] = 3
    elif deCode[step] == 'd':
        deCode[step] = 4
    elif deCode[step] == 'e':
        deCode[step] = 5
    elif deCode[step] == 'f':
        deCode[step] = 6
    elif deCode[step] == 'g':
        deCode[step] = 7
    elif deCode[step] == 'h':
        deCode[step] = 8
    elif deCode[step] == 'i':
        deCode[step] = 9
    elif deCode[step] == 'j':
        deCode[step] = 10
    elif deCode[step] == 'k':
        deCode[step] = 11
    elif deCode[step] == 'l':
        deCode[step] = 12
    elif deCode[step] == 'm':
        deCode[step] = 13
    elif deCode[step] == 'n':
        deCode[step] = 14
    elif deCode[step] == 'o':
        deCode[step] = 15
    elif deCode[step] == 'p':
        deCode[step] = 16
    elif deCode[step] == 'q':
        deCode[step] = 17
    elif deCode[step] == 'r':
        deCode[step] = 18
    elif deCode[step] == 's':
        deCode[step] = 19
    elif deCode[step] == 't':
        deCode[step] = 20
    elif deCode[step] == 'u':
        deCode[step] = 21
    elif deCode[step] == 'v':
        deCode[step] = 22
    elif deCode[step] == 'w':
        deCode[step] = 23
    elif deCode[step] == 'x':
        deCode[step] = 24
    elif deCode[step] == 'y':
        deCode[step] = 25
    elif deCode[step] == 'z':
        deCode[step] = 26

print(deCode)
######
#print(code[0] + code[1] + code[2] + deCode[0] + deCode[1] + deCode[2])
pattren=[]
for steps in range(codelen):
    change=code[steps] - deCode[steps]
    pattren.append(change)

print(pattren)
###########
decodeddWord=input('Enter the decodedd Word:')
decoded=list(decodeddWord)
decodedLen= len(decoded)
for step in range(deCodeLen):
    if decoded[step] == 'a':
        decoded[step] = 1
    elif decoded[step] == 'b':
        decoded[step] = 2
    elif decoded[step] == 'c':
        decoded[step] = 3
    elif decoded[step] == 'd':
        decoded[step] = 4
    elif decoded[step] == 'e':
        decoded[step] = 5
    elif decoded[step] == 'f':
        decoded[step] = 6
    elif decoded[step] == 'g':
        decoded[step] = 7
    elif decoded[step] == 'h':
        decoded[step] = 8
    elif decoded[step] == 'i':
        decoded[step] = 9
    elif decoded[step] == 'j':
        decoded[step] = 10
    elif decoded[step] == 'k':
        decoded[step] = 11
    elif decoded[step] == 'l':
        decoded[step] = 12
    elif decoded[step] == 'm':
        decoded[step] = 13
    elif decoded[step] == 'n':
        decoded[step] = 14
    elif decoded[step] == 'o':
        decoded[step] = 15
    elif decoded[step] == 'p':
        decoded[step] = 16
    elif decoded[step] == 'q':
        decoded[step] = 17
    elif decoded[step] == 'r':
        decoded[step] = 18
    elif decoded[step] == 's':
        decoded[step] = 19
    elif decoded[step] == 't':
        decoded[step] = 20
    elif decoded[step] == 'u':
        decoded[step] = 21
    elif decoded[step] == 'v':
        decoded[step] = 22
    elif decoded[step] == 'w':
        decoded[step] = 23
    elif decoded[step] == 'x':
        decoded[step] = 24
    elif decoded[step] == 'y':
        decoded[step] = 25
    elif decoded[step] == 'z':
        decoded[step] = 26


#print(decoded)

#########
decodedword=[]
for steps in range(codelen):
    chng=decoded[steps] - pattren[steps]
    decodedword.append(chng)
print(decodedword) 

#################


for step in range(deCodeLen):
    if decodedword[step] == 1:
        decodedword[step] = "a"
    elif decodedword[step] == 2:
        decodedword[step] = "b"
    elif decodedword[step] == 3:
        decodedword[step] = "c"
    elif decodedword[step] == 4:
        decodedword[step] = "d"
    elif decodedword[step] == 5:
        decodedword[step] = "e"
    elif decodedword[step] == 6:
        decodedword[step] = "f"
    elif decodedword[step] == 7:
        decodedword[step] = "g"
    elif decodedword[step] == 8:
        decodedword[step] = "h"
    elif decodedword[step] == 9:
        decodedword[step] = "i"
    elif decodedword[step] == 10:
        decodedword[step] = "j"
    elif decodedword[step] == 11:
        decodedword[step] = "k"
    elif decodedword[step] == 12:
        decodedword[step] = "l"
    elif decodedword[step] == 13:
        decodedword[step] = "m"
    elif decodedword[step] == 14:
        decodedword[step] = "n"
    elif decodedword[step] == 15:
        decodedword[step] = "o"
    elif decodedword[step] == 16:
        decodedword[step] = "p"
    elif decodedword[step] == 17:
        decodedword[step] = "q"
    elif decodedword[step] == 18:
        decodedword[step] = "r"
    elif decodedword[step] == 19:
        decodedword[step] = "s"
    elif decodedword[step] == 20:
        decodedword[step] = "t"
    elif decodedword[step] == 21:
        decodedword[step] = "u"
    elif decodedword[step] == 22:
        decodedword[step] = "v"
    elif decodedword[step] == 23:
        decodedword[step] = "w"
    elif decodedword[step] == 24:
        decodedword[step] = "x"
    elif decodedword[step] == 25:
        decodedword[step] = "y"
    elif decodedword[step] == 26:
        decodedword[step] = "z"

print('The Decoded Word is:' + ''.join(decodedword))
wait=input("Press Enter to exit")
