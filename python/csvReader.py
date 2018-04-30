# Axioms about input (CSV) data:
#
# 1.) If a value has a ',' '\r' or '\n', the value has quotes around it
# 2.) Values cannot tcontain a '"' in the actual data

import sys

# Global variables
buffer = ""
waitingForEndQuote = False
maxBufferLen = 1000
numColumns = 50 # CSV has 50 columns
bufferIndex = 0
records = None

# Create a new set of records
#
# Records is an array of arrays of strings, e.g.:
#
# [
#    ["this", "is", "an"],
#    ["example", "of", "records"],
# ]
def createNewRecords():
    global records
    records = []
    records.append([])
    return

# This function is called when the buffer length exceeds maxBufferLen.
# This function prints an error and then terminates execution
def bufferLimitExceededExit():
    global maxBufferLen, buffer
    sys.stderr.write('Buffer limit of ' + str(maxBufferLen) + " exceeded\n")
    sys.stderr.write('Buffer contents:\n\n' + buffer + "\n")
    sys.exit()

# Add the byte to the buffer
def addByteToBuffer(byte):
    global buffer
    if (len(buffer) == 999):
        bufferLimitExceededExit()
    buffer += str(byte)
    return

def incrementBufferIndex():
    global bufferIndex, numColumns
    if (bufferIndex == (numColumns - 1)):
        bufferIndex = 0
    else:
        bufferIndex += 1

# Add the contents of the buffer to the records as a value
def addBufferAsValue():
    global records, numColumns
    currInd = len(records) - 1
    lastValueInd = len(records[currInd])
    if (lastValueInd == numColumns):
        records.append([])
        currInd += 1
    records[currInd].append(buffer) # append to records
    clearBuffer() # clear the buffer
    return

# Clear the buffer
def clearBuffer():
    global buffer
    buffer = ""
    return

# Process a byte
def processByte(byte):
    global waitingForEndQuote
    if (byte == ','):
        if (waitingForEndQuote != True):
            addBufferAsValue()
        else:
            addByteToBuffer(byte)
    elif (byte == '"'):
        if (waitingForEndQuote):
            waitingForEndQuote = False
        else:
            waitingForEndQuote = True
    elif (byte == '\r'):
        return
    elif (byte == '\n'):
        if (waitingForEndQuote):
            addByteToBuffer(byte)
        else:
            addBufferAsValue()
    else:
        addByteToBuffer(byte)
    return

def validateRecords():
    global records, numColumns
    errorsFound = False
    
    for i in range(0, numColumns):
        if (len(records[i]) != numColumns):
            print("validateRecords: Error found: len(records[" + str(i) + "]) = " + len(records[i]))
            errorsFound = True

    if not errorsFound:
        print("All records have the correct number of columns")
    return

file = open("./path/file.csv")

# Create a new records
createNewRecords()

while True:
    byte = file.read(1)
    if not byte:
        break
    else:
        processByte(byte)

print(str(len(records)) + " lines found")
validateRecords()