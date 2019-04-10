import csv

if __name__=='__main__':
    with open("tweetdata08.csv", "r", encoding="ISO-8859-1") as csvfile:
        reader = csv.reader(csvfile)
        i = 1
        for row in reader:
            if i%2000 == 0:
                print(row)
            i+=1
        print(i)
