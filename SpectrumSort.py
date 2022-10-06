from PIL import Image
import os
import numpy as np
import tkinter as tk

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
            if (images.endswith(".jpg") or images.endswith(".png")):
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
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]
            d = maxColor - minColor
            if (maxColor == minColor):
                Hue = 0
            else:
                if r == maxColor:
                    Hue = (g - b)/d + (6 if g < b else 0)
                    if Hue > 0.9:
                        Hue = 0.005
                if g == maxColor:
                    Hue = (b - r)/d + 2
                if b == maxColor:
                    Hue = (r - g)/d + 4
                Hue /= 6.0
            self.__listOfHSL = np.append(self.__listOfHSL, Hue)
            
    def sortImages(self):
        for i in range(2, np.size(self.__listOfHSL)):
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

folderDirCopy = str()
folderDirPaste = str()

def sort():
    folderDirCopy = finput.get()
    folderDirPaste = foutput.get()
    indWork = SpectrumSort(folderDirCopy, folderDirPaste)
    indWork.imagestoRGB()
    indWork.convertRGBtoHUE()
    indWork.sortImages()
    indWork.insertImages()

win = tk.Tk()
win.title("SpectrumSort")
win.resizable(False, False)
tk.Label( win, text='Input' ).grid( row=0 )
tk.Label( win, text='Output' ).grid( row=1 )

finput = tk.Entry( win )
foutput = tk.Entry( win )

finput.grid( row=0, column=1 )
foutput.grid( row=1, column=1 )

tk.Button( win, text='Sort', command=sort ).grid( row=3, column=1, sticky=tk.W, pady=4 )

tk.mainloop()
