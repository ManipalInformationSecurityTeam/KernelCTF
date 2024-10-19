import random
filenames = [
    "code1.py",
    "code2.py"
]

files = [open(i,"r") for i in filenames]
codes = [i.readlines() for i in files]
lengths = [len(code) for code in codes]
total_lines = sum(lengths)
packages = [[(i+1,j==0,codes[j][i]) for i in range(lengths[j])] for j in range(len(filenames))]
combined = [j for i in packages for j in i]
# for i in combined:
#     print(i)
random.seed()
random.shuffle(combined)
combined = [(i+1,) + combined[i] for i in range(total_lines)]

table = open("table.py","w")
answer = open("answers.txt", "w")
for i in combined:
    table.write(i[3])
    if i[2]:
        answer.write(f"{i[0]} ")

map((lambda x: x.close), files)
table.close()
answer.close()
