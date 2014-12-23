import urllib

from django.contrib import admin
from torrent.models import Torrent

from django.template.defaultfilters import filesizeformat

class TorrentAdmin(admin.ModelAdmin):

    search_fields = ['name']

    def torrent_url(self, obj):
        return '<a href="http://torcache.net/torrent/%s.torrent" target="_blank">get torrent</a>' % obj.hash.upper()
    torrent_url.allow_tags=True

    def file_size(self, obj):
       return filesizeformat(obj.size)

    #def magnet_url(self, obj):
    #    
    #    return '<a href="magnet:?xt=urn:btih:%(hash)s&amp;%(params)s" target="_blank">magenet link</a>' % {
    #        'hash': obj.hash.upper(),
    #        'params': urllib.urlencode({
    #            'dn': obj.name.encode('utf-8'),
    #            'xl': obj.size,
    #            'dl': obj.size
    #        })
    #    }

        
    #magnet_url.allow_tags=True
    torrent_url.allow_tags=True

#TorrentAdmin.list_display += ('file_size', 'magnet_url', 'torrent_url')
TorrentAdmin.list_display += ('file_size', 'torrent_url')

admin.site.register(Torrent, TorrentAdmin)
