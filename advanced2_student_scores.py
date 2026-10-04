# Advanced Functions 2 - Student Exam Scores

def exam_results(score1, score2, score3):
    total_points = score1 + score2 + score3
    average = total_points / 3
    return total_points, average

def main():
    last_name = input("Enter student's last name: ")
    score1 = float(input("Enter exam 1 score: "))
    score2 = float(input("Enter exam 2 score: "))
    score3 = float(input("Enter exam 3 score: "))

    total_points, average = exam_results(score1, score2, score3)

    print(f"Student: {last_name}")
    print(f"Total Points: {total_points:.2f}")
    print(f"Average Exam Score: {average:.2f}")

if __name__ == "__main__":
    main()
