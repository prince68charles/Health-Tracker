from load_repo import load_repoistory
import pandas as pd
import datetime


"""This file will retreive data for scores"""


def retreieve_contributors(repo: list[dict]) -> list: 


    """This will reterive a list of contriubuters for each repoistory"""
    
    #Read the json file
    repo_df = pd.json_normalize(repo['Contributors'])

    logins = repo_df['login']

    subset = repo_df[['login', 'contributions']]

    return subset

def retreive_commits(repo: dict) -> list:

    """This will reterive a list of commits for each repo along with their dates"""

    commit_list = repo["Commits"]

    df = pd.DataFrame(commit_list)

    return df
    


def retereive_stars(repo: dict) -> int:

    """This will reterive the number of stars"""

    return repo['stats']['stars']

def reterive_last_commit(repo: dict) -> datetime:

    """Returns the date of the last commit, and by who"""
    commits = retreive_commits(repo)

    return commits.iloc[0,0]


