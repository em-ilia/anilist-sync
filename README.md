# A utility to sync anilist with other similar websites
I only use Anilist and MAL, but I tried to write this such that I could sync to a site like anidb in the future if I feel like it.
Note: This is meant to have anilist be used as the primary list, with other websites being used as clones of anilist.


## APIs Used
- Anilist
	Anilist supplies a GraphQL API. [Link](https://github.com/AniList/ApiV2-GraphQL-Docs)
- MyAnimeList
	While MyAnimeList has its own API, part of the motivation for this project is avoiding frequent down times. Jikan seems good, but it has very restrictive rate limits. [Link](https://jikan.moe/)
	Funnily enough, Anilist's API also stores the MyAnimeList id for each entry, meaning that Anilist actually provides the best API for MAL. Nice.

## Dependencies
- Requests
	This project doesn't really need anything else. All of my systems have this installed globally anyway since it's a pretty common package.

## Usage
### MyAnimeList
If one really wanted, you could use the official MyAnimeList API to automatically upload and modify your list, but I'm pretty sure you would have to create an API token. Instead, take the XML file generated and upload it to [here](https://myanimelist.net/import.php).
