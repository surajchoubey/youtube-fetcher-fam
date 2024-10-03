from datetime import datetime, timedelta

def publishedDateTime(delta=0):
    time_diff = datetime.now() - timedelta(days=delta)
    return time_diff.strftime("%Y-%m-%dT%H:%M:%SZ")

def fetch_yt_and_save(youtube, topic, collection):
    published_after = publishedDateTime(1)
    request = youtube.search().list(
        order="date",
        part="snippet",
        maxResults=10,
        q=topic,
        videoLicense="any",
        publishedAfter=published_after
    )
    
    response = request.execute()

    videos = []
    if "items" in response:
        for item in response["items"]:
            video_info = {
                'videoId': item['id']['videoId'],
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'publishedAt': item['snippet']['publishedAt'],
                'channelTitle': item['snippet']['channelTitle'],
                'thumbnail': item['snippet']['thumbnails']['default']['url'],
                'createdAt': publishedDateTime()
            }
            videos.append(video_info)
        
        collection.insert_many(videos)
    return response