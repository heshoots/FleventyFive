"use strict"


var numbers = {0: '',      1: 'One',  2: 'Two', 3: 'Three',
               4: 'Four',  5: 'Five', 6: 'Six', 7: 'Seven',
               8: 'Eight', 9: 'Nine', 10: 'A',  11: 'B',
               12: 'C',    13: 'D',   14: 'E',  15: 'F'}

var chars = ['0', '1', '2', '3', '4', '5', '6', '7',
             '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

var teens = ["Eleven",  "Twelve", "Thirteen", "Fourteen", "Fifteen",
             "Sixteen", "Seventeen", "Eighteen", "Nineteen", "A-teen",
             "B-teen",  "C-teen"   , "D-teen"  , "E-teen",   "F-teen"]

var numbersTens = {0: '', 1: 'Ten', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5:'Fifty',
                   6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety', 10: 'A-ty',
                   11: 'B-ty', 12: 'C-ty',  13: 'D-ty',  14: 'E-ty', 15: 'Fleventy'}

var magnitudes = {0: '', 1: 'Thousand', 2: 'Million', 3: 'Billion', 4: 'Trillion'}

function parseHundred(number)
{
    if (number > 255)
    {
        var digit = ((number - (number % 256)) / 256);
        var remainder = number % 256;
        if (remainder > 0)
        {
            return numbers[digit] + " hundred and " + parseTens(number % 256);
        }
        else
        {
            return numbers[digit] + " hundred";
        }
    }
    else
    {
        return parseTens(number)
    }
}

function getTeens(number)
{
    return teens[number - 17];
}

function parseTens(number)
{
    if (16 < number && number < 32)
    {
        return getTeens(number);
    }
    if (number > 15)
    {
        var digit = ((number - (number % 16)) / 16);
    }
    else
    {
        return parseDigit(number)
    }
    return numbersTens[digit] + " " + parseDigit(number);
}

function parseDigit(number)
{
    return "" + numbers[number % 16];
}

function splitNumber(number)
{
    var numlist = [];
    if (number < 4096)
    {
        numlist.push(number);
        return numlist;
    }
    numlist.push(number % 4096);
    var out = numlist.concat(splitNumber( ( number - (number % 4096) ) / 4096 ) )
    return out;
}

function toString(number)
{
    if (number == 0) {return "Zero"}
    if (number < 0) {return "Minus" + toString(-number)}
    var numlist = splitNumber(number);
    var strlist = ""
    for (var i = 0; i < numlist.length; i++)
    {
        strlist = (parseHundred(numlist[i]) + " " + magnitudes[i]) + " " + strlist;
    }
    return strlist;
}

function StringToHex(string)
{
    var num = 0
    for (var i = 0; i < string.length; i++)
    {
        num *= 16
        num += chars.indexOf(string[i]);
    }
    return num
}

function fleventyFive(string)
{
    return toString(StringToHex(string));
}
