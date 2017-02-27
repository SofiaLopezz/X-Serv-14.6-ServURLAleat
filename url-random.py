#!/usr/bin/python3

#Sofia Lopez

import webapp
import random

class randomApp (webapp.webApp):

    def process(self, parsedRequest):
        randomNum = 10000*random.random()
        randomURL = ("<html><a href=" + str(randomNum) + ">Dame otra</a><html>")
        return("200 OK", randomURL)

if __name__ == "__main__":
    testwebApp = randomApp("localhost", 1234)

