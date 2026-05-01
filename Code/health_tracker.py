"""
1:This file will judge the overall health of repo using the data reterived via data_reteriver.py.
2: It will then plot the overall health via matplotlib
"""

import data_reteriver


def calculate_score(contriubtions, commits, stars, date):

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

    **Formula:**
    $$Health = (0.4C_{ont} + 0.35C_{omm} + 0.25S) \cdot \text{decay}(date)$$

    :param contributions: int, number of unique contributors.
    :param commits: int, total commit count.
    :param stars: int, total star count.
    :param date: datetime, last activity timestamp.
    :return: float, normalized health score (0-100).
    """



def plot_score(cont_score, commit_score, star_score, date_score):

    
    """
    Generates a visual representation of repository health metrics.

    ### Visualization Components:
    *   **Data Points:** Maps individual scores for Contributions, Commits, 
        Stars, and Recency.
    *   **Plot Type:** Typically renders a **Radar (Spider) Chart** to show 
        balance across categories or a **Bar Chart** for direct comparison.
    *   **Normalization:** Ensures all scores are scaled (e.g., 0-1.0) for 
        visual consistency.

    ### Parameters:
    :param cont_score: float, weighted contribution metric.
    :param commit_score: float, weighted commit frequency metric.
    :param star_score: float, weighted community popularity metric.
    :param date_score: float, calculated recency/decay factor.
    """

