# main.py

from model import calculate_score, get_best_career
from utils import explain_choice, save_to_file


def main():
    print("\nStudent Recommendation System")
    print("--------------------------------")

    interest = input("Enter interest (coding/management/design): ").lower()
    strength = input("Enter strength (math/communication/creativity): ").lower()
    marks = int(input("Enter marks (0-100): "))
    subject = input("Enter favourite subject (computer/commerce/arts): ").lower()

    scores = calculate_score(interest, strength, marks, subject)
    result = get_best_career(scores)

    print("\nRecommended Career Path:")
    print(result)

    print("\nReason:")
    print(explain_choice(result))

    data = interest + ", " + strength + ", " + str(marks) + ", " + subject + " -> " + result
    save_to_file(data)


def menu():
    while True:
        print("\nMenu")
        print("1. Get Recommendation")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            main()
        elif choice == "2":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Try again.")


menu()