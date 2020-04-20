from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from random import randint
import os


def create_session():
    br=webdriver.Chrome()
    url = 'https://www.instagram.com/accounts/login/'
    br.get(url)
    return br


def login(br):
    with open('user_pass.txt','r')as f:
        user,password = f.readlines()

    br.find_element_by_name('username').send_keys(user.strip())
    time.sleep(1.2)
    br.find_element_by_name('password').send_keys(password.strip(),Keys.ENTER)


def remove_dialog(br):
    noti = br.find_elements_by_tag_name('button')
    for button in noti:
        if button.text == 'Not Now':
            button.click()
            break


def get_famous():
    with open('famous.txt','r') as f:
        famous = f.read().splitlines()
    return famous




