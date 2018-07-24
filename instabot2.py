import time
import urllib.request as req
from InstagramAPI import InstagramAPI
from Instahandler import get_image_path
from image_access import image_aspect_change
from pathlib import Path

InstagramAPI = InstagramAPI('straighthalal','jibneh82')
InstagramAPI.login()
my_id = InstagramAPI.username_id


def image_upload():
    photo_path = get_image_path()
    caption = 'Testing 1 2 3'
    InstagramAPI.uploadPhoto(photo_path,caption)
    print('Done')


def following():
    #List of all followers
    my_follower_list = [i['pk'] for i in InstagramAPI.getTotalFollowers(my_id)]
    for id in my_follower_list:
        their_followers = [i['pk'] for i in InstagramAPI.getTotalFollowers(id)]
        for person_to_follow in their_followers:
            InstagramAPI.follow(person_to_follow)
            time.sleep(5)
            print('Followed!')

        print()

def unfollowing():
    #list of people following
    #following = InstagramAPI.getTotalFollowings(my_id)
    following_id = [i['pk'] for i in InstagramAPI.getTotalFollowings(my_id)]
    for id in following_id:
        InstagramAPI.unfollow(id)
        print('unfollowed: '+str(id))
        time.sleep(1)
    print(following_id)
    #for person in following:
    #    print(person)


def inbox():
    my_inbox = InstagramAPI.getv2Inbox()
    num_messages = InstagramAPI.LastJson['inbox']['threads']
    seen_file = open('seenit.txt','r+')
    posted_list = [line.replace('\n','') for line in seen_file.readlines()]
    seen_file.close()
    #if num[element]['thread_id'] in posted_list:
    notseen_file = open('seenit.txt','a+')
    ##Change profile photo OR post new photo
    for element in range(len(num_messages)):
        item_id = str(num_messages[element]['items'][0]['item_id'])
        base_access2 = num_messages[element]['items'][0]
        #caption = base_access2['text']
        gate2 = base_access2['item_type']
        print()
        print(num_messages[element])
        print()
        if item_id not in posted_list:
            notseen_file.write(item_id+'\n')
            if gate2 == 'media':
                photo_url = base_access2['media']['image_versions2']['candidates'][0]['url']
                req.urlretrieve(photo_url, "image_name.jpg")
                image_aspect_change("image_name.jpg")
                InstagramAPI.uploadPhoto("image_name.jpg")
                print('Done')
                time.sleep(5)
            if gate2 == 'raven_media':
                photo_url = base_access2['visual_media']['media']['image_versions2']['candidates'][0]['url']
                req.urlretrieve(photo_url, "image_name.jpg")
                image_aspect_change("image_name.jpg")
                InstagramAPI.uploadPhoto("image_name.jpg")
                print('Done')
                time.sleep(5)
            if gate2 == 'media_share':
                print('we in media share')
                photo_url = base_access2['direct_media_share']['media']['image_versions2']['candidates'][0]['url']
                req.urlretrieve(photo_url, "image_name.jpg")
                image_aspect_change("image_name.jpg")
                InstagramAPI.uploadPhoto("image_name.jpg")
                print('Done')
                time.sleep(5)
    notseen_file.close()
    print('File Closed')




if __name__ == '''__main__''':
    print('Oi')
    unfollowing()
