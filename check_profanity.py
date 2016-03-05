import urllib

def read_text():
    text = open("C:\Users\gopi\Documents\Python\sampleText.txt")
    contents = text.read()
    print(contents)
    print("")
    text.close()
    print("Does the document contains any profane Words?")
    check_profanity(contents)
    print("")
    print("This is how a pirate will say the same text")
    pirate_speech(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert")
    elif "false" in output:
        print("No curse Words! Yayyy Its clean as sh*t")
    else:
        print("Could not scan the document")
def pirate_speech(text_to_convert):
    c = urllib.urlopen(" http://isithackday.com/arrpi.php?text=" + text_to_convert)
    output = c.read()
    print(output)
    c.close()
    

read_text()
