# -*- coding: utf-8 -*-
"""
@author: Anurag Natoo
"""
import praw
import urllib.request
import os
RedditClientId=#Enter CLIENT ID
RedditClientSecret=#Enter Client Secret
RedditUserAgent=#Enter User Agent 
reddit = praw.Reddit(client_id=RedditClientId, client_secret=RedditClientSecret,user_agent=RedditUserAgent)
subReddit=reddit.subreddit('aww')#Change Subreddit as Required
counter=1
for post in subReddit.new(limit=1000):#Increase or Decrease Limit as Required
    if "jpg" in post.url.lower():
        fname=r"images/aww/"+str(counter)+".jpg"#Edit fname as required
        print(post.url.lower())
        url=post.url
        try:
            urllib.request.urlretrieve(url,fname)
        except:
            print(counter,"Image not found")
        print(counter)
        counter+=1