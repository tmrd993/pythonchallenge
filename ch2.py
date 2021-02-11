def getRares():
    file = open("ch2.txt");
    text = file.read();
    file.close();
 
    foundCharacters = "";

    for ch in text:
        if ch.isalpha():
            foundCharacters += ch;

    return foundCharacters;

if __name__ == '__main__':
    print(getRares());
