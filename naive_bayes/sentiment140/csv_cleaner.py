import csv

num_files = 16
num_rows = 1600000
f_name = "tweetdata00.csv"

if __name__=='__main__':
    contents = []
    with open("training.1600000.processed.noemoticon.csv", "r", encoding="ISO-8859-1") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            contents.append(row)
    file_ind = 1
#row_per_File = len(contents)/num_files

    index = 0
    for i in range(num_files):
        f_name_list = list(f_name)
        if file_ind < 10:
            f_name_list[10] = str(file_ind)
        else:
            f_name_list[9] = str(file_ind)[0]
            f_name_list[10] = str(file_ind)[1]
            
        file_ind += 1
        f_name = ''.join(f_name_list)
        with open(f_name, "w") as csvfile:
            for i in range(index, index+(num_rows//num_files)//2):
                writer = csv.writer(csvfile, delimiter=',',quotechar='"')
                writer.writerow(contents[i])
                index+=1
            for i in range(num_rows-index, num_rows-index+(num_rows//num_files)//2):
                writer = csv.writer(csvfile, delimiter=',',quotechar='"')
                writer.writerow(contents[i])
            
