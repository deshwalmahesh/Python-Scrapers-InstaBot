import insta_methods as insta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from random import randint
import os

br = insta.create_session() # get browser chrome session
time.sleep(random.uniform(3.1,5.7)) # depending on internet connection

insta.login(br)
time.sleep(random.uniform(2.4,5.5))

famous = insta.get_famous() # get list of famous people/pages

try:
    insta.remove_dialog(br) # if there is a dialogue, remove it
except:
    None

to_like = insta.read_file('to_like.txt')

if len(to_like) == 0:
    insta.get_names(br,famous,to_like)





            




