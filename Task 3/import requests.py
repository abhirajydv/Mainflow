import requests
from bs4 import BeautifulSoup

#url of webpage
url = 'https://time.com/4960202/most-influential-websites/'

#get request
response = requests.get(url)

#check if request was successful
if response.status_code ==200:
    #Parse HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    #Extract texts
    page_text = soup.get_text()

    #Extract Links
    links = [a['href'] for a in soup.find_all('a', href=True)]

    #Extract images
    images = [img['src'] for img in soup.find_all('img', src=True)]

    #Print extracted data
    print("page text:")
    print(page_text)

    print("\nLinks:")
    for link in links:
        print(link)

    print("\nImages:")
    for image in images:
        print(image)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")        
