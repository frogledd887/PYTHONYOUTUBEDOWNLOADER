#!/usr/local/bin/python

from pytube import Playlist

input = input('address：')
pl = Playlist(input)
#pl.populate_video_urls()
#print "List size is %s:" % len(pl.video_urls)
print("start")
pl.download_all()
print("finish")