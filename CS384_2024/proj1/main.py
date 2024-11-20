import pandas as pd
from data_loader import load_data, prepare_course_counts
from room_allocation import allocate_rooms
from student_assignment import assign_students_to_rooms

# Load and preprocess the data
ip_1, ip_2, room_cap = load_data()

# Calculates the number of students enrolled in each course.
course_counts = prepare_course_counts(ip_1)

# Adds a buffer to the room capacity by reducing it by the specified percentage.
buffer = int(input("Enter the buffer percentage (e.g., 5 for 5%): ")) / 100
room_cap["effective_capacity"] = (room_cap["Exam Capacity"] * (1 - buffer)).astype(int)

# Allocate rooms
final_allocations = pd.DataFrame()
for _, row in ip_2.iterrows():
    morning_courses = pd.DataFrame({'course_code': row['Morning'].split('; ')})
    morning_courses['course_code'] = morning_courses['course_code'].str.strip()
    morning_courses['count'] = morning_courses['course_code'].apply(
        lambda code: ip_1[ip_1['course_code'] == code].shape[0]
    )
    morning_courses = morning_courses.sort_values(by="count", ascending=False).reset_index(drop=True)

    morning_allocations = allocate_rooms(morning_courses, room_cap, buffer)
    final_allocations = pd.concat([final_allocations, morning_allocations], ignore_index=True)

    room_cap["effective_capacity"] = (room_cap["Exam Capacity"] * (1 - buffer)).astype(int)

# Assign students to rooms
final_with_students = assign_students_to_rooms(ip_1, final_allocations)

# Save outputs
final_with_students.to_excel("room_assignment.xlsx", index=False)
final_with_students.to_csv("room_assignment.csv", index=False)

# Final Message
print("Room assignments completed. Outputs saved.")
