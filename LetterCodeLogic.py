#letter code logic by - Zach Palmer

class LetterCodeLogic:
    """encode/decode methods"""
    
    @staticmethod #lets class functions always avaliable
    def Encode(msg):
        result = ""
        leterList = []
        #reverse of decode
        #step threw each chr of msg (not split operation)
        UprMsg = msg.upper()
        for letter in UprMsg:
            try:
                #take each nchar and turn it into unicode val
                letter = ord(letter)
                if letter == 32:
                    leterList.append(0)
                elif letter not in range(65,91):
                    leterList.append(99)
                else:
                    leterList.append(letter)
            except ValueError:
                leterList.append(99)
        #adjust nunicode val to be our 1-26 number
        #spacew is still a special case of 0
        for code in leterList[0:]:
            if code == 0 or code == 99:
                result += str(code)
                result += " "
            else:
                result += str(code-64)
                result += " "
        return result

        
    @staticmethod
    def Decode(msg):
        #method to split msg strng and decode number
        result = ""
        #seperate string such as 1,26,4 into individual values:
        numbers = msg.split(",") #split string into list seperate elements
        #process each element of the list (e.g. '1','26','5')
        #step threw elemnts of the list nums
        for x in numbers:
            #convert individual string elmt into numeric value
            try:
                n = int(x.strip()) # el is now the integer value of string number elmt
                if n == 0:
                    c = " "
                elif n < 1 or n > 26:
                    c = "?"
                else:
                    #traslate  valid #s 1 to 26 into abc etc
                    # based on the char vals
                    c = chr(n+64)
            except ValueError:
                c = "?"
                
            result += c # last step inside for
            
        return result

    # extra credit cesar shift

    @staticmethod
    def EncodeCesar(msg,offset):
        result = ""
        letterList = []
        UprMsg = msg.upper()
        for letter in UprMsg:
            try:
                letter = ord(letter)
                if letter == 32:
                    letterList.append(32)
                elif letter not in range(65,91):
                    letterList.append(99)
                else:
                    letterList.append(letter)
            except ValueError:
                letterList.append(99)
        for code in letterList[0:]:
            if code == 32:
                result += str(0)
                result += " "
            elif code == 99:
                result += str(code)
                result += " "
            else:
                newLetter = (code - 64) + offset
                distance = 0
                if newLetter < 1:
                    distance = newLetter -1
                    result += str(27 + distance)
                    result += " "
                elif newLetter > 26:
                    distance = newLetter - 26
                    result += str(0 + distance)
                    result += " "
                else:
                    result += str(newLetter)
                    result += " "
        return result


    @staticmethod
    def DecodeCesar(msg,offset):
        result = ""
        letterList = []
        Smsg = msg.split(",")
        for letter in Smsg:
            try:
                letter = int(letter.strip())
                if letter == 0:
                    result += chr(32)
                elif letter not in range(1,27):
                    result += "?"
                else:
                    newLetter = letter + offset
                    distance = 0
                    if newLetter < 1:
                        distance = newLetter - 1
                        result += chr(91 + distance)
                    elif newLetter > 26:
                        distance = newLetter - 26
                        result += chr(64 + distance)
                    else:
                        result += chr(newLetter + 64)
            except ValueError:
                result += "?"
        return result


        
        
        
    
