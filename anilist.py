from pathlib import Path
import requests
import json

# user is the name of the user
# type is either "ANIME" or "MANGA"
def get_list(user, type = "ANIME", queries = None):
    if queries is None: queries = load_queries()
    variables = {
        'name': user,
        'type': type
    }
    url = 'https://graphql.anilist.co'
    r = requests.post(url, json={'query': queries['animelist'],
                                 'variables': variables})
    j = r.json()
    return r.json()

def trim_list(l, type = "anime"):
    unified_list = [y for x in
                            l['data']['MediaListCollection']['lists']
                            for y in x['entries']]
    return unified_list

def load_queries() -> {str: str}:
    query_dir = 'anilist_queries'
    queries = [x for x in Path(query_dir).iterdir() if x.suffix == '.query']
    return {query.stem: open(query).read() for query in queries}

if __name__ == '__main__':
    #queries = load_queries()
    #test_write(get_list('Darn', queries = queries), 'balls2')
    trim_list(get_list('Darn'))
