class malDataExport:
    # data can be the map from anilist.trimList
    def __init__(self, data):
        self.entries = []
        for x in data:
            self.entries.append(malEntry(x))

    def mal_skeleton(self, name):
        # chr(10) == '\n'
        return f"""<?xml version="1.0" encoding="UTF-8" ?>
		<myanimelist>
			<myinfo>
				<user_name>{name}</user_name>
				<user_export_type>1</user_export_type>
			</myinfo>
                            {chr(10).join(map(str,self.entries))}
			</myanimelist>
        """

class malEntry:
    def __init__(self, entry):
        self.id = entry['media']['idMal']
        self.progress = entry['progress']
        self.date_start = entry['startedAt']
        self.date_end = entry['completedAt']
        self.score = entry['score']
        self.status = entry['status']
        self.repeat_number = entry['repeat']
        self.comment = entry['notes']
        self.convert_status()
        self.convert_dates()

    def convert_status(self):
        switch = {
            'CURRENT': 'Watching',
            'PLANNING': 'Planning',
            'COMPLETED': 'Completed',
            'DROPPED': 'Dropped',
            'PAUSED': 'On-Hold',
            'REPEATING': 'Completed',
        }
        self.status = switch.get(self.status)

    def convert_dates(self):
        self.date_start = malEntry.convert_date(self.date_start)
        self.date_end = malEntry.convert_date(self.date_end)

    @staticmethod
    def convert_date(date):
        if date['year'] == None:
            return '0000-00-00'
        else:
            return '{}-{}-{}'.format(date['year'], date['month'], date['day'])

    def __str__(self):
        return f"""<anime>
    <series_animedb_id>{self.id}</series_animedb_id>
    <my_watched_episodes>{self.progress}</my_watched_episodes>
    <my_start_date>{self.date_start}</my_start_date>
    <my_finish_date>{self.date_end}</my_finish_date>
    <my_score>{self.score}</my_score>
    <my_status>{self.status}</my_status>
    <my_times_watched>{self.repeat_number}</my_times_watched>
    <my_tags><![CDATA[{self.comment}]]></my_tags>
    <update_on_import>1</update_on_import>
</anime>"""

    __repr__ = __str__
