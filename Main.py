import csv
import pickle
import time
import matplotlib.pyplot as plt
Dict = pickle.load(open('Dictionary.pkl','rb'))

comments = open("Topic1 dataset/helpfulness_reviews_worst_apps1 - Copy.csv", encoding="utf8")
csv_reader = csv.reader(comments, delimiter=',')

count = 0
repl = 0
t = []
start = time.time()
for row in csv_reader:
    if count%1000 == 0:
        t.append(time.time() - start)
    test_str = row[4]
    clean_str = ""
    for c in test_str:
        if c.isalnum() or c == " ":
            clean_str += c
    str_list = clean_str.split()

    for w in str_list:            
        if Dict.get(w) == None:
            continue
        else:
            str_list[str_list.index(w)] = Dict.get(w)
            repl += 1
    row[4] = " ".join(str_list)
    count += 1


comments.close()

n = range(0,104000,1000)
plt.plot(n, t)
plt.xlabel('Number')
plt.ylabel('time')