from PIL import Image
import PIL.ImageOps

img = Image.open('ch11.jpg');
width, height = img.size;
px = img.load();

oddImage = PIL.Image.new(mode='RGB', size=(width // 2, height // 2));
evenImage = PIL.Image.new(mode='RGB', size=(width // 2, height // 2));

evenCol = 0;
oddCol = 0;
evenRow = 0;
oddRow = 0;
# go through the original image and split it into two images
#with odd and even pixels (x-coordinate)
for i in range(height):
    for j in range(width):
        if(j % 2 == 0 and i % 2 == 0): # even pixel
            evenImage.putpixel((evenCol, evenRow), (px[j, i]));
            evenCol += 1;
        elif(j %2 != 0 and i % 2 != 0): # odd pixel
            oddImage.putpixel((oddCol, oddRow), (px[j, i]));
            oddCol += 1;
    evenCol = 0;
    oddCol = 0;
    if(i % 2 == 0):
        evenRow += 1;
    else:
        oddRow += 1;

# both images show the suffix so it doesn't really matter which one is shown
oddImage.show();
evenImage.show();
