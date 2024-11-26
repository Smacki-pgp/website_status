import requests

def check_url():
    url = input("Enter a website url: ")# Request url
    if url == "x": # Just a simple exit point
            return
    if "https://" not in url: # Check if Https:// is included
        response = requests.get("https://" + url)
    else:
        response = requests.get(url)
     
    if response.status_code == 200: #If url is responsive
        print(f"{url} is reachable! ")
        loaded_fc = response.text[:500] #collect first 500 characters in page
        print(f"\n Page loaded: \n {loaded_fc}") 
    else:
        print(f"Failed to reach {url}. Status code: {response.status_code}")
   
        




check_url()