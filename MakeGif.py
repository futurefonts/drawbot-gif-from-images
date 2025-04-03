import sys
import os
from datetime import datetime



docWidth=1080
docHeight=1920

srcPath = "./src/stop-motion-1" # path to folder with images
saveFormats = ['gif','mp4'] # use gif and/or mp4

defaultFrameDuration = 0.5 # in seconds
repeat = 1 # how many times to loop (will result in larger file)


fileName = srcPath.split('/')[-1]
exportPath = "./exports/"

saveEnabled = True  


def main():
    setup()
    for i in range(repeat):
        drawFrames()
    
    if saveEnabled:
        for saveFormat in saveFormats:
            fullFilePath = exportPath + fileName + '-' + getTimestamp() + '.' + saveFormat
            saveImage(fullFilePath)
            print('exported: ' + fullFilePath)

    print('Done')
def setup():
    newDrawing()

def drawFrames():
    images = getImageList(srcPath)
    for imgSrc in images:
        drawFrame(imgSrc)

def drawFrame(imgSrc):
    #print(imgSrc)
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
    
    return sorted(image_files, key=str.lower)
    #return image_files

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