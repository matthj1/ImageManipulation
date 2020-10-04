from PIL import Image

image = Image.open("Original/Bella.jpg")

max_dimension = 255

size_x, size_y = image.size

if size_x > size_y:
    scale = size_y/max_dimension
    new_dimensions = (size_x//scale, size_y//scale)
    image.thumbnail(new_dimensions)
    print(new_dimensions)
    print(((new_dimensions[0]-max_dimension)//2, 0, max_dimension + (new_dimensions[0]-max_dimension)//2, max_dimension))
    new = image.crop(((new_dimensions[0]-max_dimension)//2, 0, max_dimension + (new_dimensions[0]-max_dimension)//2, max_dimension))
    new.show()