from flask import Flask, jsonify, request, send_from_directory
from fetch_youtube import fetch_results, fetch_from_collection
from flask_cors import CORS
from threading import Thread
from time import sleep
import os

app = Flask(__name__, static_folder='build')
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/videos', methods=['GET'])
def fetch_from_database():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    search_text = request.args.get('search_text', None)
    before_date = request.args.get('before_date', None)
    after_date = request.args.get('after_date', None)
    sortby = int(request.args.get('sortBy', -1))

    videos, total_count = fetch_from_collection(page, page_size, search_text, before_date, after_date, sortby)

    total_pages = (total_count + page_size - 1) // page_size

    return jsonify({
        "videos": videos,
        "page_size": len(videos),
        "total_count": total_count,
        "total_pages": total_pages,
        "current_page": page,
    })

def trigger_youtube_and_save():
    while True:
        topic = 'football'
        print("Triggering YOUTUBE!")
        fetch_results(topic)
        sleep(10)

if __name__ == '__main__':
    thread = Thread(target=trigger_youtube_and_save)
    thread.daemon = True
    thread.start()
    
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5001)))
