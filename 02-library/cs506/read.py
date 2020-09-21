import csv
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    check = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final = []
    f = open(csv_file_path)
    readFile = csv.reader(f)
    for row in readFile:
        for i in range(len(row)):
            if row[i] not in check:
                row[i] = int(row[i])
        final+=[row]
    return final
