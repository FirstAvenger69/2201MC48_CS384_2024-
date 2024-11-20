import pandas as pd

def load_data():
    ip_1 = pd.read_csv("ip_1.csv", header=1)
    ip_2 = pd.read_csv("ip_2.csv", header=1)
    ip_3 = pd.read_csv("ip_3.csv", header=0)
    ip_4 = pd.read_csv("ip_4.csv", header=0)

    ip_1['course_code'] = ip_1['course_code'].str.strip()

    def extract_floor(room_no):
        if room_no[:2].isalpha():
            return room_no[:]
        else:
            return int(room_no[0])

    ip_3['floor'] = ip_3['Room No.'].apply(extract_floor)
    room_cap = ip_3.sort_values(by=['floor', 'Exam Capacity'], ascending=[True, True])

    return ip_1, ip_2, room_cap

def prepare_course_counts(ip_1):
    course_counts = ip_1['course_code'].value_counts().reset_index()
    course_counts.columns = ['course_code', 'count']
    return course_counts
