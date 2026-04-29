"""In this file we will load the repos and sucsefully conver them into readable data"""
import requests
import json
class InvalidRepositoryError:


    """Create a class that handles repoistory erros"""

    def __init__(self, message, original_expection = None):
        super.__init__(message)
        self.original_expection = original_expection



def load_repoistory(url, headers):

    """Here we will load the repoistory for storing and convert it into json"""

    response = requests.get(url, headers)

    try:

        if response.status_code == 200:
        
            #Here is the github repo
            response = response.json()

            with open("repos.json", "w") as f:

                json.dump(response, f, indent = 4)
        
    except InvalidRepositoryError:

        raise("Invalid repo, check again")
    

