from instaloader import Instaloader, Profile
import instaloader

import re
import subprocess

L = Instaloader()

banned  = r'[a-zA-Z0-9_\-\.]'

def download_profile(username):
    PROFILE = username
    profile = Profile.from_username(L.context, PROFILE)
    posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.date, reverse=True)
    for post in posts_sorted_by_likes:
        L.download_post(post, PROFILE)

def download_profile_pic(username):
    L.download_profile(username, profile_pic_only=True)

def download_stories(username):
    L.download_profile(username, download_stories_only=True)

def download_post(url):
    shortCode = url.split('/')[-2]

    print(shortCode)
    post = instaloader.Post.from_shortcode(L.context, shortCode)
    
    name = re.sub(f'[^{banned}]', '', post.caption)

    L.download_post(post, target=name)
