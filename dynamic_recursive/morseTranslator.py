morseDict = {'...': 'S', '.-.': 'R', '...--': '3', '.-..': 'L', '----.': '9', '-.-.': 'C', '-..': 'D', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '--': 'M', '.--.': 'P', '-...': 'B', '..-.': 'F', '.---': 'J', '-.-': 'K', '.--': 'W', '-': 'T', '--...': '7', '-....': '6', '..---': '2', '..': 'I', '--.': 'G', '...-': 'V', '.....': '5', '.-': 'A', '--.-': 'Q', '.': 'E', '..-': 'U', '---..': '8', '.----': '1', '....': 'H', '---': 'O', '-.': 'N', '....-': '4'}

def morseTranslate(string):
    # all possible interpretations of the string
    allInterpretations = []

    for i in range(len(string)):
        # translate the beginning of the string
        prefix = string[:i+1]
        if not prefix in morseDict:
            # can't append to a nonvalid prefix
            continue
        prefix = morseDict[prefix]
        # get all suffices starting after i, the current index
        suffices = morseTranslate(string[i+1:])
        for suffix in suffices:
            allInterpretations.append(prefix + suffix)
        # reached the end of the string, there are no suffices
        if not suffices:
            allInterpretations.append(prefix)

    return allInterpretations

def main():
    testStrings = ['...--.-', '.-.-.', '---.-']
    for string in testStrings:
        print("Morse translation of %s is %s\n\n" \
                % (string, morseTranslate(string)))
main()
