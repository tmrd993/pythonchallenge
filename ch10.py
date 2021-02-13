# a = [1, 11, 21, 1211, 111221,
# == look-and-say sequence

num = '1';

for i in range(0, 30):
    current = num[0];
    count = 0;
    tmpNum = '';
    for digit in num:
        if current == digit:
            count += 1;
        else:
            tmpNum += str(count) + current;
            current = digit;
            count = 1;
    tmpNum += str(count) + current;
    num = tmpNum;       

print(len(num));        
