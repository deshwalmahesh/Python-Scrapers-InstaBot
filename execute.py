import insta_methods as insta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from random import randint
import os

br = insta.create_session() # get browser chrome session
insta.login(br) #login
insta.remove_dialog(br) # if there is a dialogue, remove it

famous = insta.read_file('famous.txt') # get list of famous people/pages
to_like = insta.read_file('to_like.txt')


if len(to_like) == 0:
    insta.get_names(br,famous,to_like)





            




