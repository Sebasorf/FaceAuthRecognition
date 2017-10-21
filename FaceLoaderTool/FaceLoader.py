import time
import cv2
import os 

#Task Messages
CREATING_DB_DIR = 'Creating DB directory...      '
TAKING_PH =       'Saving photo to DB...         '

#Task Results Messages
OK =     'OK'
FAILED = 'FAILED'
DIR_ALREADY_EXISTS =         FAILED + ' - Directory exists'
INVALID_PHOTO_NAME =         FAILED + ' - This name is invalid'
PHOTO_NAME_ALREADY_EXISTS =  FAILED + ' - This name is already in use'
DB_ENTRY = 'Entry was created with that photo and name...'

#Input Messages
CREATE_NAME = 'Please, enter a "Name LastName" for adding to DB (e.g: Albert Kau): '

#Directories...
DIRECTORY_NAME = 'FaceDatabase'
DIRECTORY_PATH = os.path.dirname(os.path.realpath(__file__)) + '/../'
DIRECTORY_DB = DIRECTORY_PATH + DIRECTORY_NAME
OUTPUT_PHOTO = ''

##################################
#
# Application Start
#
##################################

existing_user_list = []

# Creo la carpeta si no existe. Sino, cargo las personas que tiene
print CREATING_DB_DIR,
if not os.path.exists(DIRECTORY_DB):
    os.makedirs(DIRECTORY_DB)
    print OK
else:
    existing_user_list = os.listdir(DIRECTORY_DB)
    existing_user_list = [f.split('.')[0].lower() for f in existing_user_list]
    print DIR_ALREADY_EXISTS

# Cargo a un nuevo usuario, valido que no exista, y que tenga mas de 1 palabra    
valid_name = False
while not valid_name:
    new_user_name = raw_input(CREATE_NAME).strip().lower()
    if len(new_user_name.split(' ')) > 1:
        if new_user_name not in existing_user_list:
            OUTPUT_PHOTO = DIRECTORY_DB + '/' + new_user_name + '.png'
            valid_name = True
        else:
            print PHOTO_NAME_ALREADY_EXISTS
    else:
        print INVALID_PHOTO_NAME


camera_port = 0
camera = cv2.VideoCapture(camera_port)
time.sleep(0.1)
return_value, image = camera.read()
cv2.imwrite(OUTPUT_PHOTO, image)
del(camera)
