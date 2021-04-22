import requests
import json

class lolData(): 
    def __init__(self):
        print("Class Started")

    def getLeagues(self):
        url = 'https://esports-api.lolesports.com/persisted/gw/getLeagues?hl=en-US'

        req = requests.get(url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"})
        reqJson = req.json()

        return reqJson

    def getSchedule(self, leagueIDs):
        schedule = {}
        
        for leagueID in leagueIDs:
            url = 'https://esports-api.lolesports.com/persisted/gw/getSchedule?hl=en-US&leagueId='
            url+=leagueID

            req = requests.get(url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"})
            reqJson = req.json()

            #return reqJson

            leagueData = reqJson['data']['schedule']['events']
            for eventData in leagueData:
                date = eventData['startTime']
                date = date[0:10]
                league = eventData['league']['name']
                blockName = eventData['league']['name']+' '+eventData['blockName']
                matchID = eventData['match']['id']
                if not schedule.get(blockName):
                    schedule[blockName] = {}

                if not schedule[blockName].get(date):
                    schedule[blockName][date] = {}

                if not schedule[blockName][date].get(matchID):
                    schedule[blockName][date][matchID] = {}

                teamData = eventData['match']['teams']
                for team in teamData:
                    teamName = team['name']
                    teamImage = team['image']
                    try:
                        wins = team['result']['gameWins']
                    except:
                        wins = '-'
                    try:
                        result = team['result']['outcome']
                    except:
                        result = '-'
                    if not schedule[blockName][date][matchID].get(teamName):
                        schedule[blockName][date][matchID][teamName] = {}

                    schedule[blockName][date][matchID][teamName] = {
                        "image":teamImage,
                        "wins":wins,
                        "result":result
                    }

        return schedule
    
    def getMatchDetails(self, matchID):
        url = 'https://esports-api.lolesports.com/persisted/gw/getEventDetails?hl=en-US&id='+matchID
        print(url)

        req = requests.get(url, headers={"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"})
        reqJson = req.json()

        return reqJson