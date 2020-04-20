import insta_methods as insta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from random import randint
import os

br = insta.create_session() # get browser chrome session
time.sleep(4) # depending on internet connection

insta.login(br)
insta.remove_dialog(br)
time.sleep(3)

famous = insta.get_famous()



