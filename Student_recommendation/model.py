# model.py

from collections import deque

def calculate_score(interest, strength, marks, subject):
    scores = {
        "AI/Data Science": 0,
        "Web Development": 0,
        "Business/Marketing": 0,
        "Finance": 0,
        "UI/UX Design": 0,
        "Animation": 0
    }

    if interest == "coding":
        scores["AI/Data Science"] += 2
        scores["Web Development"] += 2
    elif interest == "management":
        scores["Business/Marketing"] += 2
        scores["Finance"] += 2
    elif interest == "design":
        scores["UI/UX Design"] += 2
        scores["Animation"] += 2

    if strength == "math":
        scores["AI/Data Science"] += 2
        scores["Finance"] += 2
    elif strength == "communication":
        scores["Business/Marketing"] += 2
    elif strength == "creativity":
        scores["UI/UX Design"] += 2
        scores["Animation"] += 2

    if marks >= 85:
        scores["AI/Data Science"] += 2
        scores["Finance"] += 1
    elif marks >= 70:
        scores["Web Development"] += 1
        scores["Business/Marketing"] += 1

    if subject == "computer":
        scores["Web Development"] += 2
        scores["AI/Data Science"] += 1
    elif subject == "commerce":
        scores["Finance"] += 2
    elif subject == "arts":
        scores["Animation"] += 2
        scores["UI/UX Design"] += 1

    return scores


def bfs_search(options):
    queue = deque(options)
    visited = set()

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            return current


def get_best_career(scores):
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    options = [career for career, score in sorted_scores]
    return bfs_search(options)

# ---------------- SIMPLE ML MODEL ----------------
def ml_predict(interest, strength, marks, subject):
    
    # Simple dataset (training-like data)
    data = [
        ("coding", "math", "computer", "AI/Data Science"),
        ("coding", "communication", "computer", "Web Development"),
        ("management", "communication", "commerce", "Business/Marketing"),
        ("management", "math", "commerce", "Finance"),
        ("design", "creativity", "arts", "UI/UX Design"),
        ("design", "creativity", "arts", "Animation")
    ]

    best_match = None
    max_score = -1

    for d in data:
        score = 0
        
        if interest == d[0]:
            score += 1
        if strength == d[1]:
            score += 1
        if subject == d[2]:
            score += 1
        
        if score > max_score:
            max_score = score
            best_match = d[3]

    return best_match