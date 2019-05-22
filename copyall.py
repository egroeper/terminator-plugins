#!/usr/bin/python
# Terminator by Chris Jones <cmsj@tenshu.net>
# GPL v2 only
"""copyall.py - Terminator Plugin to copy the terminal content into clipboard"""

import os
import gtk
import terminatorlib.plugin as plugin
from terminatorlib.translation import _

# Every plugin you want Terminator to load *must* be listed in 'AVAILABLE'
AVAILABLE = ['CopyAll']

class CopyAll(plugin.MenuItem):
    """Add custom commands to the terminal menu"""
    capabilities = ['terminal_menu']

    def __init__(self):
        plugin.MenuItem.__init__(self)

    def callback(self, menuitems, menu, terminal):
        """Add our menu items to the menu"""
        item = gtk.MenuItem(_('Copy all to clipboard'))
        item.connect("activate", self.copyall, terminal)
        menuitems.append(item)

    def copyall(self, _widget, terminal):
        """Select all text and copy it to the clipboard"""
	terminal.vte.select_all()
        terminal.vte.copy_clipboard()
        terminal.vte.select_none()

