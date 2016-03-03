import turtle

def read_text():
    text = open("C:\Users\gopi\Documents\Python\sampletext.txt")
    print(text.read())
    text.close()   

read_text()
