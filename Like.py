from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from random import randint
import os

#useres list that are famous and related to your field
subject=['sc_web','supervinay','indiangymlegend','akshat_xesthetix','gym_fitness.idol','gauravarora55','jattmehkma','deeply.shredded','hazzelchoudhary','sandeep.xav','vikas_rt','real.bodybuilders','58vikash','the.ashu','monty_lohia','rahulchauhan26','sandeep.xav','rehan_mandaviya','dpanshu_narwal','mayank_sharma144','gauravmolri','faraaz_zs','sagarmidda','im_rahulsharmaa','musclemechanix','vasumittal','vinay_0610','_indianmen_','harish_rehman','vaibhav_63fitness']

def get_list():
    element=[]
    ran_num=int(random.randint(0,len(subject)-1))
    search(subject[ran_num])
    br.find_element_by_class_name("_e3il2").click() #open first image
    time.sleep(2)
    br.find_element_by_partial_link_text('likes').click()
    time.sleep(2)
       
    while len(element)<150:
            element=br.find_elements_by_xpath("//*[@class='_9mmn5']")
            i=len(element)-1
            element[i].click()
            time.sleep(1.50)
                    
    likers=br.find_elements_by_xpath("//*[@class='_2g7d5 notranslate _o5iw8']") #get the username
    for i in range(len(likers)):
            insta_id=likers[i].text
            if (insta_id not in main_list):
                main_list.append(insta_id)
                with open ('to_like.txt','a') as f:
                    f.write('%s\n'%insta_id)
                    
    return()

def update_file():
    main_list=[]
    private_acc=[]
    liked_list=[]
    with open('to_like.txt') as f:
        main_list=f.read().splitlines()

    with open('private_accounts.txt') as f:
        private_acc=f.read().splitlines()

    with open('liked.txt') as f:
        liked_list=f.read().splitlines()


    return(main_list,private_acc,liked_list)

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

def like_pic():
    x=br.find_element_by_class_name('_ebcx9')# find class of like button
    x.find_element_by_tag_name('a').click() #like
    with open ('liked.txt','a') as f:
        x=str(i)
        f.write('%s\n'%x)
    return()
    



def change_ip():
    os.system("ipconfig /release")
    time.sleep(3)
    os.system("ipconfig /renew")
    time.sleep(3)
    return()

br=webdriver.Chrome()
br.get('https://www.instagram.com/accounts/login/')
time.sleep(5)
br.find_element_by_name('username').send_keys('********')
br.find_element_by_name('password').send_keys('******',Keys.ENTER)
time.sleep(5)

while True:
    main_list,private_acc,liked_list=update_file()
    count=0
    
    try:
        br.get('https://www.instagram.com')
        time.sleep(3)
        for i in main_list:
            count+=1
            if count==len(main_list):
                change_ip()
                get_list()
                x=br.find_element_by_class_name('_ebcx9') #forced error so that we can update main list
            sleeping=int(random.randint(5,9))
            if ((str(i) in liked_list) or (str(i) in private_acc)):
                continue
            else:
                go=search(str(i))
                if go==0:
                    continue
                
                elif((("This Account is Private" in str(br.page_source)) or ("No posts yet" in str(br.page_source)) or ("Sorry" in str(br.page_source)))):
                    with open ('private_accounts.txt','a') as f:
                        x=str(i)
                        f.write('%s\n'%x) 
                    continue

                else:
                    br.find_element_by_class_name("_e3il2").click()
                    time.sleep(sleeping)
                    if ("Unlike" in str(br.page_source)):
                        br.back()
                        time.sleep(1)
                        with open ('liked.txt','a') as f:
                            x=str(i)
                            f.write('%s\n'%x)
  
                        continue
                    else:
                        like_pic()
                        br.back()
                        time.sleep(sleeping)

    except Exception as e:
        print(e)
        pass
        
    

    




