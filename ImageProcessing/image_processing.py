'''
Author: Brady Anderson
Date: 3/3/2021

Purpose: 
Process images pixel by pixel and edit the values to experiment with hiding bits in the lsb of the image color channels

This program is defined as a class that is my general image processing. It handles color channels, encoding, and saving files

'''
import cv2 as cv
import sys
import numpy as np
import random as rn
import string

class ImageProcessing():
    punctuation = string.punctuation
    whitespaceing = string.whitespace

    def __init__(self, fname):
        self.fname = fname

    def convert_to_greyscale(self):
        # given an image convert it to greyscale pixel by pixel with the option to save it
        img = cv.imread(f"{self.fname}.jpg")

        # convert to greyscale
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                colors = img[i, j]
                grey = .59 * colors[0] + .11 * colors[1] + .3 * colors[2]
                img[i, j] = (grey, grey, grey)

        # show before edit
        cv.imshow("Display window", img)
        k = cv.waitKey(0)

        if k == ord("s"):
            cv.imwrite(f"{self.fname}_grey.jpg", img)
        if k == ord("e"):
            print("TODO: implement encode method")

    def display_green(self):
        img = cv.imread(f"{self.fname}.jpg")

        src = img[:,:,1]

        # create empty shape of image 
        g_channel = np.zeros(img.shape)

        # assign the green channel to empty image
        g_channel[:, :, 1] = src

        # display and save
        cv.imshow("Green Only", g_channel)
        k = cv.waitKey(0)

        if k == ord("s"):
            cv.imwrite(f"{fname}_green.jpg", g_channel)

    def display_red(self):
        img = cv.imread(f"{self.fname}.jpg")

        src = img[:,:,2]

        # create empty shape of image 
        r_channel = np.zeros(img.shape)

        # assign the red channel to empty image
        r_channel[:,:,2] = src

        # display and save
        cv.imshow("Red Only", r_channel)
        k = cv.waitKey(0)

        if k == ord("s"):
            cv.imwrite(f"{fname}_red.jpg", r_channel)

    def display_blue(self):
        img = cv.imread(f"{self.fname}.jpg")

        src = img[:,:,0]

        # create empty shape of image 
        b_channel = np.zeros(img.shape)

        # assign the green channel to empty image
        b_channel[:,:,0] = src

        # display and save
        cv.imshow("Blue Only", b_channel)
        k = cv.waitKey(0)

        if k == ord("s"):
            cv.imwrite(f"{fname}_blue.jpg", b_channel)

    def convertText2Binary(self, m):
        '''
        m - message to be encoded

        returns a binary string of m
        '''
        binary_string = ""

        for letter in m:
            # we can add a 0 here when we are working with letters 
            binary_string += "0" + str(bin(ord(letter)))[2:]

        return binary_string

    def clean_message(self, message):
        '''
        remove whitespacing and punctuation from all messages
        '''
        output = ""
        for i in message:
            if(i not in self.punctuation or i not in self.whitespaceing):
                output += i
        return output

    def encode_image(self, message):
        '''
        input: 
        fname - the name of the file to be encoded\
        message - the message to encode

        returns an encoded file
        '''
        isEncoded = False
        channel = rn.randint(1, 3)

        img = cv.imread(f"{self.fname}.jpg")
        temp = cv.imread(f"{self.fname}.jpg")

        m = self.convertText2Binary(self.clean_message(message))

        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                pixel = img[i, j]
                # B G R - encode lsb with 2 bits from binary string
                if(channel == 1):
                    pixel_value = str(bin(pixel[0]))[:-2] + m[:2]
                    pixel[0] = int(pixel_value, 2)
                elif(channel == 2):
                    pixel_value = str(bin(pixel[1]))[:-2] + m[:2]
                    pixel[1] = int(pixel_value, 2)
                else:
                    pixel_value = bin(pixel[2])[:-2] + m[:2]
                    pixel[2] = int(pixel_value, 2)

                m = m[2:]

                if(len(m) == 0):
                    isEncoded = True
                    break
            if(isEncoded):
                break

        # display and save
        cv.imshow("Unencoded", temp)
        cv.imshow("Encoded", img)
        k = cv.waitKey(0)

        if k == ord("s"):
            cv.imwrite(f"{self.fname}_encoded.jpg", temp)
            cv.imwrite(f"{self.fname}_unencoded.jpg", img)


            

if __name__ == '__main__':
    image = ImageProcessing("./images/michael")

    # convert_to_greyscale("./images/milkyway")
    # display_blue("./images/milkyway")
    # print(convertText2Binary("Hello world"))

    # image.convert_to_greyscale()
    # secret_message = "All of my followers are so kinda I appreciate all of you and think it's wonderful that you are supporting me and would love to hear all your thoughts!"
    # image.encode_image(secret_message)
    # a = image.convertText2Binary("HelloWorld")
    image.convert_to_greyscale()


'''
Random Note:

Would be very cool to create something with boids or PLOS

-> defines collective swarm behavior

'''