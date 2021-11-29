import os
import glob

def writeCSV(data, fileName):
    
    numCol = len(data[0])-1
    with open(fileName, "w") as file:     
        for row in data:
            count = 0
            for word in row:
                if count == numCol: # if this is true, we have started a new row
                    file.write(word + "\n")
                else:
                    file.write(word + ",")
                    count += 1
    f = fileName
    return f



def readFromTXT(filename):
    with open(filename) as f:
        lines = f.readlines()

    data = []

    for l in lines:
        data.append(l.split())
    return data

if __name__ == '__main__':
    
    print("\n[Script Running]")
    
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    # we do this so that this script can work in any directory...

    outputDir = "output/" # output location is a file back, and then in 'ouput'
    outputDir = os.path.join(script_dir, outputDir)

    inputDir = "txts/"
    inputDir = os.path.join(script_dir, inputDir)
    
    # first we delete all files in the output directory
    # we only want the output of one pdf at a time...
    print("\n[Deleting Old Outputs]")
    
    files = glob.glob(outputDir+"*.csv")
    for f in files:
        os.remove(f)
    
    print("[Deletion Completed]")

    files = glob.glob(inputDir+"*.txt")

    print("\n[Processing txt files]:")
    for f in files:
        data = readFromTXT(f)

        name = os.path.basename(f)
        newName = name[:-4]
        writeCSV(data, outputDir+newName+".csv")
        
        print("-\t" + newName)

    print("\n[Script Completed]")


      

