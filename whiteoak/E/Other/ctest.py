#!/usr/bin/env/ python3
import xjson, jsonparse, sys

# When ctest.py is given a filename, it will run the "C" program on that .json input
# and then create an output .json file. Naming convention will be:
# name.json -> name-output.json
def main():
    inputfile = sys.argv[1]
    values = jsonparse.read_file(inputfile)
    countseq = xjson.formCountSeq(values)
    countrev = xjson.formCountRev(values)

    extensionindex = inputfile.find(".json")
    if extensionindex != -1:
        newfilename = inputfile[0:extensionindex] + "-output.json"
        file = open(newfilename,'w')
        file.write(countseq)
        file.write(countrev)
    else:
        print("input wasn't a .json")
        sys.exit(1)


if __name__ == "__main__":
    main()