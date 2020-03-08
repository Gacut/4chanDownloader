#MadeByGacut

import os
import sys
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen, urlretrieve

print('''
                           __         _                 
                          / /        | |                
                         / /____ ____| | _   ____ ____  
                        |___   _) ___) || \ / _  |  _ \ 
                            | |( (___| | | ( ( | | | | |
                            |_| \____)_| |_|\_||_|_| |_|
                                                        
            _____                    _                 _             
           (____ \                  | |               | |            
            _   \ \ ___  _ _ _ ____ | | ___   ____  _ | | ____  ____ 
           | |   | / _ \| | | |  _ \| |/ _ \ / _  |/ || |/ _  )/ ___)
           | |__/ / |_| | | | | | | | | |_| ( ( | ( (_| ( (/ /| |    
           |_____/ \___/ \____|_| |_|_|\___/ \_||_|\____|\____)_|    
                                                                     
	''')

# This part is just to get the url of the thread

while True:
    url = input('\nPlease enter link to 4chan thread: ')
    try:
        website = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(website)
        break
    except ValueError:
        print('\nThe URL type is not valid.
              Try to add "http://" before the link')
        print('Or just type in an actual link...smartass.')


# Make a folder for your files in this session
# If folder with that name already exists, it wil prompt
# you to rename it.

while True:
    folderName = input('Name your directory: ')

    try:
        os.mkdir(folderName)
        print('Directory "' + folderName + '" created.')
        break
    except FileExistsError:
        print('Directory "' + folderName + '" already exists.')
    except OSError:
        print("You can\'t name directory " + folderName)

# Finding links for pictures and shows, how many there are
# in this thread.

soup = bs(webpage, features="lxml")
images = []
for img in soup.findAll("a", {"class": "fileThumb"}):
    images.append('http:' + img.get('href'))
print('There are ' + str(len(images)) + ' pictures in thread')

# Downloading and saving downloaded file in folder made in this session
# You can press CTRL+C to close the program
os.chdir(folderName)
fileNumber = 1
for image in images:
    try:
        splited = image.split('/')
        print('\nDownloading ' + splited[-1] + '...')
        print('File ' + str(fileNumber) + ' out of ' + str(len(images)))
        urlretrieve(image, splited[-1])
        print('Done!')
        fileNumber += 1
    except KeyboardInterrupt:
        print('Program closed.')
        sys.exit()

print('\nEvery file in this thread is stored in "' + folderName + '" Folder.')
