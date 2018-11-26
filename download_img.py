import random
import urllib.request

url = "https://scontent.fdac5-1.fna.fbcdn.net/v/t1.0-9/29594676_1672187822873456_5116480409237836263_n.jpg?_nc_cat=0&oh=fb930cc3b678bdb6c4b828c3c8f185da&oe=5B297C7C"

def download_web_img(url):
    name = random.randrange(1, 1000)
    full_name = str(name)+".jpg"
    urllib.request.urlretrieve(url, full_name)
download_web_img(url)