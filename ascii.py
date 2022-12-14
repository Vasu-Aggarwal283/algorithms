import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont

# Characters used for Mapping to Pixels
Character = {
    "standard": "@%#*+=-:. ",
}


def get_data(mode):
    font = ImageFont.truetype("DejaVuSansMono-Bold.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale


# Making Background Black or White
bg = "white"
# bg = "black"
if bg == "white":
    bg_code = 255
elif bg == "black":
    bg_code = 0

# Getting the character List, Font and Scaling characters for square Pixels
char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 400

# Reading Input Image
image = cv2.imread("among.jpg")

# Converting Color Image to Grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Extracting height and width from Image
height, width = image.shape

# Defining height and width of each cell==pixel
cell_w = width / num_cols
cell_h = scale * cell_w
num_rows = int(height / cell_h)

# Calculating Height and Width of the output Image
char_width, char_height = font.getsize("A")
out_width = char_width * num_cols
out_height = scale * char_height * num_rows

# Making a new Image using PIL
outputImage = Image.new('RGB', (out_width, out_height), color = (0, 0, 0))
draw = ImageDraw.Draw(outputImage)


# Mapping the Characters
for i in range(num_rows):
    min_h = min(int((i + 1) * cell_h), height)
    row_pix = int(i * cell_h)

    # lst = [i for i in range(5)] => We can make strings/lists/tuples in this way => lst = [0, 1, 2, 3, 4]
    # lst[first:last] gives us a sublist from the first index to the last index excluding the last index => lst[1:4]==[1, 2, 3]
    line = "".join([char_list[
        min(int(
            np.mean(image[row_pix:min_h, int(j*cell_w)
                    :min(int((j + 1) * cell_w), width)]) / 255 * num_chars
        ), num_chars - 1)]
        for j in range(num_cols)]) + "\n"
            draw.text((j* char_width, i * char_height), line, font=font ,fill=(r,g,b))

    # Draw string at a given position (x,y)
    

# Inverting Image and removing excess borders
if bg == "white":
    cropped_image = ImageOps.invert(out_image).getbbox()
elif bg == "black":
    cropped_image = out_image.getbbox()

# Saving the new Image
out_image = out_image.crop(cropped_image)
out_image.save("output1.jpg")