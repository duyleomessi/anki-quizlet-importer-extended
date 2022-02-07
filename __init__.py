#-------------------------------------------------------------------------------
#
# Name:        Quizlet plugin for Anki 2.0
# Purpose:     Import decks from Quizlet into Anki 2.0
# Author:
#  - Original: (c) Rolph Recto 2012, last updated 12/06/2012
#              https://github.com/rolph-recto/Anki-Quizlet
#  - Also:     Contributions from https://ankiweb.net/shared/info/1236400902
#  - Current:  JDMaybeMD
# Created:     04/07/2017
#
# Changlog:    Inital release
#               - Rolph's plugin functionality was broken, so...
#               - removed search tables and associated functions to KISS
#               - reused the original API key, dunno if that's OK
#               - replaced with just one box, for a quizlet URL
#               - added basic error handling for dummies
#
#               Update 04/09/2017
#               - modified to now take a full Quizlet url for ease of use
#               - provide feedback if trying to download a private deck
#               - return RFC 2616 response codes when error handling
#               - don't make a new card type every time a new deck imported
#               - better code documentation so people can modify it
#
#               Update 01/31/2018
#               - get original quality images instead of mobile version
#
#               Update 09/12/2018
#               - updated to Anki 2.1 (by kelciour)
#
#               Update 04/02/2020
#               - download a set without API key since it's no longer working (by kelciour)
#
#               Update 19/02/2020
#               - download private or password-protected sets using cookies (by kelciour)
#
#               Update 25/02/2020
#               - make it work again by adding the User-Agent header (by kelciour)
#
#               Update 14/04/2020
#               - try to get title from HTML a bit differently (by kelciour)
#
#               Update 29/04/2020
#               - suggest to disable VPN if a set is blocked by a captcha (by kelciour)
#-------------------------------------------------------------------------------
#!/usr/bin/env python

__window = None

import sys, math, time, urllib.parse, json, re
from operator import itemgetter

# Anki
from aqt import mw
from aqt.qt import *
from aqt.utils import showText

import requests
import shutil

from . import quizletimporter

# plugin was called from Anki
def runQuizletPlugin():
    global __window
    __window = quizletimporter.QuizletWindow()

# create menu item in Anki
action = QAction("Import from Quizlet", mw)
action.triggered.connect(runQuizletPlugin)
mw.form.menuTools.addAction(action)
