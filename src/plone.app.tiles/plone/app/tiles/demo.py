from zope.interface import Interface
from zope import schema

from plone import tiles


class ITransientTileData(Interface):

    message = schema.TextLine(title=u"Test string")


class TransientTile(tiles.Tile):

    def __call__(self):
        return "<html><body><b>Transient tile %s</b></body></html>" % \
            self.data['message']


class IPersistentTileData(Interface):

    message = schema.TextLine(title=u"Persisted message")
    counter = schema.Int(title=u"Counter")


class PersistentTile(tiles.PersistentTile):

    def __call__(self):
        return "<html><body><b>Persistent tile %s #%d</b></body></html>" % \
            (self.data['message'], self.data['counter'],)
