#!/usr/bin/env/ python3
import json, os, io
# jsonparse.py contains functionality to read in JSON values from
# some input stream.
#https://stackoverflow.com/questions/6886283/how-i-can-i-lazily-read-multiple-json-values-from-a-file-stream-in-python


# Reads in a file object that contains JSON values and reads them out one by one
# This function is a generator, which means that it outputs something very similar
# to a list of all the JSON values
def read_json(stream):
    position = 0
    while True:
        try:
            value = json.load(stream) # this will only succeed at the last JSON value
            yield value
            return
        except json.JSONDecodeError as err:
            stream.seek(position) # find our current position in the stream (usually file)
            value = json.loads(stream.read(err.pos)) # read up to the error, then take out JSON value
            position += err.pos # move up in the file
            yield value


# Given some input stream, takes in JSON values and
# returns a proper list of JSON values.
# Used as a wrapper of sorts for read_json
def get_json(stream):
    jsonvalues = []
    for value in read_json(stream):
        jsonvalues.append(value)
    return jsonvalues


# Reads in a file (not needed for E, but needed for C)
# After reading it in, it parses the JSON values in the file and returns a list
# of all the individual JSON values
def read_file(filename):
    jsonvalues = []
    if os.path.getsize(filename):
        file = open(filename, 'r')
        jsonvalues = get_json(file)
    return jsonvalues


# Reads in a string representing JSON value(s), and turns it into a
# list of JSON values (converts string to a file object for code above)
def read_json_string(jsonstr):
    if jsonstr == "":
        return []
    f = io.StringIO(jsonstr)
    return get_json(f)


# Reads in a list of JSON values and returns a string representation of those values
def return_json_string(jsonvalues):
    jsonstring = ""
    for value in jsonvalues:
        jsonstring += json.dumps(value)
    return jsonstring