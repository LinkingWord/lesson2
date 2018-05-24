
school_scores = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]}, 
                 {'school_class': '4b', 'scores': [4, 5, 3, 3, 4]}, 
                 {'school_class': '4c', 'scores': [3, 5, 4, 2, 4]},]


# average_for_each = [statistics.mean(school_scores[0]['scores']), 
                    # statistics.mean(school_scores[1]['scores']), 
                    # statistics.mean(school_scores[0]['scores'])]


average_for_each = [sum(school_scores[0]['scores'])/len(school_scores[0]['scores']),
                    sum(school_scores[1]['scores'])/len(school_scores[1]['scores']),
                    sum(school_scores[2]['scores'])/len(school_scores[2]['scores'])]


average_for_school = sum(average_for_each)/len(average_for_each)

all_avrg = [average_for_each, average_for_school]

for avrg in all_avrg:
    print(avrg) 


# for score in school_scores[0]['scores']:
    # print(score)

# print(school_scores[0]['scores'][0])





# for score in school_scores
   # print(score)

# print (sum(school_scores[0][1][2])/len(school_scores[0][1][2]))

# phrase = input('Введите слово/фразу: ')

# for letter in phrase:
   # print(letter)


# number = [25, 8, 26, 44, 68, 37, 15, 4, 19, 76]

# for number in number:
    #print(number+1)