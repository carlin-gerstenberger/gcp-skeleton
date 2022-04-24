from flask import Flask
from flask_restful import Api
from bq import bq


app = Flask(__name__)
api = Api(app)

query = '''
        SELECT geo.country AS country, COUNT(DISTINCT user_pseudo_id) AS count
        FROM `podcastapp-767c2.analytics_193436959.events_*` 
        WHERE device.operating_system = 'IOS'
        GROUP BY geo.country
limit 100;
'''

@app.route("/")
def home():
    return bq(query)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
