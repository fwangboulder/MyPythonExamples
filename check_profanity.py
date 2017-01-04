import urllib
def read_text():
    quotes=open("c:\path\.txt")
    contents_of_file=quotes.read()
    #www.wdyl.com/profanity?q=shit
    #print contents_of_text
    quotes.close()
    check_profanity(contents_of_file)
def check_profanity(text_to_check):
    conntection=urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output=connection.read()
    print output
    connection.close()

read_text()
