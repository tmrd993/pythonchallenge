import pickle
import requests

url = r"http://www.pythonchallenge.com/pc/def/banner.p";

req = requests.get(url);
infile = open('ch5', 'wb').write(req.content)
outfile = open('ch5', 'rb');

outlist = pickle.load(outfile);

for sublist in outlist: # print the result to the terminal
    for k, v in sublist:
        print(int(v) * k, end='');
    print();    
