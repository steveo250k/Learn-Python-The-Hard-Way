from os.path import exists

filename = "..\\Hospital_Quality\\data_files\\Hospital_Inpatient_Discharges_SPARCS_De-Identified_2012.csv"
if exists(filename):
    print "File exists."
    file_ptr = open(filename, 'r') # Opens a file for reading.
    print file_ptr.readline() # Read header.
    print file_ptr.readline() # Read 1st line of data.
    print file_ptr.readline() # Read 2nd line of data.
    print file_ptr.readline() # Read 3rd line of data.    
    print file_ptr.readline() # Read 4
    print file_ptr.readline() # Read 5
    print file_ptr.readline() # Read 6
    print file_ptr.readline() # Read 7
    print file_ptr.readline() # Read 8
    print file_ptr.readline() # Read 9
    print file_ptr.readline() # Read 10
    print file_ptr.readline() # Read 11
    print file_ptr.readline() # Read 12
    file_ptr.close() # Close an open file.
else:
    print filename + " not found."
