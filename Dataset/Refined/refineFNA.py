import sys

filePath = sys.argv[1]

with open(filePath, 'r') as myfile:
    data = myfile.readlines()
    data = [x.strip() for x in data]
    newData = ""
    for i in data:
        if (i[0] != ">"):
            for x in i:
                if (x == "A" or x == "T" or x == "G" or x == "C"):
                    newData = newData + x

    refFile = str(sys.argv[1]).replace(".fna", "") + "Refined" + ".txt"
    file = open(refFile, 'w')
    file.write(newData)
    file.close()
