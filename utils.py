from datetime import datetime, timedelta
from pymongo.errors import DuplicateKeyError
from pymongo import UpdateOne

def publishedDateTime(delta=0):
    time_diff = datetime.now() - timedelta(seconds=delta)
    return time_diff.strftime("%Y-%m-%dT%H:%M:%SZ")

def fetch_yt_and_save(youtube, topic, collection):
    
    published_after = publishedDateTime(300) # for first video in database fetching from five mins ago
    
    last_video = list(collection.find().sort("publishedAt", -1).limit(1))

    if len(last_video):
        published_after = last_video[0]["publishedAt"]
        
    print("Published after = " + published_after)
        
    request = youtube.search().list(
        order="date",
        part="snippet",
        maxResults=10,
        q=topic,
        videoLicense="any",
        publishedAfter=published_after
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
            task = collection.bulk_write(operations)
            print("Operations done in database")
            print(task)

    return response
