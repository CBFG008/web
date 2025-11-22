from PIL import image, imagefilter
img = image.open("images/004 charmander. jpg")
filter_img =img.convert('L')
filter_img.save ("grey charmander, png")
print("images saved")