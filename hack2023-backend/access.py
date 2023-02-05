import requests
import json

headers = {
  "apikey": "e1fc82b0-a4c0-11ed-8b4b-37a0090fe976"}

host = 'https://app.sportdataapi.com/api/v1/soccer'

class SoccerStats:
  def __init__(self, country):
    self.country = country
  def getCountries(self, continent):
    response = requests.get(host + '/countries', headers=headers, params={'continent': continent})
    return json.loads(response.text)

  def getCountryID(self):
    response = requests.get(host + '/countries', headers=headers)
    data_dict = json.loads(response.text)

    for n in data_dict['data']:
      if n['name'] == self.country:
        return n['country_id']

#Player Specific Info
  def getPlayers(self):
    param_id = {"country_id": f"{self.getCountryID()}"}
    response = requests.get(host + '/players', headers=headers, params=param_id)
    return json.loads(response.text)

  def getSinglePlayer(self, firstname, lastname):
    origin = self.getPlayers()
    for n in origin['data']:
      if firstname == n['firstname'] and lastname == n['lastname']:
        if type(n['player_id']) is int:
          response = requests.get(host + '/players/' + f"{n['player_id']}", headers=headers, params={})
          return json.loads(response.text)
    return "Player ID not found for " + firstname + ' ' + lastname

  def getTopScorers(self, league_name):
    param_id = self.getSeasonID(league_name, self.country)
    response = requests.get(host+'/topscorers', headers=headers, params={param_id})
    return json.loads(response.text)

#Team Specific Info
  def getTeams(self):
    relevant = self.getCountryID()
    response = requests.get(host + '/teams', headers=headers, params={'country_id': f'{relevant}'})
    return json.loads(response.text)

  def getSingleTeam(self, name):
    relevant = self.getTeams()
    for n in relevant['data']:
      if n['name'] == name:
        response = requests.get(host + '/teams', headers=headers, params={'team_id': f"{n['team_id']}"})
        return json.loads(response.text)

#League Specific Info
  def getLeagues(self, **kwargs):
    #param_id = {'country_id' : f'{self.getCountryID(country)}'}
    response = requests.get(host + '/leagues', headers=headers, params=kwargs)
    return json.loads(response.text)

  def getLeagueID(self, league_name):
    valid_leagues = self.getLeagues(country_id=self.getCountryID())
    for n in valid_leagues['data']:
      if n['name']==league_name:
        return n['league_id']

  def getLeagueStandings(self, league_name):
    param_id = {'league_id':f'{self.getLeagueID(league_name)}'}
    response = requests.get(host+'/standings', headers=headers, params=param_id)
    return json.loads(response.text)

#Season specific Info
  def getSeasons(self, league_ID:int):
    # param_id = {'league_id': f'{self.getLeagueID(league_name, country)}'}
    response = requests.get(host + '/seasons', headers=headers, params={'league_id': f'{league_ID}'})
    return json.loads(response.text)

  def getSeasonID(self, league_name):
    for n in self.getSeasons(self.getLeagueID(league_name))['data']:
      if n['name'] == league_name:
        return n['season_id']

#Match specific Info
  def getMatch(self, season_ID, **kwargs):
    param_id = {'season_id': season_ID}
    for k, i in kwargs.items():
      param_id[k] = i
    response = requests.get(host+'/matches', headers=headers, params=param_id)
    return json.loads(response.text)

  def getMatchID(self, season_ID):
    for n in self.getMatch(season_ID)['data']:
      if n['season_id'] == season_ID:
        return n['match_id']
    return "match ID not found, we are either not subscribed or it does not exist."

#prematch odds for a match
#currently for random matches only
  def getOdds(self, strExpected, **kwargs):
    response = requests.get(host+'/odds', headers=headers, params={'type': strExpected})
    return json.loads(response.text)
# if __name__ == "__main__":
#   #test
#   print(self.getLeagues("Hungary"))
