# Name: Andrew Osborne
# OSU Email: osborna2@oregonstate.edu
# Course: CS361
# Assignment: Microservices Warm-up
# Due Date: 10/3/2022
# Description: An exploration of microservices

import random, time

while True:
    """Checks for 'run' string in 'prng-service.txt' file and replaces it 
    with a random integer
    """
    time.sleep(1)

    prng_file = open("prng-service.txt", "r")
    line = prng_file.readline()
    prng_file.close()
    if line == "run":
        prng_file = open("prng-service.txt", "w")
        prng_file.writelines(str(random.randint(1, 10)))
        prng_file.close()



