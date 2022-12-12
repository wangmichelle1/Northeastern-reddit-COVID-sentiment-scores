'''
     Michelle Wang 
     sentiment.py
     Goal -- determine sentiment score and average score of reddit comments 
     during covid times; display a scatterplot with the sentiment scores 
'''
import matplotlib.pyplot as plt

REDDIT = "reddit.txt"

POSITIVE = ["good", "ok", "amazing", "safe", "ready", "happy", "finally",
            "relief", "relieved", "like", "love", "great", "mild"]
NEGATIVE = ["bad", "unsafe", "upset", "sad", "wait", "waited", "scared",
            "scary", "scaring", "premature", "hate", "hated", "worried",
            "weird", "concern", "concerned", "lmao", "isolation", "trouble",
            "contagious"]


def read_file(filename):
    ''' Function: read_file
        Parameters: name of a file, a string
        Return: a list of strings   
    '''
    comments = []

    with open(filename, "r", encoding="utf-8") as infile:
        lines = infile.readlines()
        lines = [w.strip() for w in lines]
        for i in range(4, len(lines), 6):
            comments.append(lines[i])

    return comments


def comment(comment_lst):
    ''' Function: comment
        Parameters: 1d lst of one comment   
        Return: 1d list of one comment with no punctuation and all lower case
    '''
    output_st = ""
    letters = []
    
    for word in comment_lst:
        for letter in word: 
            if letter.isalpha() or letter == " ":
                output_st = output_st + letter.lower()
    letters.append(output_st)
    
    return letters 

    
def clean_lst(comments):
    ''' Function: clean_lst
        Parameters: 2d list of strings that are all lower cased but has punct
        Return: 2d list of strings that are cleaned - lower cased and no punct
    '''
    clean_twod = []

    for lst in comments: 
        clean = comment(lst)
        clean_twod.append(clean)
    
    return clean_twod


def sentiment_score(comment_lst, pos, neg):
    ''' Function: sentiment_score
        Parameter: comment_lst, a 1d list of cleaned strings, and two lists 
        rep the positive/negative words
        Returns: sentiment score, a float
    '''    
    score = 0

    for item in comment_lst:
        clean_word = item.split()
        
        for word in clean_word:
            if word in pos: 
                score = score + 1
            if word in neg:
                score = score - 1 
        scores = score / len(clean_word) 
        
    return scores


def sentiment_scores(comment_lsts, pos, neg): 
    ''' Function: sentiment_scores
        Parameters: comment_lsts, 2d list of cleaned strings 
        Returns: 1d list of all the scores for all comments (strings) 
    '''
    scores = []
    
    for comment_lst in comment_lsts:
        score = sentiment_score(comment_lst, pos, neg)
        scores.append(score)
        
    return scores 


def sct_plot(sentiment_lst):
    ''' Function: sct_plot
        Parameters: sentiment_lst, a 1d list of scores
        Return: nothing, just a plot of sentiment scores against position 
    ''' 
    positive_scores = []
    negative_scores = []
    neutral_scores = []
    pos_positions = []
    neg_positions = []
    neu_positions = []
    
    sentiment_lst.reverse()
    
    for i in range(len(sentiment_lst)):
        if sentiment_lst[i] > 0:
            positive_scores.append(sentiment_lst[i])
            pos_positions.append(i)
        
        elif sentiment_lst[i] < 0:
            negative_scores.append(sentiment_lst[i])
            neg_positions.append(i)
        
        else:
            neutral_scores.append(sentiment_lst[i])
            neu_positions.append(i)
    
    plt.scatter(pos_positions, positive_scores, color = "green", 
                label = "positive")
    plt.scatter(neg_positions, negative_scores, color = "red", 
                label = "negative")
    plt.scatter(neu_positions, neutral_scores, color = "yellow", 
                label = "neutral")
    
    plt.legend()

def main():
    # Get the data as a list from the file. 
    comments = read_file(REDDIT)

    # Get the clean 2d list of the data.  
    clean_str = clean_lst(comments)

    # Get the 1d list of sentiment scores using constant pos and neg words. 
    scores = sentiment_scores(clean_str, POSITIVE, NEGATIVE)
    # Compute average sentiment score. Print it out.     
    average = sum(scores) / len(scores)
    print("The average sentiment score of all comments is", round(average, 5))
        
    # Create a scatterplot, with the sentiment score against the position 
    # of the comment (from oldest to newest). 
    sct_plot(scores) 
    plt.title("Sentiment Scores Regarding Covid Annoucements")
    plt.xlabel("Comment Time from Oldest to Newest")
    plt.ylabel("Sentiment Score")
    
main()
