# -*- coding: utf-8 -*- 

import os
import sys
import xbmc
import xbmcaddon,xbmcvfs
import urllib,xbmcplugin

__addon__      = xbmcaddon.Addon()
__author__     = __addon__.getAddonInfo('author')
__scriptid__   = __addon__.getAddonInfo('id')
__scriptname__ = __addon__.getAddonInfo('name')
__cwd__        = __addon__.getAddonInfo('path')
__version__    = __addon__.getAddonInfo('version')
__language__   = __addon__.getLocalizedString

__cwd__        = xbmc.translatePath( __addon__.getAddonInfo('path') ).decode("utf-8")
__profile__    = xbmc.translatePath( __addon__.getAddonInfo('profile') ).decode("utf-8")
__resource__   = os.path.join( __cwd__, u'resources', u'lib' )


class MyPlayer( xbmc.Player ):
  def __init__( self, *args, **kwargs ):
    xbmc.Player.__init__( self )
    xbmc.log('MyPlayer - init')
    self.paused = False
        
  def onPlayBackStopped( self ):
    self.paused = False
  
  def onPlayBackEnded( self ):
    self.paused = False    
  
  def onPlayBackStarted( self ):
    self.paused = False

  def onPlayBackPaused( self ):
    self.paused = True

  def onPlayBackResumed( self ):
    self.paused = False    

player_monitor = MyPlayer()

counter = 0
delay = int(__addon__.getSetting("delay"))
while not xbmc.abortRequested:
  if player_monitor.paused == True:
    counter += 1
    if counter > delay*300:
      xbmc.Player().stop()
      counter = 0
  else:
    counter = 0   
  xbmc.sleep(200)



