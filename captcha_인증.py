from captcha.image import ImageCaptcha
image = ImageCaptcha()

data = image.generate('111111')

image.write ('111111','sample.png')