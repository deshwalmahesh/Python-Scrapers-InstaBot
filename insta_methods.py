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


def get_posts(br):
    '''
    get number of posts by a user
    '''
    posts = br.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span').text
    posts = posts.replace(',','')
    return int(posts)


def get_followers(br):
    '''
    get number of followers of a user
    '''
    followers = br.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('title')
    followers = followers.replace(',','')
    return int(followers)


def get_following(br):
    '''
    get following of a person
    '''
    following = br.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text
    following = following.replace(',','')
    return int(following)


def open_random_image(br):
    '''
    open a random image from the initial page of user
    '''
    imgs = br.find_elements_by_class_name('_9AhH0')
    imgs[random.randint(0,len(imgs))].click()


def like_image(br,user_name):
    '''
    like image IFF it has not been liked already
    '''
    like_xpath = '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button'
    like_button = br.find_element_by_xpath(like_xpath)
    svg_css = 'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.FY9nT.fr66n > button > svg'
    if br.find_element_by_css_selector(svg_css).get_attribute('aria-label') == 'Like':
        like_button.click()
        with open ('liked.txt','a') as f:
            f.write('%s\n'%user_name)


def unlike_image(br):
    '''
    unlike an image if it has been liked
    '''
    like_xpath = '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button'
    like_button = br.find_element_by_xpath(like_xpath)
    svg_css = 'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.FY9nT.fr66n > button > svg'
    if br.find_element_by_css_selector(svg_css).get_attribute('aria-label') == 'Unlike':
        like_button.click()


def follow(br,user):
    '''
    Follow a user
    '''
    br.get('https://www.instagram.com/'+user+'/') # get user page
    time.sleep(random.uniform(1.98,3.99)) # wait for random time
    xpath = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button'
    br.find_element_by_xpath(xpath).click()



def unfollow(br,user):
    '''
    Unfollow a user
    '''
    br.get('https://www.instagram.com/'+user+'/') # get user page
    time.sleep(random.uniform(1.8,3.9)) # wait for random time
    xpath = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button'
    br.find_element_by_xpath(xpath).click() # clik on first button
    time.sleep(random.uniform(1.1,2.7)) # beat the bot checker
    confirm_xpath = '/html/body/div[4]/div/div/div[3]/button[1]'
    br.find_element_by_xpath(confirm_xpath).click() # click on unfollow
