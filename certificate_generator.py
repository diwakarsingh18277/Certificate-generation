#Certificate Generator

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def generateCertifcate(template, target, name, course):
	try:
		#load an image in memory
		canvas = Image.open('D:\images\certificate.jpg')
		#canvas.size = (w,h)

		# Create a drawing pen for the canvas
		# Thereafter, operations performed by the pen
		# will render on the canvas
		pen = ImageDraw.Draw(canvas)

		#more attributes
		fnt = ImageFont.truetype(font='arial.ttf', size=40)
		fg_color = 237, 28, 36  # r,g,b
        # location can be determined by using paint app
		name_center = 650,550
		course_center = 650,695
		now = datetime.now()
		#print(now.strftime('%A %a'))
		#print(now.strftime('%B %b'))
		#print(now.strftime('%d/%m/%Y'))
		#print(now.strftime('%H:%M:%S'))

		day = now.strftime('%d')
		month = now.strftime('%b')
		year = now.strftime('%Y')

		#write name
		reqd_size = pen.textsize(text=name, font=fnt)
		pen.text(xy= (name_center[0]-reqd_size[0]/2, name_center[1]- reqd_size[1]),text=name, font=fnt, fill=fg_color)

		#write course
		reqd_size = pen.textsize(text=course, font=fnt)
		pen.text(xy= (course_center[0]-reqd_size[0]/2, course_center[1]- reqd_size[1]),text=course, font=fnt, fill=fg_color)

		#write date
		pen.text(xy=(405,760), text=month, font=fnt, fill=fg_color)
		pen.text(xy=(265,760), text=day, font=fnt, fill=fg_color)
		pen.text(xy=(497,760), text=year, font=fnt, fill=fg_color)

		#save it
		canvas.save(target)

	except:
		print('Certificate Creation Failed')

generateCertifcate('D:\images\certificate.jpg', 'new_certificate.jpg', 'Diwakar Singh', 'Python for Everybody')
