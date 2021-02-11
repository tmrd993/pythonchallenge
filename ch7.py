import re
from PIL import Image

image = Image.open('ch7.png');
pixels = image.load();

width = image.size[0];
height = image.size[1];

# the rectangles are located at exactly height / 2
codepoints = [pixels[0, height / 2][0]];

# the rectangles all have a width of 7 pixels except the first one (loop and see for youself)
# we already took the first which has a width of 5 so we need to start at width = 5
# note that we only take the first colorpoint (R) since R==G==B for all rectangles.
for i in range(5, width, 7):
    codepoints.append(pixels[i, height / 2][0]);

resultingtext = "".join([chr(codepoint) for codepoint in codepoints]);    

# the final rectangles represent 9 triple digit codepoints inside rectangular brackets (print and see for yourself)
suffixCodepoints = re.findall('[\\d]{3}', resultingtext);
suffix = "".join([chr(int(codepoint)) for codepoint in suffixCodepoints]);
print(resultingtext[:resultingtext.index('is') + 2] + ' ' + suffix);
image.close();
