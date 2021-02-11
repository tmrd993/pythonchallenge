from zipfile import ZipFile

zip = ZipFile('ch6.zip', 'r');
print(zip.getinfo('90052.txt').comment);

pathPrefix = 'ch6/';
fileType = '.txt';

filename = "90052";
fileContents = open(pathPrefix + filename + fileType, "r").read();
filename = fileContents[fileContents.index('is') + 3:];
print(str(zip.getinfo(filename + fileType).comment)[2], end=""); # print the first character

while 'nothing is' in fileContents:
    fileContents = open(pathPrefix + filename + fileType, "r").read();
    if('comments' in fileContents):
        break;
    filename = fileContents[fileContents.index('is') + 3:];
    output = str(zip.getinfo(filename + fileType).comment);
    output = output[2:output.index('\'', 2)] # strip quotation marks
    if output == '\\n':
        print();
    else:
        print(output, end='');
