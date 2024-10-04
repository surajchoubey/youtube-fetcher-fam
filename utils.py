from datetime import datetime, timedelta
from pymongo.errors import DuplicateKeyError
from pymongo import UpdateOne

def publishedDateTime(delta=0):
    time_diff = datetime.now() - timedelta(seconds=delta)
    return time_diff.strftime("%Y-%m-%dT%H:%M:%SZ")

def fetch_yt_and_save(youtube, topic, collection):
    published_after = publishedDateTime(10)
    published_before = publishedDateTime()
    request = youtube.search().list(
        order="date",
        part="snippet",
        maxResults=10,
        q=topic,
        videoLicense="any",
        publishedAfter=published_after,
        publishedBefore=published_before
    )
    
    response = request.execute()

    if "items" in response:
        videos = []
        for item in response["items"]:
            video_info = {
                '_id': item['id']['videoId'],
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'publishedAt': item['snippet']['publishedAt'],
                'channelTitle': item['snippet']['channelTitle'],
                'thumbnail': item['snippet']['thumbnails']['default']['url'],
                'createdAt': publishedDateTime()
            }
            videos.append(video_info)
        
        operations = []

        for video in videos:
            operations.append(
                UpdateOne(
                    {"_id": video["_id"]},
                    {"$set": video},
                    upsert=True
                )
            )

        if len(operations) > 0:
            collection.bulk_write(operations)

    return response
