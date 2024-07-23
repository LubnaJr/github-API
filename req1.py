import requests

class githup:
    def __init__(self, user):
        self.username = user
        self.repo = []

    def get_repos(self):
        url = f"https://api.github.com/users/{self.username}/repos"  
        response = requests.get(url)
        if response.status_code == 200:
            self.repo = response.json()
            self.display_repos()
        else:
            print(f"Eror: {response.status_code} - {response.json().get('message')} ")  

    def display_repos(self):
        for r in self.repo:
            name = r.get('name')
            description = r.get('description')
            stars = r.get('stargazers_count')
            forks = r.get('forks_count')  
            print(f"Name: {name}\nDescription: {description}\nStars: {stars}\nForks: {forks}\n{'-'*40}")      

def main():
    username = input("Enter GitHub username: ")
    githup_repo = githup(username)
    githup_repo.get_repos()

if __name__ == "__main__":
    main() 

