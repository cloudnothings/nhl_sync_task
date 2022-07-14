import json

import requests


# TODO: Implement convert json data to csv. Time will tell if Google Sheets can take a csv through API
def json_to_csv(data):
    """Will convert json to csv"""
    return 'results.csv'


def get_match_data(club_id):
    """Returns json of last 5 games of specified club_id"""
    print(f'Getting last 5 matches of club {club_id}')
    _url = 'https://proclubs.ea.com/api/nhl/clubs/matches'
    _query = f'?clubIds={club_id}&platform=xbox-series-xs&matchType=club_private'
    _headers = {  # user agent of browser seems to work
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    _response = requests.get(_url + _query, headers=_headers)
    if _response.status_code == 200:
        print("Request successful")
        return json.loads(_response.content)
    else:
        print('Error')
        exit(1)


def get_data_all_clubs():
    """Returns json obj of last 5 matches of all clubs in CLUB_IDS"""
    _results = get_match_data(CLUB_IDS[0])
    if len(CLUB_IDS) > 1:
        for i in range(1, len(CLUB_IDS)):
            _results += get_match_data(CLUB_IDS[i])
    return _results


def sync_nhl_data():
    """Intended use is as follows:
    1. Periodically pulls recent matches from all defined clubs as json
    2. Process the json to get only necessary data
    3. Upload data to Google Sheets API"""
    _data = get_data_all_clubs()
    # TODO: Implement json to csv function
    _data = json.dumps(_data)  # data = json_to_csv(data)
    # TODO: Implement API call to send csv to Google Sheets, or update cells programmatically


CLUB_IDS = [
    '21230'  # ,
    # '69420',
    # '696969,
    # '611275'
]
print(f'Clubs defined in your list: {CLUB_IDS}')
data = get_data_all_clubs()
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    print('Saved response as data.json')
