import requests

def fetch_repo(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    if response.status_code == 200: # check the status code if 200 means success 
        repos = response.json()  # We want response in JSON format 
        #print(repos)
        for repo in repos:
            print(repo['name'])
            print(repo['svn_url'])
            
    else:
        print(f"Failed to fetch the repos {response.status_code}") 
        
fetch_repo("Pankajp1997")
