import urllib

def read_text():
    text = open("C:\Users\gopi\Documents\Python\sampleText.txt")
    contents = text.read()
    print(contents)
    text.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    

read_text()
