import re
import nltk
import csv

with open(r'F:\\TwitterData\\tradenew.csv', "rb") as myfile:
    mycsvfile = csv.reader(myfile)
    for row in mycsvfile:
        #user_id = row[0]
        text = row[0]
        date_time = row[1]
        id = row[2]

        #print date_time[0:10] + date_time[25:30]
        # removing numbers:
        text = re.sub("\d+", "", text)
        # removing specific item:
        text = text.replace("<a>", "")
        # removing punctuations(1):
        text = re.sub(r'[^\w\s]', '', text)
        # removing punctuations(2):
        text = re.sub(r"(?:\@|'|https?\://)\s+", "", text)
        # tokenizing text:
        tokens_text = nltk.word_tokenize(text)
        # removing stopwords:
        stopwords = nltk.corpus.stopwords.words('english')
        #clearing date
        new_date = date_time[0:10] + date_time[25:30]

        print new_date

        new_list = []
        # print word_list
        for word in tokens_text:
            if word.lower() not in stopwords:
                if len(word) > 2:
                    new_list.append(word)
                    print word
        # new_list= [w for w in ]

        print new_list

        with open("F:\\TwitterData\\tradecleaning24.csv", "ab") as new_list_write:

            mycsvfile_write = csv.writer(new_list_write)
            mycsvfile_write.writerow([id, new_date, new_list])