def romanToInt(s):
    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}
    output = 0
    list_s = list(s)
    for idx in range(len(list_s)):
        if (list_s[idx] == "V" or list_s[idx] == "X") and (list_s[idx-1] == "I") and (idx > 0):
            output = output - roman_to_int[list_s[idx-1]]
            output = output + roman_to_int[list_s[idx]]
            output = output - roman_to_int[list_s[idx-1]]
            if output < 0:
                output = abs(output)
        elif (list_s[idx] == "L" or list_s[idx] == "C") and (list_s[idx-1] == "X") and (idx > 0):
            output = output - roman_to_int[list_s[idx-1]]
            output = output + roman_to_int[list_s[idx]]
            output = output - roman_to_int[list_s[idx-1]]
            if output < 0:
                output = abs(output)
        elif (list_s[idx] == "D" or list_s[idx] == "M") and (list_s[idx-1] == "C") and (idx > 0):
            output = output - roman_to_int[list_s[idx-1]]
            output = output + roman_to_int[list_s[idx]]
            output = output - roman_to_int[list_s[idx-1]]
            if output < 0:
                output = abs(output)
        else:
            output += roman_to_int[list_s[idx]]
    return output

if __name__ == "__main__":
    s = "MMMCDXC"
    print(romanToInt(s))
