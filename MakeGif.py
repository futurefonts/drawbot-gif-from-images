import sys
import os
from datetime import datetime

# Path to folder of images
# This add all images to the animation, in alphabetical order

docWidth=2046
docHeight=3634

srcPath = "./src/A" # change this to point to your directory of images
saveFormats = ['gif','mp4'] # use gif and/or mp4

framesPerSecond = 2 # lower will go slower, 30 is typical smooth animation
defaultFrameDuration = 1 / framesPerSecond
repeat = 1


fileName = srcPath.split('/')[-1]
exportPath = "./exports/"

saveEnabled = True  


def main():
    setup()
    for i in range(repeat):
        drawFrames()
    
    fullFilePath = exportPath + fileName + '-' + getTimestamp()
    print(fullFilePath)
    for saveFormat in saveFormats:
        saveImage(fullFilePath + '.' + saveFormat)

def setup():
    newDrawing()

def drawFrames():
    images = getImageList(srcPath)
    for imgSrc in images:
        drawFrame(imgSrc)

def drawFrame(imgSrc):
    newPage(docWidth, docHeight)
    frameDuration(defaultFrameDuration)
    image(imgSrc, (0, 0), alpha=1) 


def getImageList(directory):
    """
    Retrieves a list of image file paths from a given directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        list: A list of image file paths.
    """
    image_files = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Basic check based on file extension (case-insensitive)
            extensions = ['.jpg', '.jpeg', '.png', '.gif', '.tiff']
            if any(filepath.lower().endswith(ext) for ext in extensions):
                image_files.append(filepath)

    return image_files

def getTimestamp():
    """
    Returns the current date and time in the format YY-MM-DD-HH-MM.

    Returns:
        str: The formatted date and time string.
    """
    now = datetime.now()
    formatted_datetime = now.strftime("%y%m%d%H%M")
    return formatted_datetime
    
main()