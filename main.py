import argparse
from anilist import get_list, trim_list
import myanimelist

def test_loadFile(filepath):
    with open(filepath, 'r') as file:
        return json.loads(file.read())

def test_write_json(content, path):
    import json
    with open(path, 'w') as file: file.write(json.dumps(content,
                                                        indent=4,
                                                        sort_keys=True))

def test_write(content, path):
    with open(path, 'w') as file: file.write(content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Generate an importable xml file for MyAnimeList from AniList')
    parser.add_argument('anilist_user', help='Username on AniList')
    parser.add_argument('mal_user', help='Username on MyAnimeList')
    parser.add_argument('-o', '--out', help='Write to file instead of stdout',
                        dest='path')
    args = parser.parse_args()

    d = trim_list(get_list(args.anilist_user))
    mde = myanimelist.malDataExport(d)
    if args.path is not None:
        test_write(str(mde.mal_skeleton(args.mal_user)), args.path)
    else: print(mde.mal_skeleton(args.mal_user))
