"""
1:This file will judge the overall health of repo using the data reterived via data_reteriver.py.
2: It will then plot the overall health via matplotlib
"""

from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sn

def calculate_score(contriubtions, commits, stars, date_to_check):

    """
    Calculates a repository health score based on activity and community impact.

    ### Metrics & Weights:
    *   **Contributions (40%):** Measures collaborative diversity.
    *   **Commits (35%):** Measures development velocity.
    *   **Stars (25%):** Measures community popularity.

    ### Temporal Decay:
    The raw score is adjusted based on the `date` parameter. Recent activity 
    maintains the score, while older activity is penalized using a time-decay 
    function to account for project obsolescence.


    :param contributions: int, number of unique contributors.
    :param commits: int, total commit count.
    :param stars: int, total star count.
    :param date: datetime, last activity timestamp.
    :return: float, normalized health score (0-100).
    """

    #Calculate Score
    regular_score = 0.40*(len(contriubtions)) + 0.35*(len(commits)) + 0.25*(stars)

    #Grab todays date
    today = datetime.now()
    
    #Ensure date_to_check is a datetime object (if it's a string)
    if isinstance(date_to_check, str):
        
        date_to_check = datetime.fromisoformat(date_to_check)
    
    duration = today - date_to_check
    final_score = regular_score

    #Find pas days
    days_past = duration.days
    
   
    if days_past >= 90:

        final_score = 0.0

    elif days_past >= 30:

        final_score = regular_score - 0.30

    elif days_past >= 10:

        final_score = regular_score - 0.10
        
    
    return max(0.0, final_score)



def plot_score(repo_name, score):

    
    """
    Generates a visual representation of repository health metrics.

    

    ### Parameters:
    :param cont_score: float, weighted contribution metric.
    :param commit_score: float, weighted commit frequency metric.
    :param star_score: float, weighted community popularity metric.
    :param date_score: float, calculated recency/decay factor.
    """


    #Construct the graph
    
    fig, ax = plt.subplots(figsize = (8,5))
    sn.barplot(x=repo_name, y = score, ax=ax)

    ax.set_title("Healthines of Repoistories")
    ax.set_xlabel("Repoistory")
    ax.set_ylabel("Score")


    fig.savefig("Healthines-Tracker.png", dpi = 120)
    plt.close(fig)