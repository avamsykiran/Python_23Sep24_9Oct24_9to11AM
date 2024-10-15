
def analyze(string):
    charCount=wordCount=spCharCount=digitCount=0

    for x in string:
        if x.isalpha():
            charCount += 1
        elif x.isdigit():
            digitCount += 1
        else:
            spCharCount += 1
    
    wordCount = string.count(" ")+1

    return {"NoOfChars":charCount,"NoOfWords":wordCount,"NoOfdigits":digitCount,"NoOfSpecialChars":spCharCount}

s1 = input("Enter a string ")

results = analyze(s1)

for key in results.keys():
    print("{}={}".format(key,results[key]))