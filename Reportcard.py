import csv

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def generate_report_card(name, roll_no, subjects, marks_list):
    total_marks = sum(marks_list)
    percentage = total_marks / len(subjects)
    top_score = max(marks_list)
    top_subject = subjects[marks_list.index(top_score)]

    lines = []
    lines.append(f"Student Name : {name}")
    lines.append(f"Roll Number  : {roll_no}")
    lines.append("-" * 50)
    lines.append(f"{'Subject':20}{'Marks':10}{'Grade':5}")
    lines.append("-" * 50)
    for subject, marks in zip(subjects, marks_list):
        lines.append(f"{subject:20}{marks:<10}{get_grade(marks)}")
    lines.append("-" * 50)
    lines.append(f"Total Marks  : {total_marks}/{len(subjects)*100}")
    lines.append(f"Percentage   : {percentage:.2f}%")
    lines.append(f"Top Subject  : {top_subject} ({top_score} marks)")
    lines.append("-" * 50)
    return lines, percentage

def main():
    print("\n📚 STUDENT REPORT CARD GENERATOR 📚")
    print("-" * 50)

    num_subjects = int(input("Enter number of subjects: "))
    subjects = [input(f"Enter subject {i+1} name: ") for i in range(num_subjects)]

    num_students = int(input("Enter number of students: "))
    all_students_data = []

    for _ in range(num_students):
        print("\n--- Enter Student Details ---")
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")

        marks_list = []
        for subject in subjects:
            while True:
                try:
                    marks = float(input(f"Enter marks for {subject} (out of 100): "))
                    if 0 <= marks <= 100:
                        marks_list.append(marks)
                        break
                    else:
                        print("⚠ Marks must be between 0 and 100.")
                except ValueError:
                    print("⚠ Please enter a valid number.")

        lines, percentage = generate_report_card(name, roll_no, subjects, marks_list)

        filename = f"{name.replace(' ', '_')}_ReportCard.txt"
        with open(filename, "w") as file:
            file.write("\n".join(lines))
        print(f"📄 Report card saved as '{filename}'.")

        all_students_data.append([name, roll_no] + marks_list + [sum(marks_list), percentage])

    csv_filename = "Class_Report.csv"
    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Roll No"] + subjects + ["Total Marks", "Percentage"])
        writer.writerows(all_students_data)
    print(f"\n📊 Class report saved as '{csv_filename}'.")

    topper = max(all_students_data, key=lambda x: x[-1])
    print("\n🏆 CLASS TOPPER 🏆")
    print(f"Name: {topper[0]} | Roll No: {topper[1]} | Percentage: {topper[-1]:.2f}%")

    print("\n📈 Subject-wise Average Marks:")
    for i, subject in enumerate(subjects, start=2):  # offset because name, roll_no are first
        avg = sum(student[i] for student in all_students_data) / num_students
        print(f"{subject:20}: {avg:.2f}")

if __name__ == "__main__":
    main()
