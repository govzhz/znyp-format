# Images to znyp format
It is mainly used to create images dataset for training, which supports RGB-image and one-channel grey image
# example

image(JPG / PNG) files:
```
├── resize_image.py
├── load_znyp_format.py
├── convert_images_to_znyp_format.py
├── README.md
├── znyp_dataset
└── classes
    ├── 0
    │   ├── gesture-1.jpg
    │   └── gesture-2.jpg
    ├── 1
    │   ├── gesture-3.jpg
    │   └── gesture-4.jpg
    ├── 2
    │   └── gesture-5.jpg
   
```

# prerequisites
depend on python3.5

 - pillow(PIL)
 - numpy
 - matplotlib


# usage 

 1. put your images in the class folder
 2. modify the configuration that matches the images in **convert_images_to_znyp_format.py**
 3. run the python script, which will transform you images into znyp format
    ```bash
    python convert_images_to_znyp_format.py
    ```
 4. you can also load and visualize the dataset using python script
    ```bash
    python load_znyp_format.py
    ```