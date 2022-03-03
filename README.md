# TXT to CSV

This is a simple helper script that can be used to convert multiple text files, containing tables of data from PDF files into properly formatted CSV files. Trying to get a table from a PDF into Excel so that it is properly formatted can be a pain. This simple script intends to speed up that process.

To use, simply copy and paste the text data from some PDF or someplace else, and put it into a `.txt` file and place it in the `txts` folder. The name of this does not matter too much.

From there simply run the python script and the output folder will give the properly formatted CSV files to be used in Excel.

Below is an example of the script running for 4 text files. It notifies the user of where it is in the conversion porcess.

```
[Script Running]

[Deleting Old Outputs]
-       c:\Users\...\TextToCSV\output\page28.csv
-       c:\Users\...\TextToCSV\output\page30.csv
-       c:\Users\...\TextToCSV\output\page31.csv
-       c:\Users\...\TextToCSV\output\page32.csv
[Deletion Completed]

[Processing txt files]:
-       page28
-       page30
-       page31
-       page32
[Processing Completed]

[Script Finished]
```