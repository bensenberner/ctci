"{John,Tim,George} went on a {vacation,journey} in the {Grand Canyon,wilderness} to find {nature,tranquility}."
"@ went on a @ in the @", 

"#{name}" % "some string"

# choices = [[John, Tim, George], [vacation, journey]], [Grand Canyon, wilderness], [nature, tranquility]]
# choice could be ["John", "vacation", "wilderness", "nature"]
# allChoices = [["John", "vacation", "wilderness", "nature"], ["John", "vacation", "wilderness", "tranquility"]]
# n = len(choices)

# initialization

base case:
['nature', 'tranquility'], ['john', 'tim']
return ['nature', 'quility']

# after this, allChoices will contain all possible choices
"{John,Tim,George} went on a {vacation,journey} in the {Grand Canyon,wilderness} to find {nature,tranquility}."
# python string interpolation
# "hi there %s, %s" % [name, greeting]
#string = "{John,Tim,George} went %s on%s a {vacation,journey} in the {Grand Canyon,wilderness} to find {nature,tranquility}."
#newStringArray = string.split('%s')
# do the transformation on newStringArray --> transformedStringArray
#finalString = transformedString.join('%s')
re.sub(regex, "")


"{John,Tim,George} went on a {vacation} in the {Grand Canyon,wilderness} to find {nature,tranquility}."
"John went on a vacation"
from copy import deepcopy
import re

def printAllCombinations(string):
    regexString = "/{(\w*)}*/"
    regex = re.compile(regexString)
    matches = re.match(regex, someString)
    
    # there were no matches because there were no curly braces in the original string
    if not matches:
        print(string)
        return
    
    combinations = []
    for match in matches:
        combinations.append(match.split(','))
    # matches = [[john, tim, george], [vacation, journey], ...]
    
    # modify the original string to remove everything inside all curly braces
    string = re.sub(regex, "")    
    allCombos = []
    choice = []
    
    # modifies allCombos
    generateAllWordCombos(combinations, choice, allCombos, len(matches), 0)
    # allcombos = [['john', 'vacation', 'wilderness'], [...]...]
    
    for combo in allCombos:
        newString = deepcopy(string)
        newString.format(combo)
        print(newString)
    
    
def generateAllWordCombos(choices, choice, allChoices, n, index):
    if len(choice) == n:
        allChoices.append(choice)
        return
     
    for possibleWord in choices[index]:
        tempChoice = deepcopy(choice)
        tempChoice.append(possibleWord)
        generateAllWordCombos(choices, tempChoice, allChoices, n, index + 1)






# '{} {}'.format(['one', 'two'])
# "one two"








