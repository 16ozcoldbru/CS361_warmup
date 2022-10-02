# Name: Andrew Osborne
# OSU Email: osborna2@oregonstate.edu
# Course: CS361
# Assignment: Microservices Warm-up
# Due Date: 10/3/2022
# Description: An exploration of microservices
import time

number_of_pics = 4

while True:
    """Converts a random integer from 'image-services.txt' to
    a valid path to image stored locally"""
    time.sleep(1)

    image_file = open("image-service.txt", "r")
    line = image_file.readline()
    image_file.close()
    if line.isdigit():
        rand_num = int(line) % number_of_pics
        path_str = "/Users/adeptus-astartes/cs-361/" \
                   + str(rand_num) + ".jpg"
        image_file = open("image-service.txt", "w")
        image_file.write(path_str)
        image_file.close()



