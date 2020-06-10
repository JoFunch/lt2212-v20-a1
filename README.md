# LT2212 V20 Assignment 1


Part 1 
The initial part and pre-processing part was done through the use of a dictionary. 
Through my sparring with my class-mates I heard use of different data structures, but I eventually 
found the dictionary to be the most intuitive one. There has not been much other preprocessing done 
to the corpus as the task excluded the use of libraries providing such tools like SPACY, NLTK, etc. 
The only real preprocessing done is converting alpha-words (cap-initial words) to lower, which in
theory would yield some discrepancy, but nothing too disturbing of the result. There are also a
visual amount of clitics and genitives, but likewise not something that completely disturbs the 
data.

Part 2
The visualisation part of the assignment was successfully done, 
however, I did explore some weird graphics when running in the script
in my text editor wherefore i at times was presented line charts rather than bar-charts.

Let me know if this does this to yours as well as a solution how to fix it.


Part 3

the TF-IDF yielded exactly the expected words; primarily the striking results are words pertaining
the two respective field's specialised vocabulary. Words like "wheat" and "oil" scored significant 
in the crude while having absolute absence the in grain, and so on.

Should this have been improved / changed in the preprocessing looking at the results, there should have been made a stop-word list
eliminating function words as they take up the majority of the space in the top TFIDF-score but seldom carry any real significance.

