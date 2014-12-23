import csv

from django.core.management.base import BaseCommand, CommandError
from torrent.models import Torrent

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        with open("/home/dlemos/tmpfs/tmp/torrents_mini.csv") as csvfile:
            #reader = csv.reader(csvfile, delimiter='|', quotechar='"')
            try:
                #for row in reader:
                torrents = []
                for line in csvfile:
                    rows = line.split('|')
                    if len(rows) != 7:
                        continue
	            torrent = Torrent(
                        name = rows[0],
                        size= rows[1],
                        hash = rows[2],
                        num_files = rows[3],
                        category = rows[4]
	            )
	            torrents.append(torrent)
                Torrent.objects.bulk_create(torrents)
            except Exception, e:
		import pdb; pdb.set_trace()
