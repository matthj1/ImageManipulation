from PIL import Image

image = Image.open("Original/Bella.jpg")

max_dimension = 125

size_x, size_y = image.size

if size_x > size_y:
    scale = size_y/max_dimension
else:
    scale = size_x/max_dimension

new_dimensions = (size_x//scale, size_y//scale)
image.thumbnail(new_dimensions)
new = image.crop(((new_dimensions[0]-max_dimension)//2, 0, max_dimension + (new_dimensions[0]-max_dimension)//2, max_dimension))
new.show()