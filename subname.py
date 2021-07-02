#################################################################################
#This plugin allows you to put subnames in pwnagotchi, it will be under its face#
#################################################################################

from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import pwnagotchi
import logging

class Subname(plugins.Plugin):
    __author__ = 'demetrius@gmail.com'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'A plugin for add subname in pwnagothci'

    def on_ui_setup(self, ui):
        ui.add_element('subname', LabeledValue(color=BLACK, label='CONDE VAMPIRADÃO', value='', position=(ui.width() / 15, 85),
                                           label_font=fonts.Bold, text_font=fonts.Medium))
