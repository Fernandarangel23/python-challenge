import os
import csv

# input and output files
input_file = 'election_data.csv'
output_file = 'pypoll_out.txt'

candidates, total_candidates, candidate_perc, candidate_total, summaries = ([] for i in range(5))


with open(input_file, mode='r', newline='') as poll_data:
    reader = csv.reader(poll_data, delimiter=',')

    next(reader)

    num_rows = 0

    for row in reader:
        total_candidates.append(row[2])
        num_rows += 1



sorted_candidates = sorted(total_candidates)

for i in range(num_rows):
    if sorted_candidates[i - 1] != sorted_candidates[i]:
        candidates.append(sorted_candidates[i])


print("Election Results")
print("-----------------------------------")
print("Total Votes:", num_rows)

for j in range(len(candidates)):
    candidate_count = 0

    for k in range(len(sorted_candidates)):
        if candidates[j] == sorted_candidates[k]:
            candidate_count += 1

    candidate_perc.append(round(candidate_count / num_rows * 100, 1))
    candidate_total.append(candidate_count)



for row in candidate:
    print(row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) + ")")
    summary = (row[0] + ": ", str(row[1]) + "%", " (" + str(row[2]) + ")")
    summaries.append(summary)


for k in range(len(candidate_perc)):
    if candidate_total[k] > candidate_total[k - 1]:
        wincandidate = candidates[k]

print("Winner:", wincandidate)
