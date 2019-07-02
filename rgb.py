from PIL import Image, ImageFilter
#Read image
im = Image.open( 'images(2)' )
#Display image
im.show()

#Applying a filter to the image
#im_sharp = im.filter( ImageFilter.SHARPEN )
#Saving the filtered image to a new file
#im_sharp.save( 'image_sharpened.jpg', 'JPEG' )

#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
#r,g,b = im_sharp.split()
image = im.split()[1]

image.save('newimage_.png')
#im = Image.merge("RGB", (b, g, r))cor predominante imagem