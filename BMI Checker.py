#by Jonesy167, Body Mass Index Tool, tested on Windows 10 x64


import os 

#set file paths as varaiables using CSIDL type function, to mitigate unpredictable system names
healthy = os.path.join(os.environ['USERPROFILE'], "Desktop\BMI-master\other\healthy.jpg")
superfat = os.path.join(os.environ['USERPROFILE'], "Desktop\BMI-master\other\superfat.jpg")
superfat2 = os.path.join(os.environ['USERPROFILE'], "Desktop\BMI-master\other\superfat2.jpg")
superfat3 = os.path.join(os.environ['USERPROFILE'], "Desktop\BMI-master\other\superfat3.jpg")
superfat4 = os.path.join(os.environ['USERPROFILE'], "Desktop\BMI-master\other\superfat4.jpg")
superfat5 = os.path.join(os.environ['USERPROFILE'], "Desktop\BMI-master\other\superfat5.png")
instructions = os.path.join(os.environ['USERPROFILE'], "Desktop\BMI-master\other\instructions.docx")
sweat = os.path.join(os.environ['USERPROFILE'], "Desktop\BMI-master\other\sweat.jpg")

print ("this program will let you know if your fat or not, in case there was any doubt...............")

print ("")

print ("Using you're weight (plenty of that to go arround?) and height it will calculate your Body Mass Index (BMI) and let you know if you should be considering selling the surplus part of you to the soap factory :)")

raw_input ("")

sex = (raw_input ("are you male or female? enter M for Male and F for female          "))

print ("")

weight_subject = float(raw_input ("enter your weight in kg e.g. 65.40       "))

print ("")

height_subject = float (raw_input ("enter your height in metres e.g. 1.62     "))

print ("")

if sex in ["M", "m", "male", "Male"]:
	print ("Ok so you weigh %fkg are %fm tall and are a male" % (weight_subject, height_subject))

if sex in ["F", "f", "female", "Female"]:
	print ("Ok so you weigh %fkg are %fm tall and are a female" % (weight_subject, height_subject))

raw_input ("")

squared_height = height_subject **2

bmi = weight_subject / squared_height

print ("Your bmi is %f " % bmi)


raw_input ("")

if bmi >= 20 and bmi <= 25:
	print "your weight is good well done :) "
	import os
	import Image
	raw_input ("")
	os.startfile(healthy)
	
	
if bmi >=25 and bmi <= 30:
	print "your are OVERWEIGHT this is unacceptable, get running fatty!!!!!!!"
	import os
	import Image
	raw_input ("")
	os.startfile(superfat2)
	raw_input ("")
	print ("ok so i'm going to give you a tip..............")
	raw_input ("")
	os.startfile(instructions)
	
	
if bmi <=20:
	print "you are underweight, still better to be to thin than to fat :) "
	import os
	import Image
	raw_input ("")
	os.startfile(superfat3)

	
if bmi >=30:
	print "you are far far to fat! jesus do you do anything other than eat?"
	import os
	import Image
	os.startfile(superfat)
	raw_input ("")
	print ("ok so i'm going to give you a tip..............")
	raw_input ("")
	os.startfile(instructions)

raw_input ("")

if bmi <=25 and sex in ["f", "F", "female", "Female"]:
	print ("bye bye, stay thin foxy lady! you deserve a cool screensaver!")
	import ctypes
	SPI_SETDESKWALLPAPER = 20 
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, sweat, 0) #change screenaver to weakness leaving the body

if bmi <=25 and sex in ["m", "M", "male", "Male"]:
	print ("bye bye, stay thin handsome! you deserve a cool screensaver!")
	import ctypes
	SPI_SETDESKWALLPAPER = 20 
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, sweat, 0) #change screenaver to weakness leaving the body


if bmi >=25 and sex in ["f", "F", "female", "Female"]:
	print ("see ya later 'slim' enjoy the screensaver, don't let that be future you!!!!")
	import ctypes
	SPI_SETDESKWALLPAPER = 20 
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, superfat4, 0) #change screensaver to woman eating cake

if bmi >=25 and sex in ["m", "M", "male", "Male"]:
	print ("see ya later 'slim' enjoy the screensaver, don't let that be future you!!!!")
	import ctypes
	SPI_SETDESKWALLPAPER = 20 
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, superfat5, 0) #change screensaver to man eating cake

	
raw_input ("")

