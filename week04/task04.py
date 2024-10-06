import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names = ["John", "Alice", "Bob", "Emily", "Michael", "Sarah", "David",  "Jessica", "Daniel", "Sophia", "James", "Olivia", "Andrew", "Mia", "Matthew", "Isabella", "Joshua", "Charlotte", "Ethan", "Liam", "Ava"]


subjects = ["Math", "Science", "English", "History", "Geography"]


Student_ID = np.random.randint(1000, 9999, size=1000)
Student_Name = np.random.choice(names, size=1000)
Subject = np.random.choice(subjects, size=1000)
Score= np.random.randint(0, 100, size=1000)
TotalMarks=100
df = pd.DataFrame({'Student_ID': Student_ID, 'Student_Name': Student_Name, 'Subject': Subject, 'Score': Score, 'TotalMarks': TotalMarks})

print(df.head())

score_array = df['Score'].to_numpy()

mean = np.mean(score_array)
median = np.median(score_array)

print('Mean Score:', mean)
print('Median Score:', median)


high_scorers = df[df['Score'] > 80]
length=len(high_scorers)
print('Number of students who scored more than 80:', length)

average_score = df.groupby('Subject')['Score'].mean()


# fifth




print('Average Score by Subject:', average_score)

plt.hist(df['Score'], bins=10)
plt.xlabel('Score')
plt.ylabel('Students')

plt.show()

plt.bar(average_score.index, average_score.values)
plt.show()
