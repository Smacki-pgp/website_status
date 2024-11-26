import requests

def check_url():
    url = input("Enter a website url: ")
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is reachable! ")
        loaded_fc = response.text[:500]
        print(f"\n Page loaded: \n {loaded_fc}")
    else:
        print(f"Failed to reach {url}. Status code: {response.status_code}")


check_url()