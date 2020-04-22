import insta_methods as insta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from random import randint
import os

br = insta.create_session() # get browser chrome session
insta.login(br) #login
insta.remove_dialog(br) # if there is a dialogue, remove it

follow_count = 0
while True:
    # get files eveytime an error happens. so that you load from the previous
    famous = insta.read_file('famous.txt') 
    to_like = insta.read_file('to_like.txt') 
    liked = insta.read_file('liked.txt')
    private = insta.read_file('private.txt')
    followed = insta.read_file('followed.txt')

    try:
        br.get('https://www.instagram.com/')
        time.sleep(random.uniform(3.0,5.0))

        if len(to_like) == 0:
            # if user to connect is empty, get users from famous and save in file just in case it crashes
            insta.get_names(br,famous,to_like)
            insta.overwrite_file('to_like.txt',to_like)

        for i,user in enumerate(to_like[:]):
            br,success = insta.search(br,user)
            if not success:
                to_like.remove(user)
                print('No User Found','\n','*'*25)
                continue
            else:
                print('Search Successful')
                posts = insta.get_posts(br)

                if 'This Account is Private' in br.page_source:
                    print('Private profile')
                    # if account is private: wait long, follow, update files and remove from list
                    time.sleep(random.uniform(24.24,57.05))
                    insta.follow(br)
                    print('Followed')

                    private.append(user)
                    insta.append_to_file('private.txt',user)

                    followed.append(user)
                    insta.append_to_file('followed.txt',user)

                    to_like.remove(user)
                    print('_'*30)

                else:
                    print('Public Profile')
                    # for open account, like, append to list and files and remove
                    insta.open_random_image(br)
                    print('Image opened')
                    insta.like_image(br)
                    print('Image Liked')
                    liked.append(user)
                    insta.append_to_file('liked.txt',user)
                    
                    print('Getting Followers')
                    followers = insta.get_followers(br)
                    print(followers)

                    if followers > 2000:
                        print('User is famous')
                        if user not in famous:
                            famous.append(user)
                            insta.append_to_file('famous.txt',user)

                    to_like.remove(user)
                    print('-'*25)

            time.sleep(random.uniform(60.60,240.24)) # to avoid bot detection, randomly sleep for 1-4 minutes

    except Exception as e:
        # if an error occurs, update to_like 
        print(f"Error: '\n {'+'*30} \n {e} \n {'+'*30}")
        new = []
        for user in to_like:
            if (user not in liked) and (user not in followed) and (user not in private) and (len(user)>2):
                new.append(user)
        insta.overwrite_file('to_like.txt',new)