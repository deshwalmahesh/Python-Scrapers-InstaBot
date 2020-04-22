from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from random import randint
import os



def update_file():
    unfollowed=[]
    to_unfollow=[]
    
    with open('unfollowed.txt') as f:
        unfollowed=f.read().splitlines()
        
    with open('1.txt') as f:
        to_unfollow=f.read().splitlines()

    return(unfollowed,to_unfollow)

def search(x):
    search_box=br.find_element_by_xpath("//input[@type='text']")
    search_box.clear() 
    search_box.send_keys(str(x))
    time.sleep(sleeping)
    search_box.send_keys(Keys.ENTER,Keys.ENTER)
    time.sleep(sleeping)
    if("No results found" in br.page_source):
        return (0)
    else:
        return(1)



def unfollow(i):
    if ("Following" in br.page_source):
        x=br.find_elements_by_tag_name("button")
        x[0].click()
        with open ('unfollowed.txt','a') as f:
            x=str(i)
            f.write('%s\n'%x)
    return()



br=webdriver.Chrome()
br.get('https://www.instagram.com/accounts/login/')
time.sleep(3)
br.find_element_by_name('username').send_keys('XXXXX')
br.find_element_by_name('password').send_keys('XXXXX',Keys.ENTER)
time.sleep(3)
like_count=0

while True:
    unfollowed,to_unfollow=update_file()
    
    try:
        br.get('https://www.instagram.com')
        time.sleep(3)
        for i in to_unfollow:
            
            sleeping=int(random.randint(4,7))
            if (str(i) in unfollowed):
                continue
            else:
                go=search(str(i))
                if go==0:
                    continue

                else:
                    if ("Following" not in br.page_source):
                        with open ('unfollowed.txt','a') as f:
                            x=str(i)
                            f.write('%s\n'%x)
                    else:    
                        unfollow(i)
                        time.sleep(sleeping)

    except Exception as e:
        print(e)
        pass
        
    

    




