import pyifx

image = pyifx.misc.PyifxImage("./imgs/input/img1.jpg", "./imgs/output/img1-output.jpg")

image = pyifx.hsl.to_grayscale(image)


volume = pyifx.misc.ImageVolume("./imgs/input/", "./imgs/output", "output-")

volume = pyifx.hsl.to_grayscale(volume)


list_image = [pyifx.misc.PyifxImage("./imgs/input/img1.jpg", "./imgs/output/img1-output.jpg")]

list_image = pyifx.hsl.color_overlay(list_image, [255,0,0], 50)