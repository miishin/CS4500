#!/usr/bin/env/ python3
import json

# xjson.py replicates the functionality of the "C" assignment


# Takes in a list of JSON values and returns a JSON object with
# The form: {count:x, seq:[a,b,c...]}, where x is the number of
# JSON values, and [a,b,c..] is a JSON list of all the JSON values
def formCountSeq(jsonvalues):
    countseq = {}
    countseq["count"] = len(jsonvalues)
    countseq["seq"] = jsonvalues
    return json.dumps(countseq)


# Takes in a list of JSON values and returns a JSON list with the form:
# [count, a, b, c...] where count is the number of JSON values, and
# the rest of the list is the original list of JSON values but reversed
def formCountRev(jsonvalues):
    countrev = []
    countrev.append(len(jsonvalues))
    countrev += jsonvalues[::-1]
    return json.dumps(countrev)


# Returns a JSON string of the full response (what will be sent over TCP)
def formFullResponse(jsonvalues):
    response = ""
    response += formCountSeq(jsonvalues)
    response += formCountRev(jsonvalues)
    return response

