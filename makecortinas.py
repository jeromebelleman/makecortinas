'''
Make cortinas
'''

import os
import subprocess
from gi.repository import Nautilus, GObject


def makecortinas(_, files):
    '''
    Make cortinas
    '''

    for fle in files:
        path = fle.get_location().get_path()
        root, _ = os.path.splitext(path)
        args = ['ffmpeg',
                '-t', '30',
                '-y',
                '-i', path,
                '%s-cortina.mp3' % root,
               ]
        subprocess.Popen(args)


class MakeCortinas(GObject.GObject, Nautilus.MenuProvider):
    '''
    Menu provider
    '''

    def get_file_items(self, _, files): # pylint: disable=arguments-differ
        for fle in files:
            if fle.get_mime_type().split('/')[0] != 'audio':
                return

        item = Nautilus.MenuItem(name='Nautilus::makecortinas',
                                 label='Make Cortinas')
        item.connect('activate', makecortinas, files)
        return item,
