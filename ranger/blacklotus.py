# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.
# Author: Joseph Tannhuber <sepp.tannhuber@yahoo.de>, 2013
# Solarized like colorscheme, similar to solarized-dircolors
# from https://github.com/seebi/dircolors-solarized.
# This is a modification of Roman Zimbelmann's default colorscheme.

from __future__ import (absolute_import, division, print_function)

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import (
    black, blue, cyan, green, magenta, red, white, yellow, default,
    normal, bold, reverse, dim, BRIGHT,
    default_colors,
)


class Blacklotus(ColorScheme):
    progress_bar_color = magenta

    def use(self, context):  # pylint: disable=too-many-branches,too-many-statements
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            fg = yellow
            if context.selected:
                attr = reverse
            else:
                attr = normal
            if context.empty or context.error:
                fg = default
                bg = red
            if context.border:
                fg = magenta
                fg += BRIGHT
            if context.media:
                if context.image:
                    fg = magenta
                    fg += BRIGHT
                else:
                    fg = magenta
            if context.container:
                fg = red
                fg += BRIGHT
            if context.directory:
                fg = default
                if context.selected:
                    fg = blue
                    bg = black
            elif context.executable and not \
                    any((context.media, context.container,
                         context.fifo, context.socket)):
                fg = green
                attr |= bold
            if context.socket:
                fg = yellow
                bg = white
                attr |= bold
            if context.fifo:
                fg = green
                bg = white
                attr |= bold
            if context.device:
                fg = black
                fg += BRIGHT
                bg = white
                attr |= bold
            if context.link:
                fg = cyan if context.good else red
                fg += BRIGHT
                attr |= bold
                if context.bad:
                    bg = black
            if context.tag_marker and not context.selected:
                attr |= bold
                if fg in (red, magenta):
                    fg = white
                else:
                    fg = red
            if not context.selected and (context.cut or context.copied):
                fg = black
                attr |= bold
            if context.main_column:
                if context.selected:
                    attr |= bold
                if context.marked:
                    attr |= bold
                    bg = black
                    bg += BRIGHT
            if context.badinfo:
                if attr & reverse:
                    bg = magenta
                else:
                    fg = magenta

            if context.inactive_pane:
                fg = black
                fg += BRIGHT

        elif context.in_titlebar:
            attr |= bold
            if context.hostname:
                fg = black if context.bad else blue
                if context.bad:
                    bg = red
                    bg += BRIGHT
            elif context.directory:
                fg = magenta
                fg += BRIGHT
            elif context.tab:
                fg = green if context.good else green
                fg += BRIGHT
                bg = black
                bg += BRIGHT
            elif context.link:
                fg = cyan

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = magenta
                    fg += BRIGHT
                elif context.bad:
                    fg = red
                    fg += BRIGHT
                    bg = black
            if context.marked:
                attr |= bold | reverse
                fg = black
                fg += BRIGHT
                bg = green
                bg += BRIGHT
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = red
                    fg += BRIGHT
                    bg = black
            if context.loaded:
                bg = self.progress_bar_color

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = magenta
                fg += BRIGHT

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    bg = self.progress_bar_color

        return fg, bg, attr
