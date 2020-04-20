from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from random import randint
import os


def change_ip():
    os.system("ipconfig /release")
    time.sleep(3)
    os.system("ipconfig /renew")
    time.sleep(3)


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


def open_random_image(br):
    imgs = br.find_elements_by_class_name('_9AhH0')
    imgs[random.randint(0,len(imgs))].click()


def like_image(br,user_name):
    like_xpath = '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button'
    like_button = br.find_element_by_xpath(like_xpath)
    svg_css = 'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.FY9nT.fr66n > button > svg'
    if br.find_element_by_css_selector(svg_css).get_attribute('aria-label') == 'Like':
        like_button.click()
        with open ('liked.txt','a') as f:
            f.write('%s\n'%user_name)


def unlike_image(br):
    like_xpath = '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button'
    like_button = br.find_element_by_xpath(like_xpath)
    svg_css = 'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.FY9nT.fr66n > button > svg'
    if br.find_element_by_css_selector(svg_css).get_attribute('aria-label') == 'Unlike':
        like_button.click()
