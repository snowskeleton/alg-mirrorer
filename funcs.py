#!/usr/bin/env python3
from logging import raiseExceptions

acceptableMoves = "RLFBUDrlfbudmxyz'23"

def mirror(input):
    match input:
        #return mirroed moves
        case "R":
            return "L"
        case "L":
            return "R"
        case "r":
            return "l"
        case "l":
            return "r"

        # F, B, U, D, x, y, and z don't swap faces, just change direction, so these moves can be returned as is
        case "F"|"B"|"U"|"D"|"f"|"b"|"u"|"d"|"x"|"y"|"z"|"m":
            return input

        # any other input is error
        case _:
            raise Exception(f"Sorry, the charcter '{input}' is not a valid character")

def clean(string, chars):
    # removes all spaces
    string = string.replace(" ", "")
    # removes from string all characters not in chars
    for c in string:
        if c not in chars:
            string = string.replace(c, '')
    return string

def invert(algorithm):
    cleanedAlg = list(clean(algorithm, acceptableMoves))
    output = []

    def nextMove():
        try: return cleanedAlg[0]
        except: return ""

    while len(cleanedAlg) > 0:
        # grab the first move and remove it from alg
        first = cleanedAlg.pop(0)

        # set the correct modifier (prime, non-prime, or double)
        # then, ensure we don't leave a dangling modifier at the start of our alg
        if nextMove() == "'":
            modifier = ""
            cleanedAlg.pop(0)
        elif nextMove() == "2":
            modifier = "2"
            cleanedAlg.pop(0)
        else:
            modifier = "'"

        # save computed move
        output.append(mirror(first) + modifier)

    return " ".join(output)
