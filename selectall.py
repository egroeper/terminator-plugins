#!/usr/bin/python
# Terminator by Chris Jones <cmsj@tenshu.net>
# GPL v2 only
"""selectall.py - Terminator Plugin to do select_all in a terminal"""

import os
from gi.repository import Gtk
import terminatorlib.plugin as plugin
from terminatorlib.translation import _

# Every plugin you want Terminator to load *must* be listed in 'AVAILABLE'
AVAILABLE = ['SelectAll']

class SelectAll(plugin.MenuItem):
    """Add custom commands to the terminal menu"""
    capabilities = ['terminal_menu']

    def __init__(self):
        plugin.MenuItem.__init__(self)

    def callback(self, menuitems, menu, terminal):
        """Add our menu items to the menu"""
        item = Gtk.MenuItem(_('Select all'))
        item.connect("activate", self.selectall, terminal)
        menuitems.append(item)

    def selectall(self, _widget, terminal):
        """Select all text """
	terminal.vte.select_all()

