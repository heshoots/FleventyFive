import math

numbers = {0: '',1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
           6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'A', \
           11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G-teen', \
           17: 'H-teen', 18: 'I-teen', 19: 'J-teen', 20: 'K-teen', 21: 'L-teen', \
           22: 'M-teen', 23: 'N-teen', 24: 'O-teen', 25: 'P-teen', 26: 'Q-teen', \
           27: 'R-teen', 28: 'S-teen', 29: 'T-teen', 30: 'U-teen', 31: 'V-teen', \
           32: 'W-teen', 33: 'X-teen', 34: 'Y-teen', 35: 'Z-teen'}

numbersTens = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'A-ty', 'B-ty', 'C-ty', 'D-ty', 'E-ty', 'Fleventy']

magnitudes = {4:'Thousand', 7:'Million', 10:'Billion', 13:'Trillion'}



def numberOfDigits(number):
    if number > 0:
        return int(math.log(number, 16))+1
    if number == 0:
        return 1
    else:
        return numberOfDigits(-number)

def giveMagnitude(numberDigits):
    if numberDigits < 4:
        return ""
    if numberDigits in magnitudes:
        return magnitudes[numberDigits]
    else:
        return giveMagnitude(numberDigits-1)

def hexToList(number, numlist):
    (a,b) = divmod(number, 16)
    if a == 0:
        numlist.append(b)
        return numlist[::-1]
    else:
        numlist.append(b)
        return hexToList(a, numlist)

def getName(numberList):
    if len(numberList) == 0: return ""
    if len(numberList) % 3 == 1:
        numberList.insert(0, 0)
    if len(numberList) % 3 == 2:
        numberList.insert(0, 0)
    if len(numberList) == 3: return nameHundred(numberList)
    if len(numberList) % 3 == 0:
        return "%s %s, %s" % (nameHundred(numberList[:3]), giveMagnitude(len(numberList)), getName(numberList[3:]))
    else: return 
                             
#lists inputed must be three digits long
def nameHundred(numberList):
    if len(numberList) < 3:
        numberList.insert(0, 0)
        nameHundred(numberList)    
    if numberList[0] > 0:
        if numberList[1] == 1:
            return "%s-hundred and %s" % (numbers[numberList[0]], numbers[10 + numberList[2]])
        return "%s-hundred and %s %s" % (numbers[numberList[0]], numbersTens[numberList[1]-1], numbers[numberList[2]])
    if numberList[1] > 0:
        return "%s %s" % (numbersTens[numberList[1]-1], numbers[numberList[2]])
    if numberList[2] > 0:
        return "%s" % numbers[numberList[2]]
    else:
        return ""


def main(number):
    print(getName(hexToList(number, [])))

