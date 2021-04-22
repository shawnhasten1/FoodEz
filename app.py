import json

# Third Party
from flask import Flask, render_template, request, redirect, jsonify, session

# Internal Libraries are loaded after we set up logging
import data

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

lolData = data.lolData()

# A welcome message to test our server
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/getLeagues')
def getLeagues():    
    leagues = lolData.getLeagues()

    return jsonify(leagues)

@app.route('/api/v1/getSchedule')
def getSchedule():
    leagueIDs = request.args.get('league')
    leagueIDSplit = leagueIDs.split(',')
    leagues = lolData.getSchedule(leagueIDSplit)

    return jsonify(leagues)

@app.route('/api/v1/getMatchDetails')
def getMatchDetails():
    matchID = request.args.get('match')
    match = lolData.getMatchDetails(matchID)

    return jsonify(match)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(host="0.0.0.0", threaded=True, port=5002, debug=True)