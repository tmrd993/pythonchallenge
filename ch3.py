import re

def findTargets():
    file = open("ch3.txt");
    text = "";
    for line in file:
        text += line.strip();
    file.close();

    matches = re.findall("[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}", text);
    return "".join([sub[4] for sub in matches]);
    
if __name__ == '__main__':
    print(findTargets());
