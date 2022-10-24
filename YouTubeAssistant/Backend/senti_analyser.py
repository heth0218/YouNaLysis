from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
def sentiment_analysis(comments=[]):
    sia = SentimentIntensityAnalyzer()
    nLikes = 0
    nComp = 0
    l = []
    r = []
    for x in range(0, len(comments)):
        d = sia.polarity_scores(comments[x]["text"])
        nComp+=d["compound"]*(comments[x]["likes"]+1)
        nLikes+=comments[x]["likes"]+1
        #print("Likes",comments[x]["likes"])
        for x in range(0, len(comments)):
                d = sia.polarity_scores(comments[x]["text"])
                l.append(d)
                nComp+=d["compound"]*(comments[x]["likes"]+1)
                nLikes+=comments[x]["likes"]+1
                print("Likes",comments[x]["likes"])
                for y in range(0,comments[x]["likes"]+1):
                    if d["compound"] <= 0.2 and d["compound"] > -0.2:
                        
                        r.append("Neutral")
                    elif d["compound"] > 0.2:
                        r.append("Positive")

                    else:
                        r.append("Negative")

        print("R: ",r)        
        comment_dict = pd.Series(l)        
        comment_label = pd.Series(r)        
        nCumm = (nComp)/nLikes        
                
        neutral = len(comment_dict[comment_label == "Neutral"])
        positive = len(comment_dict[comment_label == "Positive"])
        negative = len(comment_dict[comment_label == "Negative"])        
  
        nCumm = (nComp)/nLikes
            
        d = {
            "Neutral": neutral,
            "Positive": positive,
            "Negative": negative,
            "Cumulative":nCumm
                }
        print("D: ",d)
        return d