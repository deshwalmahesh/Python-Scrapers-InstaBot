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
    time.sleep(random.uniform(2.0,3.0))
    imgs = br.find_elements_by_class_name('_9AhH0')
    imgs[random.randint(0,len(imgs))].click()
    time.sleep(random.uniform(2,3))
    if 'views' in br.page_source:
        br.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()
        open_random_image(br)
    
    time.sleep(random.uniform(2.5,3.5))
        


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


def read_file(filename):
    '''
    read a file to get list of names
    '''
    with open(filename) as f:
        names=f.read().splitlines()
    return names


def get_names(br,famous_list,users):
    '''
    get list of users (likers) from a random pic
    '''
    name = random.choice(famous_list)
    br.get('https://www.instagram.com/'+name+'/')
    time.sleep(random.uniform(2.1,4.9))
    open_random_image(br)
    br.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button').click()
    # open the likes list
    time.sleep(random.uniform(2.2,4.4))
    i = 0
    while i<=50:
        element_inside_popup = br.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[4]/div[2]//a')
        time.sleep(random.uniform(2.2,3.3))
        element_inside_popup.send_keys(Keys.END)
        time.sleep(random.uniform(2.4,3.6))
        likers=br.find_elements_by_xpath("//*[@class='                   Igw0E   rBNOH        eGOV_     ybXk5    _4EzTm                                                                                                              ']")
        for liker in likers:
            users.append(liker.text)
        i+=1
    

