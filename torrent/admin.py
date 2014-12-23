from django.contrib import admin
from torrent.models import Torrent

class TorrentAdmin(admin.ModelAdmin):

    search_fields = ['name']

    def torrent_url(self, obj):
        return '<a href="http://torcache.net/torrent/%s.torrent">get torrent</a>' % obj.hash
    torrent_url.allow_tags=True


TorrentAdmin.list_display += ('torrent_url',)

admin.site.register(Torrent, TorrentAdmin)
