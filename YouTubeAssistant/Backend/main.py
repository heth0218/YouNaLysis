from fastapi import FastAPI, Form, status
import requests
from pydantic import BaseModel
from fastapi import Body, FastAPI
from Youtubeassist import spy
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from senti_analyser import sentiment_analysis
app = FastAPI()

origins = ['*']


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Comm(BaseModel):
    comments: list

class Item(BaseModel):
    query: str
    df: dict


class Ents(BaseModel):
    query: list
    video_id: str


@app.get("/youtubeassist/get_unique_entities/{video_id}")
def get_unique_entities(video_id: str, status_code=status.HTTP_200_OK):
    obj = spy(video_id)
    k = obj.generate_df()
    unique = obj.get_unique_ents()
    return {
        "unique_ents": unique,
    }


"""
@app.get("/youtubeassist/wild_card")
def wild_card_search(item:Item,status_code=status.HTTP_200_OK):
    print(item.query)
    df=pd.DataFrame(item.df)
    print(df.head())
    return {
        'Text':'Ok'
    }
    
"""


@app.get("/youtubeassist/wild_card/{video_id}/{query}")
def wild_card(video_id: str, query: str, status_code=status.HTTP_200_OK):
    obj = spy(video_id)
    k = obj.generate_df()
    m = obj.wildcard_search(query)
    return m


@app.post("/youtubeassist/search_by_ents")
def search_by_ents(ents: Ents):
    obj = spy(ents.video_id)
    k = obj.generate_df()
    m = obj.search_by_ents(ents.query)
    return m


@app.get("/youtubeassist/sentiment/{video_id}")
def get_sentiment(video_id: str):
    obj = spy(video_id)
    obj.generate_df()
    k = obj.sentiment_analysis((-0.2, 0.2))
    d = {
        "Negative": k["Negative"],
        "Positive": k["Positive"],
        "Neutral": k["Neutral"],
        "label_stats": dict(obj.show_label_stats()),
    }
    return d

@app.post("/youtubeassist/comment_sentiment/{video_id}")
def get_comment_sentiment(video_id: str,comm: Comm):
    obj = spy(video_id)
    k = obj.comments_sentiment_analysis(comm.comments,(-0.2,0.2))
    print(k)
    return k

@app.post("/youtubeassist/sentiment_only/")
def get_sentiment(comm: Comm):
    sentiments = sentiment_analysis(comm.comments)
    return sentiments
    
