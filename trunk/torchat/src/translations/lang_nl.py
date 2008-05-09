# -*- coding: UTF-8 -*-

##############################################################################
#                                                                            #
# Copyright (c) 2007-2008 Bernd Kreuss <prof7bit@gmail.com>                  #
#                                                                            #
# Translation file for TorChat                                               #
#                                                                            #
# Language: English [en]                                                     #
#                                                                            #
##############################################################################

LANGUAGE_CODE = u"nl"
LANGUAGE_NAME = u"Nederlands"
TRANSLATOR_NAMES = [u"2by3"]

#buttons
BTN_CANCEL = u"Annuleren"
BTN_OK = u"Ok"
BTN_SAVE_AS = u"Opslaan als..."
BTN_CLOSE = u"Sluiten"

#status
ST_AVAILABLE = u"Aanwezig"
ST_AWAY = u"Afwezig"
ST_EXTENDED_AWAY = u"Langdurig afwezig"
ST_OFFLINE = u"Offline"

#TaskbarMenu
MTB_SHOW_HIDE_TORCHAT = u"Toon/Verberg TorChat"
MTB_QUIT = u"Sluiten"

#popup menu
MPOP_CHAT = u"Chat..."
MPOP_SEND_FILE = u"Verzend bestand..."
MPOP_EDIT_CONTACT = u"Bewerk contactpersoon..."
MPOP_DELETE_CONTACT = u"Verwijder contact..."
MPOP_SHOW_OFFLINE_MESSAGES = u"Toon Offline berichten in wacht"
MPOP_CLEAR_OFFLINE_MESSAGES = u"Schoon Offline berichten in wacht"
MPOP_ADD_CONTACT = u"Contactpersoon toevoegen"
MPOP_ABOUT = u"Over TorChat"
MPOP_ASK_AUTHOR = u"Vraag %s"

#confirm delete message box
D_CONFIRM_DELETE_TITLE = u"Bevestig verwijderen"
D_CONFIRM_DELETE_MESSAGE = u"Weet u zeker dat u deze contactpersoon wilt verwijderen?\n(%s %s)"

#warning about log
D_LOG_WARNING_TITLE = u"TorChat: Logboek ingeschakeld"
D_LOG_WARNING_MESSAGE = u"Logging naar bestand is geactiveerd!\n\nLog bestand: %s\n\nVergeet niet het logbestand te verwijderen na het debuggen, deze kan gevoellige informatie bevatten"

#warnig about unread messages
D_WARN_UNREAD_TITLE = u"TorChat: Ongelezen berichten"
D_WARN_UNREAD_MESSAGE = u"Er zijn ongelezen berichten.\nDeze zullen verloren gaan!\n\nWeet u zeker dat u TorChat wilt sluiten?"

#dialog: add/edit contact
DEC_TITLE_ADD = u"Contactpersoon toevoegen"
DEC_TITLE_EDIT = u"Bewerk contactpersoon"
DEC_TORCHAT_ID = u"TorChat ID"
DEC_DISPLAY_NAME = u"Weergave naam"
DEC_INTRODUCTION = u"Introductie"
DEC_MSG_16_CHARACTERS = u"Het adres dient 16 karakters lang te zijn, niet %i."
DEC_MSG_ONLY_ALPANUM = u"Het adres kan alleen cijfers en kleine letters bevatten."
DEC_MSG_ALREADY_ON_LIST = u"%s staat al in uw lijst."

#file transfer window
DFT_SEND = u"Verzenden %s\nnaar %s\n%04.1f%% (%i van %i bytes)"
DFT_RECEIVE = u"Ontvangen %s\nvan %s\n%04.1f%% (%i van %i bytes)"

#notices in the chat window (those in square brackets)
NOTICE_DELAYED_MSG_WAITING = u"vertraagde berichten, wachtend om verzonden te worden"
NOTICE_DELAYED_MSG_SENT = u"vertraagde berichten zijn verzonden"
NOTICE_DELAYED = u"vertraagd"

#about box
ABOUT_TITLE = u"Over TorChat"
ABOUT_TEXT = u"""TorChat %(version)s
  %(copyright)s

Translations: 
  %(translators)s

Runtime environment:
  Python: %(python)s
  wx: %(wx)s
    
TorChat is free software: you can redistribute it and/or \
modify it under the terms of the GNU General Public \
License as published by the Free Software Foundation, \
either version 3 of the License, or (at your option) \
any later version.

TorChat is distributed in the hope that it will be useful, \
but WITHOUT ANY WARRANTY; without even the implied \
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. \
See the GNU General Public License for more details.

*

And now for something completely different:

If you happen to run a software company near Hannover, Germany and \
are in need of a new coder, feel free to regard this little program \
as my application documents and drop me a mail with your answer.
"""
