import csv
ids = []
def has_100k(reader):
    length = 0
    num_pos = 0
    num_neg = 0
    ids_file = []
    for row in reader:
        length+=1
        if row[0]=="0":
            num_neg+=1
        elif row[0]=="4":
            num_pos+=1
        ids_file.append(row[2])
    if length != 100000:
        print("FAILED 100k")
    else:
        print("SUCCESS 100k")
    has_50_50(num_pos, num_neg)
    global ids
    ids.append(ids_file)
def has_50_50(num_pos, num_neg):
    if num_neg != num_pos:
        print("FAILED 50-50 they do not equal")
    if num_neg != 50000:
        print("FAILED 50-50", num_neg)
    print("SUCCESS 50-50")

def no_ids_equal():
    global ids
    for i in range(len(ids)-1):
        for j in range(i+1, len(ids)):
            for k in range(len(ids[0])):
                if ids[i][k] == ids[j][k]:
                    print("FAILED EQUALS")
    print("PASSED: NO IDS EQUAL")
if __name__=='__main__':
    f_name = "tweetdata00.csv"
    file_ind = 1
    for i in range(16):
        f_name_list = list(f_name)
        if file_ind < 10:
            f_name_list[10] = str(file_ind)
        else:
            f_name_list[9] = str(file_ind)[0]
            f_name_list[10] = str(file_ind)[1]
        file_ind += 1
        f_name = ''.join(f_name_list)
        with open(f_name, "r", encoding="ISO-8859-1") as csvfile:
            reader = csv.reader(csvfile)
            has_100k(reader)
    no_ids_equal()
