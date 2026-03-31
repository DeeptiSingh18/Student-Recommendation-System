# utils.py

def explain_choice(career):
    if career == "AI/Data Science":
        return "Selected due to strong coding interest and mathematical ability."
    elif career == "Web Development":
        return "Selected based on coding interest and computer-related subject."
    elif career == "Business/Marketing":
        return "Selected due to strong communication and management interest."
    elif career == "Finance":
        return "Selected based on numerical skills and commerce background."
    elif career == "UI/UX Design":
        return "Selected due to creativity and design interest."
    elif career == "Animation":
        return "Selected based on creative skills and arts background."
    else:
        return "Selected based on overall input."


def save_to_file(data):
    file = open("student_data.txt", "a")
    file.write(data + "\n")
    file.close()