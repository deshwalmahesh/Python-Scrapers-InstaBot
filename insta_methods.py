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
    time.sleep(random.uniform(2.8,4.6))
    return br


def login(br):
    user,password = read_file('user_pass.txt')
    br.find_element_by_name('username').send_keys(user.strip())
    time.sleep(random.uniform(1.1,2.4))
    br.find_element_by_name('password').send_keys(password.strip(),Keys.ENTER)
    time.sleep(random.uniform(2.4,3.1))


def remove_dialog(br):
    try:
        noti = br.find_elements_by_tag_name('button')
        for button in noti:
            if button.text == 'Not Now':
                button.click()
                break
    except:
        None


def get_posts(br):
    '''
    get number of posts by a user
    '''
    posts = br.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span').text
    posts = posts.replace(',','')
    return int(posts)


def get_followers(br,private=False):
    '''
    get number of followers of a user
    '''
    '''
    get following of a person
    '''
    if private:
        xpath = '/html/body/div[1]/section/main/div/header/section/ul/li[2]/span/span'
    else:
        xpath = '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span'
    
    followers = br.find_element_by_xpath(xpath).get_attribute('title')
    followers = followers.replace(',','')
    return int(followers)



def open_random_image(br):
    '''
    open a random image from the initial page of user
    '''
    time.sleep(random.uniform(2.0,3.0))
    imgs = br.find_elements_by_class_name('_9AhH0')
    imgs[random.randint(0,len(imgs))].click()
    time.sleep(random.uniform(2,3))
    if 'views' in br.page_source:
        br.find_element_by_xpath('/html/body/div[4]/div[3]/button').click() # close image
        open_random_image(br)
    
    time.sleep(random.uniform(2.5,3.5))
        


def like_image(br):
    '''
    like image IFF it has not been liked already
    '''
    time.sleep(random.uniform(1.5,2.5))
    br.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()# click heart
    time.sleep(random.uniform(1.0,2.0))
    br.find_element_by_xpath('/html/body/div[4]/div[3]/button').click() # close image
    time.sleep(random.uniform(2.5,4.5))


def unlike_image(br):
    '''
    unlike an image if it has been liked
    '''
    like_xpath = '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button'
    like_button = br.find_element_by_xpath(like_xpath)
    svg_css = 'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.FY9nT.fr66n > button > svg'
    if br.find_element_by_css_selector(svg_css).get_attribute('aria-label') == 'Unlike':
        like_button.click()


def follow(br,user=False,private=True):
    '''
    Follow a user is user is given or the browser is at the page itself
    '''
    if user:
        br.get('https://www.instagram.com/'+user+'/') # get user page
        time.sleep(random.uniform(1.98,3.99)) # wait for random time
    if private:
        xpath = '/html/body/div[1]/section/main/div/header/section/div[1]/button'
        if 'Requested' not in br.page_source: # if not already requested
            br.find_element_by_xpath(xpath).click()
    else:
        xpath = '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button'
        br.find_element_by_xpath(xpath).click()
    time.sleep(random.uniform(1.65,2.34))


def unfollow(br,user=False):
    '''
    Unfollow a user given username or the current page of user
    '''
    if user:
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


def append_to_file(filename,user):
    '''
    add user name to file
    '''
    with open (filename,'a') as f:
        f.write('%s\n'%user)


def overwrite_file(filename,my_list):
    '''
    overwrite a file using a list
    '''
    with open(filename, 'w') as f:
        for item in my_list:
            f.write("%s\n" % item)


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
    

def search(br,user):
    '''
    search a user and return if successful or not
    '''
    # activate search box
    br.find_element_by_xpath("//div[@role='button'][@class='pbgfb Di7vw ']").click()
    # input the text
    search_box = br.find_element_by_xpath("//input[@type='text'][@placeholder='Search']")
    search_box.clear() 
    search_box.send_keys(user)
    time.sleep(random.uniform(1.9,2.5))
    if("No results found" in br.page_source):
        br.find_element_by_xpath("//div[@role='button'][@class='aIYm8 coreSpriteSearchClear']").click()
        # close search bar
        time.sleep(random.uniform(1.5,2.4))
        return (br,False)
    else:
        search_box.send_keys(Keys.ENTER,Keys.ENTER)
        time.sleep(random.uniform(3.3,5.4))
        return(br,True)