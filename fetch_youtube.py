import os
import googleapiclient.discovery
from googleapiclient.errors import HttpError
from utils import fetch_yt_and_save
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://choubey:choubey@youtube.h68co.mongodb.net/?retryWrites=true&w=majority&appName=Youtube"
client = MongoClient(uri)
db = client["youtube_data"]
collection = db["search_results"]

DEVELOPER_KEYS = [
    "AIzaSyCP8eI247p6LMlhzWBtK1u_Qo70yKw4xd4",
    "AIzaSyAMQ89YuQaeW-eHFfLZOJVckLfj7nh_tGM",
    "AIzaSyB7RiMI7CDUr-j-FfpuzI7BGCb6RoRV8wQ",
]

def fetch_results(topic: str, delta: int):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    current_key_index = 0
    max_keys = len(DEVELOPER_KEYS)

    while current_key_index < max_keys:
        try:
            developer_key = DEVELOPER_KEYS[current_key_index]
            youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=developer_key)
            response = fetch_yt_and_save(youtube, topic, collection, delta)
            return response

        except HttpError as e:
            if e.resp.status == 403:
                current_key_index += 1
                continue

    return {}


    
def fetch_from_collection(page =1, page_size = 10, search_text = None, before_date = None, after_date = None, sortby = -1):
    
    if page <= 0: page = 1
    query = {}
    
    if search_text:
        keywords = '|'.join(search_text.split())
        print(keywords)
        query["$or"] = [
            {"title": {"$regex": keywords, "$options": "i"}},
            {"description": {"$regex": keywords, "$options": "i"}}
        ]
    
    if before_date:
        query["publishedAt"] = {"$lt": before_date}
    if after_date:
        query.setdefault("publishedAt", {})["$gt"] = after_date

    skip = (page - 1) * page_size
    cursor = collection.find(query).sort("publishedAt", sortby).skip(skip).limit(page_size)
    
    videos = []
    for document in cursor:
        videos.append({
            "videoId": document['videoId'],
            "title": document['title'],
            "description": document['description'],
            "publishedAt": document['publishedAt'],
            "channelTitle": document['channelTitle'],
            "thumbnail": document['thumbnail'],
            "createdAt": document['createdAt'],
        })
    
    total_count = collection.count_documents(query)
    
    return videos, total_count


# if __name__ == "__main__":
#     fetch_results("football")