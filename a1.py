import os
import sys
import pandas as pd
import numpy as np
import numpy.random as npr
import grain, crude
import glob

# ADD ANY OTHER IMPORTS YOU LIKE

# DO NOT CHANGE THE SIGNATURES OF ANY DEFINED FUNCTIONS.
# YOU CAN ADD "HELPER" FUNCTIONS IF YOU LIKE.

def dictionary_to_file(directory):
    proccessed_directory = []
    dir1 = glob.glob(directory+ "/*")
    for filename in dir1:
        file_content = {}
        file_content['filename'] = filename.split('/')[1]
        file_content['classname'] = filename.split('/')[0]
        with open(filename, "r") as myfile:
            content = myfile.readlines()
            words = []
            for line in content:
                for word in line.split():
                    if word.isalpha():
                        words.append(word.lower())
            for word in words:
                if word in file_content:
                    file_content[word] += 1
                else:
                    file_content[word] = 1
        proccessed_directory.append(file_content)
    return proccessed_directory

# print(dictionary_to_file('grain'))

def part1_load(folder1, folder2, n):
    # CHANGE WHATEVER YOU WANT *INSIDE* THIS FUNCTION.
    

    container1 = dictionary_to_file(folder1)
    container2 = dictionary_to_file(folder2)

    sum_of_directories = container1 + container2
    dataframe = pd.DataFrame(sum_of_directories)
    # print(dataframe)
    dataframe = dataframe.fillna(0)
    dataframe_final = dataframe.sum()
    n_above = []
    for word in list(dataframe_final.index[2:]):
        if dataframe_final[word] > n:
            n_above.append(word)
    # print(n_above)

    n_final = dataframe.drop(n_above, 1)
    # return n_final

    return n_final # DUMMY RETURN

def part2_vis(df):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)

    # CHANGE WHAT YOU WANT HERE
    return df.plot(kind="bar")

def part3_tfidf(df):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)

    # CHANGE WHAT YOU WANT HERE
    return df #DUMMY RETURN

# ADD WHATEVER YOU NEED HERE, INCLUDING BONUS CODE.
