# by Jonesy167, Body Mass Index Tool, tested on Windows 10 x64, runs with python 2.7


import os


PHOTO_PATH = os.path.dirname(os.path.abspath(__file__)) + "/photo.jpg"

# set file paths
healthy = os.path.dirname(os.path.abspath(__file__)) +  "\other\healthy.jpg"
superfat = os.path.dirname(os.path.abspath(__file__)) + "\other\superfat.jpg"
superfat2 = os.path.dirname(os.path.abspath(__file__)) + "\other\superfat2.jpg"
superfat3 = os.path.dirname(os.path.abspath(__file__)) +"\other\superfat3.jpg"
superfat4 = os.path.dirname(os.path.abspath(__file__)) + "\other\superfat4.jpg"
superfat5 = os.path.dirname(os.path.abspath(__file__)) + "\other\superfat5.png"
instructions = os.path.dirname(os.path.abspath(__file__)) + "\other\instructions.docx"
sweat = os.path.dirname(os.path.abspath(__file__)) + "\other\sweat.jpg"

print("this program will let you know if your fat or not, in case there was any doubt...............")


PHOTO_PATH = os.path.dirname(os.path.abspath(__file__)) 
print (PHOTO_PATH)


print("")

print(
    "Using you're weight (plenty of that to go arround?) and height it will calculate your Body Mass Index (BMI) and let you know if you should be considering selling the surplus part of you to the soap factory :)")

print("")

sex = (raw_input("are you male or female? enter M for Male and F for female          "))

valid_sex = []
valid_sex.append ("M")
valid_sex.append ("F")
valid_sex.append ("m")
valid_sex.append ("f")


while sex not in (valid_sex):
    print ("")
    print ("are you male or female? enter M for Male and F for female")
    sex = (raw_input())
    if sex in (valid_sex):
        break
    else:
        sex = (raw_input("are you male or female? enter M for Male and F for female          "))


print("")

while True:
    weight_subject = raw_input("enter your weight in kg e.g. 65.40                  ")
    if weight_subject.isdigit():
        if int(weight_subject) >= 0:
            break
    elif weight_subject.count('.') == 1:
        if weight_subject.replace('.', '').isdigit():
            break

print("")

while True:
    height_subject = raw_input("enter your height in metres e.g. 1.62                       ")
    if height_subject.isdigit():
        if int(height_subject) >= 0:
            break
    elif height_subject.count('.') == 1:
        if height_subject.replace('.', '').isdigit():
            break

height_subject = float(height_subject)
weight_subject = float(weight_subject)

print("")

if sex in ["M", "m", "male", "Male"]:
    print("Ok so you weigh %fkg are %fm tall and are a male" % (weight_subject, height_subject))

if sex in ["F", "f", "female", "Female"]:
    print("Ok so you weigh %fkg are %fm tall and are a female" % (weight_subject, height_subject))

print ("")


squared_height = height_subject ** 2

bmi = weight_subject / squared_height

print("Your bmi is %f " % bmi)


if bmi >= 20 and bmi <= 25:
    print
    "your BMI is healthy, well done :) "


    raw_input("")
    os.startfile(healthy)

if bmi >= 25 and bmi <= 30:
    print
    "your are OVERWEIGHT this is unacceptable, get running fatty!!!!!!!"



    raw_input("")
    os.startfile(superfat2)
    raw_input("")
    print("ok so i'm going to give you a tip..............")
    raw_input("")
    os.startfile(instructions)

if bmi <= 20:
    print
    "you are underweight, still better to be to be a little to thin than to fat :) "


    raw_input("")
    os.startfile(superfat3)

if bmi >= 30:
    print
    "you are far far to fat! jesus do you do anything other than eat?"

    os.startfile(superfat)
    raw_input("")
    print("ok so i'm going to give you a tip..............")
    raw_input("")
    os.startfile(instructions)

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
	print ("see ya later 'slim' enjoy the background, don't let that be future you!!!!")
	import ctypes
	SPI_SETDESKWALLPAPER = 20 
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, superfat4, 0) #change screensaver to woman eating cake

if bmi >=25 and sex in ["m", "M", "male", "Male"]:
	print ("see ya later 'slim' enjoy the background, don't let that be future you!!!!")
	import ctypes
	SPI_SETDESKWALLPAPER = 20 
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, superfat5, 0) #change screensaver to man eating cake


print ("finised")
raw_input ("")

