import pandas as pd
import numpy as np
import statistics as stat
import math
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

'''
path to downloaded csv file from canvas,
relative to the directory this file is being called from
change to fit your local configuration
'''
path = "./grades.csv"

data = pd.read_csv(path)
data = np.array(data)
sections = {}

for i in range(2, len(data)):
    section = data[i][4][-2:]
    if section not in sections:
        sections[section] = []
    score = data[i][12]
    if not math.isnan(score):
        sections[section].append(score)

section_means = {}
section_medians = {}

print("section: mean, median")
for section in sections:
    mean = math.ceil(stat.mean(sections[section]) * 10) / 10
    median = stat.median(sections[section])
    print(section + ": " + str(mean) + ", "+ str(median))

    if section not in section_medians:
        section_means[section] = mean
        section_medians[section] = median


class_avg = stat.mean(section_means.values())
best_mean = max(section_means, key=section_means.get)
best_median = max(section_medians, key=section_medians.get)

print()
print("Class average: " + str(class_avg))
print("Class median: " + str(stat.median(section_medians.values())))
print()
print("Section with highest average score: " + str(best_mean) + " (" + str(section_means[best_mean]) + ")")
print("Section with highest average median: " + str(best_median) + " (" + str(section_medians[best_median]) + ")")
print("Best section objectively: AR")

all_grades = []
for i in sections:
    all_grades += sections[i]

grade_counts = {}
for i in all_grades:
    if i not in grade_counts:
        grade_counts[i] = 0
    grade_counts[i] += 1


x = grade_counts.keys()
y = grade_counts.values()
plt.bar(x, y)
plt.show()
