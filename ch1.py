import string

def shiftCipherSolver(encryptedText, shiftValue):
    decryptedText = "";
    alphabet = string.ascii_lowercase;
    alphaLen = len(alphabet);
    for ch in encryptedText:
        if ch in alphabet:
            decryptedText += alphabet[(alphabet.index(ch) + shiftValue) % alphaLen];
        else:
            decryptedText += ch;
            
    return decryptedText;

if __name__ == '__main__':
    input = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr"
    "gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    );
    inputUrl = "rhttp://www.pythonchallenge.com/pc/def/map.html";
    print(shiftCipherSolver(input, 2));
    print(shiftCipherSolver("map", 2));
