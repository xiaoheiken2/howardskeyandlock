import os
import shutil
from bs4 import BeautifulSoup
import random

def short_code_state(state_repl):
    search_categories = open("/var/www/html/howardskeyandlock/duplicatescript1/staticfile/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    for credentials in search_categories:
        credential= credentials.strip().split(',')
        short_code = credential[2].replace('ï»¿', '').upper()
        state_repl1= credential[3].replace('ï»¿', '').title()
        try:
            if state_repl.lower() == state_repl1.lower():
                break
        except:
            break
    return short_code

for d in os.listdir('locksmith'):
    try:
        for c in os.listdir(f'locksmith/{d}'):
            try:
                for b in os.listdir(f'locksmith/{d}/{c}'):
                    try:
                        search_categories = open(f'locksmith/{d}/{c}/{b}', "r", encoding="utf8").read()
                        op= search_categories.replace("﻿", '')
                        soup = BeautifulSoup(op, "lxml")
                        state_repl= str(d).replace('ï»¿', '').replace('-', ' ').title()
                        abbr_state= short_code_state(state_repl)
                        city= str(c).replace('ï»¿', '').replace('-', ' ').title()
                        meta_description = soup.find("meta", attrs={"name": "description"})
                        description_content = meta_description.get("content")
                        description_content_fix= description_content.replace('Orlando', f'{city} {abbr_state}')
                        op= op.replace(description_content, description_content_fix).replace('srcset="https://covaticonstructioncorp.shop/wordpress1/wp-content/uploads/2024/06/cropped-Howards_lock___KEY-removebg-preview-130x78.png 130w, https://covaticonstructioncorp.shop/wordpress1/wp-content/uploads/2024/06/cropped-Howards_lock___KEY-removebg-preview-300x179.png 300w, https://covaticonstructioncorp.shop/wordpress1/wp-content/uploads/2024/06/cropped-Howards_lock___KEY-removebg-preview.png 353w"', '').replace('src="../../static/wp-content-city/uploads/2024/06/cropped-Howards_lock___KEY-removebg-preview-130x78.png"', 'src="../../static/wp-content-state/uploads/2024/06/cropped-Howards_lock___KEY-removebg-preview-130x78.png"').replace('srcset="https://covaticonstructioncorp.shop/wordpress1/wp-content/uploads/2024/06/Request-a-quote-image.png 437w, https://covaticonstructioncorp.shop/wordpress1/wp-content/uploads/2024/06/Request-a-quote-image-300x78.png 300w"', '').replace('src="../../static/wp-content-city/uploads/2024/06/Request-a-quote-image.png"', 'src="../../static/wp-content-state/uploads/2024/06/Request-a-quote-image.png"')
                        fp = open(f'locksmith/{d}/{c}/{b}', "w", encoding='utf-8-sig')
                        fp.writelines(op)
                        fp.close()
                    except Exception as oops:
                        print('Error communicating:', oops)
            except:
                pass
    except:
        pass

for d in os.listdir('locksmith'):
    try:
        search_categories = open(f'locksmith/{d}/index.html', "r", encoding="utf8").read()
        if len(d.split('-')) >3:
            op= search_categories.replace("﻿", '')
            soup = BeautifulSoup(op, "lxml")
            split_data= d.split('-')
            state_repl= f'{split_data[0]} {split_data[1]} {split_data[2]}'.replace('ï»¿', '').replace('-', ' ').title()
            
            meta_description = soup.find("meta", attrs={"name": "description"})
            description_content = meta_description.get("content")
            description_content_fix= description_content.replace('Orlando', f'{state_repl}')
            op= op.replace(description_content, description_content_fix).replace('srcset="https://covaticonstructioncorp.shop/wordpress1/wp-content/uploads/2024/06/cropped-Howards_lock___KEY-removebg-preview-130x78.png 130w, https://covaticonstructioncorp.shop/wordpress1/wp-content/uploads/2024/06/cropped-Howards_lock___KEY-removebg-preview-300x179.png 300w, https://covaticonstructioncorp.shop/wordpress1/wp-content/uploads/2024/06/cropped-Howards_lock___KEY-removebg-preview.png 353w"', '').replace('src="../static/wp-content-county/uploads/2024/06/cropped-Howards_lock___KEY-removebg-preview-130x78.png"', 'src="../static/wp-content-state/uploads/2024/06/cropped-Howards_lock___KEY-removebg-preview-130x78.png"').replace('srcset="https://covaticonstructioncorp.shop/wordpress1/wp-content/uploads/2024/06/Request-a-quote-image.png 437w, https://covaticonstructioncorp.shop/wordpress1/wp-content/uploads/2024/06/Request-a-quote-image-300x78.png 300w"', '').replace('src="../static/wp-content-county/uploads/2024/06/Request-a-quote-image.png"', 'src="../static/wp-content-state/uploads/2024/06/Request-a-quote-image.png"')
            
            fp = open(f'locksmith/{d}/index.html', "w", encoding='utf-8-sig')
            fp.writelines(op)
            fp.close()
        else:
            op= search_categories.replace("﻿", '')
            soup = BeautifulSoup(op, "lxml")
            split_data= d.split('-')
            state_repl= d.replace('ï»¿', '').replace('-', ' ').title()
            
            meta_description = soup.find("meta", attrs={"name": "description"})
            description_content = meta_description.get("content")
            description_content_fix= description_content.replace('Orlando', f'{state_repl}')
            op= op.replace(description_content, description_content_fix)
            
            fp = open(f'locksmith/{d}/index.html', "w", encoding='utf-8-sig')
            fp.writelines(op)
            fp.close()
    except:
        pass


try:
    search_categories = open(f'locksmith/index.html', "r", encoding="utf8").read()
    
    op= search_categories.replace("﻿", '')
    soup = BeautifulSoup(op, "lxml")
    meta_description = soup.find("meta", attrs={"name": "description"})
    description_content = meta_description.get("content")
    description_content_fix= description_content.replace('Orlando', f'USA')
    op= op.replace(description_content, description_content_fix)
    fp = open(f'locksmith/index.html', "w", encoding='utf-8-sig')
    fp.writelines(op)
    fp.close()
except:
    pass
