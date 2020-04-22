from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


def search(x):
    
    search_box=br.find_element_by_xpath("//input[@type='text']")
    search_box.clear()
    search_box.send_keys(str(x))
    time.sleep(5)
    search_box.send_keys(Keys.ENTER,Keys.ENTER)
    time.sleep(4)
    return


main_list=[]
liked_list=[]
private=[]

with open('to_like.txt') as f:
    main_list=f.read().splitlines()
with open('liked.txt') as f:
    liked_list=f.read().splitlines()

with open('private_accounts.txt') as f:
    private=f.read().splitlines()

br=webdriver.Chrome()
br.get('https://www.instagram.com/accounts/login/')
time.sleep(2)
br.find_element_by_name('username').send_keys('XXXXXXXXX')
br.find_element_by_name('password').send_keys('XXXXXXXX',Keys.ENTER)
time.sleep(4)

search('rohitkhatrifitness')

br.find_element_by_class_name("_e3il2").click() #open first image
time.sleep(4)

br.find_element_by_partial_link_text('likes').click() #open list of likers
input(" fetch list and press enter")
    


likers=br.find_elements_by_class_name('_2nunc')#to get the whole list and get the user name of the person from list
for i in range(len(likers)):
    insta_id=str(likers[i].find_element_by_tag_name('a').get_attribute('title'))
    if (insta_id in main_list) or (insta_id in private) or (insta_id in liked_list):
        continue
    else:
        main_list.append(insta_id)
        with open ('to_like.txt','a') as f:
                f.write('%s\n'%insta_id)
br.back()
time.sleep(2)

