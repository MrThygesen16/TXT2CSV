from array import array
import os
import glob

# function that writes the data to the csv files
def writeCSV(data: array, fileName: str) -> str:
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


# function to read data from txt files
# return an array
def readFromTXT(filename: str) -> array:
    with open(filename) as f:
        lines = f.readlines()

    data = []

    for l in lines:
        data.append(l.split())
    return data


# function to delete old files
def deleteOldFiles(files: str):
    print("\n[Deleting Old Outputs]")
    for f in files:
        os.remove(f)
    print("[Deletion Completed]")


# function for processing the files
def processFiles(files: str, outputDir: str):
    print("\n[Processing txt files]:")
    for f in files:
        data = readFromTXT(f)

        name = os.path.basename(f)
        newName = name[:-4]
        
        # call write csv function
        writeCSV(data, outputDir+newName+".csv")
        
        print("-\t" + newName)
    print("\n[Processing Completed]")


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
    
    files = glob.glob(outputDir+"*.csv")
    deleteOldFiles(files)
    
    files = glob.glob(inputDir+"*.txt")
    processFiles(files, outputDir)