from PIL import Image
import os
import numpy as np

class SpectrumSort:

    def __init__(self, folderDirCopy: str, folderDirPaste: str):   
        self.__listOfRGB = np.zeros((1,3))
        self.__listOfHSL = np.zeros(1)
        self.__listOfImages = []
        self.__count = 0
        self.__folderDirCopy = folderDirCopy
        self.__folderDirPaste = folderDirPaste

    def imagestoRGB(self):
        for images in os.listdir(self.__folderDirCopy):
            if (images.endswith(".jpg")):
                self.__listOfImages.append(images);
                image = Image.open(self.__folderDirCopy + "\\" + images)
                image = image.resize((1,1))
                pixel = image.load()
                self.__count += 1
                self.__listOfRGB = np.append(self.__listOfRGB, pixel[0,0]).reshape(self.__count + 1, 3)
                
    def convertRGBtoHUE(self):
        for rgb in self.__listOfRGB:
            maxColor = np.max(rgb)
            minColor = np.min(rgb)
            if (maxColor == minColor):
                Hue = 0
            else:
                if rgb[0] == maxColor:
                    Hue = (rgb[1] - rgb[2])/(maxColor - minColor)
                if rgb[1] == maxColor:
                    Hue = 120 + (rgb[2] - rgb[0])/(maxColor - minColor)
                if rgb[2] == maxColor:
                    Hue = 240 - (rgb[0] - rgb[1])/(maxColor - minColor) 
                if Hue < 0:
                    Hue += 360
                if Hue > 360:
                    Hue -= 360
            self.__listOfHSL = np.append(self.__listOfHSL, Hue)
        
    def sortImages(self):
        for i in range(2, np.size(self.__listOfHSL) - 2):
            temp = self.__listOfHSL[i]
            tempIm = self.__listOfImages[i - 2]
            j = i - 1
            while (j >= 0 and temp < self.__listOfHSL[j]):
                self.__listOfHSL[j + 1] = self.__listOfHSL[j]
                self.__listOfImages[j - 1] = self.__listOfImages[j - 2]
                j = j - 1
            self.__listOfHSL[j + 1] = temp 
            self.__listOfImages[j - 1] = tempIm
    
    def insertImages(self):
        counter = 0
        for image in self.__listOfImages:
            counter += 1
            os.popen('copy ' + self.__folderDirCopy + '\\' + image + " " + self.__folderDirPaste + '\\' + "{}.jpg".format(counter))

indWork = SpectrumSort("C:\indWork\input", "C:\indWork\output")
indWork.imagestoRGB()
indWork.convertRGBtoHUE()
indWork.sortImages()
indWork.insertImages()