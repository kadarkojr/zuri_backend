from flask import *
import time
import json
from datetime import datetime

#dt = datetime.datetime.fromtimestamp(time.time())

dt = datetime.fromtimestamp(time.time())
serialized_dt = dt.isoformat()


weekday = datetime.now().strftime('%A')



# Format the datetime in the desired format
formatted_datetime_str = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

appp = Flask(__name__)
appp.json.sort_keys = False

@appp.route('/api', methods=['GET'])
def home_page():
    user_query = str(request.args.get('user'))
    track_query = str(request.args.get('track'))

    data_set = {
        "slack_name" : f"{user_query}",
        "current_day" : weekday,
        "utc_time": formatted_datetime_str,
        "track" : track_query,
        "github_file_url" : "https://github.com/kadarkojr/zuri_backend/blob/main/internship/appp.py",
        "github_repo_url" : "https://github.com/kadarkojr/zuri_backend",
        "status_code" : 200
        
    }
    # Use jsonify to convert the dictionary to a JSON response
    #json_dump = json.dumps(data_set)
    response = jsonify(data_set)
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
    appp.run()
