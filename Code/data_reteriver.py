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

def retreive_last_commit(repo: list[dict]) -> list:

    """This will reterive a list of commits for each repo"""



def retereive_star_growth(repo: list[dict]) -> int:

     """This will reterive the number of stars in the last 90 days"""


def recency_score(repo:list[dict]) -> datetime:

    """Will reterive the date of the last commit"""


