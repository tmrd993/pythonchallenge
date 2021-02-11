import requests;

baseUrl = r"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=";

def getNextNum(nothingNum):
    return requests.get(baseUrl + nothingNum).text;

def getLastNum(): # this takes a while due to the slow nature of http requests
    firstNum = "12345";
    #firstNum = "66831" # uncomment this variable to get the result instantly!
    nextRequestText = getNextNum(firstNum);
    requestNumBefore = "12345";
    while 'nothing is' in nextRequestText or 'Divide' in nextRequestText:
        if('Divide' in nextRequestText):
            nextRequestNum = str(int(requestNumBefore) / 2);
        else:
            nextRequestNum = nextRequestText[nextRequestText.index('nothing is') + len('nothing is') + 1:];
        nextRequestText = getNextNum(nextRequestNum);
        requestNumBefore = nextRequestNum;
        
    return nextRequestText;    

if __name__ == '__main__':
    print(getLastNum());
