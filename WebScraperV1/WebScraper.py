# Big Boi Notes:
# This "Image Extractor" cannot extract images if they are saved as dynamic HTML files.
# (basically, if other code has to take in variables, it cannot extract data from them)
# HOWEVER, this did work somehow using other images, SO ->
# If I can big brain my way out of this, and sort dynamic and static images, I can still make it work
# I can do this by searching for .jpg and .png "HTML links" inside of the source code
# Update 1: Managed to save all files stored in a static HTML link locally onto my desktop. New plan is to find out how to store what appear to be "base64 gifs"

import os # This one exists to give access to my computer
import requests # This one reads HTML files from URL links
from bs4 import BeautifulSoup # This one EXTRACTS data
from urllib.parse import urljoin, urlparse # And THIS one joins the image URL with the source URL. Idk why.
import base64
from PIL import Image
from io import BytesIO

# My FUNCTIONS MUHAHAHA
from Functions import scanStaticPNG


# Obtain Info
src = "https://honkai-star-rail.fandom.com/wiki/Silver_Wolf"
req = requests.get(src)
soup = BeautifulSoup(req.content, "html.parser")
psoup = soup.prettify(encoding="utf-8")

# Obtain Image Tags
img_tags = soup.find_all('img')

# Create save directory
save_dir = 'downloaded_imgs'
os.makedirs(save_dir, exist_ok=True)

for img_tag in img_tags:
    print("Image src:", img_tag['src'])
    print("Alt txt:", img_tag.get('alt', 'No Alt Text Availible'))
    
    
    # Obtain "absolute image url", whatever that means
    img_url = urljoin(src, img_tag['src']) 
    
    if '.png' in img_url.lower():    
       scanStaticPNG(img_url, save_dir, img_tag)
    print('--------------------\n')