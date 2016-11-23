import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


def resize_image(input_path, output_path, input_image_type, output_image_type, width, height):
    """Resize or change the image type

    input:
        path: input image save location
        output_path: output image save location
        input_image_type: the input image type
        output_image_type: the output image type
        width: the requested width in pixels
        height: the requested height in pixels
    """
    Filelist = []
    for root, dirnames, filenames in os.walk(input_path):
        for filename in filenames:
            if filename.endswith(input_image_type):
                Filelist.append(os.path.join(root, filename))

    for filename in Filelist:
        img = Image.open(filename)
        # you can also convert the image to gray-scale map
        # img = Image.open(filename).convert('L')
        # change the image size
        img = img.resize((width, height), Image.ANTIALIAS)
        outfile = os.path.join(output_path, os.path.split(filename)[1].split('.')[0] + output_image_type)
        print(filename + '  -size-> ' + outfile)
        # save image
        img.save(outfile)


if __name__ == '__main__':
    resize_image(input_path='./class', output_path='./class/1', input_image_type='.jpg', output_image_type='.jpg', width=60, height=60)