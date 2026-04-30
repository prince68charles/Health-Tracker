"""In this file we will load the repos and sucsefully conver them into readable data"""
import requests
import json


class InvalidRepositoryError:


    """Create a class that handles repoistory erros"""

    def __init__(self, message, original_expection = None):
        super.__init__(message)
        self.original_expection = original_expection



def load_repoistory(url, headers, owner, repo):

    """Here we will load the repoistory for storing and convert it into json"""

    metadata =  requests.get(url, headers).json()


    #Gather languages
    lang_url = f"{url}/languages"
    languages = requests.get(lang_url, headers).json()


    #Gather full file
    branch = metadata.get('default_branhc', 'main')
    tree_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recurisve=1"
    tree_data = requests.get(tree_url, headers).json()


    full_json_format = {

        "repo-name": metadata.get("name"),
        "desciription": metadata.get("description"),
        "visibility": metadata.get("visibility"),
        "stats": {

            "stars": metadata.get("stargazers_count"),
            "forks": metadata.get("forks_count"),
            "open_issues": metadata.get("open_issues_count")

        },

        "languages": languages,
        "file-structure": [{"path": item["path"], "type": item["type"], "size": item.get("size")}
            for item in tree_data.get("tree", [])
        ]

    }


    try:

        with open('loaded_repo.json', 'w') as f:

            json.dump(full_json_format, f, indent= 4)

            print("Repo found.")
    
    except FileNotFoundError:

        raise ("Could not find repoistory") 