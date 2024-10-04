from flask import Flask, jsonify, request
from fetch_youtube import fetch_results, fetch_from_collection
from flask_cors import CORS
from time import sleep
import os

app = Flask(__name__)
CORS(app)

@app.route('/trigger', methods = ['POST'])
def trigger_youtube_and_save():
    topic = 'football'
    i = 6
    try:
        while i > 0:
            fetch_results(topic, i)
            sleep(10)
            i -= 1
        return jsonify({ "success": True })
    except:
        return jsonify({ "success": True })

@app.route('/', methods=['GET'])
def fetch_from_database():

    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    search_text = request.args.get('search_text', None)
    before_date = request.args.get('before_date', None)
    after_date = request.args.get('after_date', None)
    sortby = int(request.args.get('sortBy', -1))
    
    print(before_date, after_date)

    videos, total_count = fetch_from_collection(page, page_size, search_text, before_date, after_date, sortby)

    total_pages = (total_count + page_size - 1) // page_size

    return jsonify({
        "videos": videos,
        "page_size": len(videos),
        "total_count": total_count,
        "total_pages": total_pages,
        "current_page": page,
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5001)))

