word_stat = {}

def read_poem():
    with open('/Users/shubhammandal/Documents/python_practise/poem.txt','r') as f:
        for line in f:
            words = line.split(' ')
            for word in words :
                if word in word_stat :
                    word_stat[word]+=1
                else:
                    word_stat[word] = 1


read_poem()

print(word_stat)

word_occurences = list(word_stat.values())
max_count = max(word_occurences)
print("max occurences of word : ",max_count)

print('word with max occurences :')
for w , c in word_stat.items():
    if word_stat[w]==max_count:
        print(w)

