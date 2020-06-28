import os
import sys
import pandas as pd
import numpy as np
import numpy.random as npr
import grain, crude
import glob
import matplotlib.pyplot as plt
import math


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

print(dictionary_to_file('grain'))

def part1_load(folder1, folder2, n):
    # CHANGE WHATEVER YOU WANT *INSIDE* THIS FUNCTION.
    

    container1 = dictionary_to_file(folder1)
    container2 = dictionary_to_file(folder2)

    sum_of_directories = container1 + container2
    word_freq_df = pd.DataFrame(sum_of_directories)
    word_freq_df = word_freq_df.fillna(0)

    too_little = []
    for column in word_freq_df.columns[2:]:
        if word_freq_df[column].sum() <= n:
            too_little.append(column)

    
    filtered_df = word_freq_df.drop(columns=too_little)


    
    return filtered_df

 
# print(part1_load("grain", "crude", 25))




def part2_vis(df, m):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)

    
    df_sum_of_columns = df.sum()[2:]
    df_sorted = df_sum_of_columns.sort_values(ascending = False)
    df_higher_than_m = df_sorted[m:]
    final = df.drop(df_higher_than_m.index, 1)
    # print(final)
    dy = final.groupby(['classname']).sum().sort_values(final['classname'][0], axis=1, ascending=False)
    dx = final.groupby(['classname']).sum().sort_values(final['classname'][1], axis=1, ascending=False)
    # dy = df.groupby('classname').get_group('crude').drop(['classname','filename'],axis=1)
    # dx = df.groupby('classname').get_group('grain').drop(['classname', 'filename'],axis=1)
    plt.plot(dx, dy)
    plt.show()
    return (dy.T.plot(kind="bar"), dx.T.plot(kind="bar"))


part2_vis(part1_load('grain', 'crude', 100), 2)

def part3_tfidf(df):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)
    td_df = df.copy()

    for column in td_df:
        if column != "classname" and column != "filename": #avoid start columns otherwise error!
            term_frequency = td_df[column] # one series with term and all frequencies of corpus
            documents_without_term = term_frequency.isin([0]).sum() #Shown as bools --  with .sum() it becomes int.
            total_term_frequency = term_frequency.sum() # Get the total amount of frequency/occurrence in corpus
            # print(term_frequency)
            # print(documents_without_term)
            # print(total_term_frequency)
            # print(td_df[column])
            total_number_of_documents = len(td_df[column]) # kind of a troubled way to avoid 0-counts ... in combi with total_term_frequency
            idf = math.log(len(td_df) / (len(td_df) - documents_without_term)) # IDF formula with log
            td_df[column] = td_df[column] * idf #simple multiplication since I took Log in the previous


    return td_df #DUMMY RETURN


# print(part3_tfidf(part1_load('grain', 'crude', 20)))

# ADD WHATEVER YOU NEED HERE, INCLUDING BONUS CODE.



def part4_vis(df, m):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)

    
    df_sum_of_columns = df.sum()[2:]
    df_sorted = df_sum_of_columns.sort_values(ascending = False)
    df_higher_than_m = df_sorted[m:]
    final = df.drop(df_higher_than_m.index, 1)
    # print(final)
    dy = final.groupby(['classname']).sum().sort_values(final['classname'][0], axis=1, ascending=False)
    dx = final.groupby(['classname']).sum().sort_values(final['classname'][1], axis=1, ascending=False)
    # dy = df.groupby('classname').get_group('crude').drop(['classname','filename'],axis=1)
    # dx = df.groupby('classname').get_group('grain').drop(['classname', 'filename'],axis=1)
    plt.plot(dx, dy)
    plt.show()
    return (dy.T.plot(kind="bar"), dx.T.plot(kind="bar"))



print(part4_vis(part3_tfidf(part1_load('grain', 'crude', 20)), 10))













