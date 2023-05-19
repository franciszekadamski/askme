#!/usr/bin/python3

import json
import os 
import jellyfish
import random
import argparse
import pickle 
import time

__doc__ = """
Library module for askme.py app
Functions:
    read(filename="data.json", ftype="json")
    write(data, filename="data.json", ftype="json")
    json_to_pickle(filename_json="data.json", filename_pickle="data.pkl")
    multiline_input(title="")
"""

def read(filename="data.json", ftype="json"):
    """Reads file of type defined in ftype
    Parameters: 
        filename : str
        ftype : str
    Output: 
        content : container type
    """
    if ftype == "json":
        with open(filename, "r") as f:
            content = json.load(f)
        return content 
    elif ftype == "pkl" or ftype == "pickle":
        with open(filename, "rb") as f:
            content = pickle.load(f)
        return content 
    else:
        raise Exception("'ftype' parameter has to be 'json', 'pkl' or 'pickle'")
            
def write(data, filename="data.json", ftype="json"):
    """Writes to file of type defined in ftype
    Parameters: 
        data : container, 
        filename : str
        ftype : str
    Output: 
        None
    """
    if ftype == "json":
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    elif ftype == "pkl" or ftype == "pickle":
        with open(filename, "wb") as f:
            pickle.dump(data, f)
    else:
        raise Exception("'ftype' parameter has to be 'json', 'pkl' or 'pickle'")
    
def json_to_pickle(filename_json="data.json", filename_pickle="data.pkl"):
    """Reads json file and writes content to pickle
    Parameters:
        filename_json : str
        filename_pickle : str
    Output: 
        None
    """
    content = read(filename_json, "json")
    write(content, filename_pickle, "pickle")

def ask_to_pickle(filename="test.ask"):
    data = []
    key = "question"
    question_and_answer = {"question" : "", "answer" : ""}
    cell_content = ""
    
    with open(filename, "r") as f:
        lines = f.readlines()
        f.close()

    for line in lines:
        if "---" in line and key == "question":   
            question_and_answer[key] = cell_content
            cell_content = ""   
            key = "answer"
            continue

        if "---" in line and key == "answer":
            data.append(question_and_answer)
            question_and_answer[key] = cell_content
            question_and_answer = {"question" : "", "answer" : ""}
            cell_content = ""
            key = "question"
            continue

        cell_content += line
                 
    write(data, filename[:-4] + ".pkl", "pickle") 
         
# other
def multiline_input(title=""):
    """Reads lines of input from user until 'f\n' is the only content of a line
    Parameters: 
        title : str
    Output:
        None
    """
    print(title)
    content = ""
    while True:
        line = input()
        if line == "":
            break
        content += line + "\n"
    return content

