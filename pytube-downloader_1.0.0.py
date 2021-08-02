# cleaning up the code

# importing some libraries
import urllib.request
import re
from pytube import YouTube

# defining functions

# this one downloads file once url is found

def download_from_url(url_of_video):

    # creates a youtube object defined in pytube

    yt = YouTube(url_of_video)

    # scrape website to get audio streams, also works for videos, will add soon
    print(yt.streams.filter(only_audio=True))
    stream_id = int(input("select stream   "))

    #you must select a stream by its id, each stream has specific features and audio quaity, same for videos
    stream = yt.streams.get_by_itag(stream_id)
    stream.download()
    print("file downloaded")
    return

# this one gets the url of video after query string is given

def get_url(query):

    # add plus sign instead of spaces to be used in url query searching

    for i in range(0, len(query)):
        query = query.replace(" ", "+")
    print(query)

    # open up a web connection to query search

    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
    print(html)

    # find all results links and store in lists (max results is 30)

    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print(video_ids)

    #now print the data extracted from each link one by one

    for i in range(0, 5):  
        
        # modify the range here to get more results but also takes more time
        
        temp_link = "https://www.youtube.com/watch?v=" + video_ids[i]
        temp_yt = YouTube(temp_link)
        temp_list = [i, temp_yt.title, temp_yt.author, temp_yt.length]
        print(temp_list)

    #select a video to grab the required link

    select_link = int(input("which video to select?  "))
    video_link = "https://www.youtube.com/watch?v=" + video_ids[select_link]
    print(video_link)
    return video_link

# main code here

# printing gui
print("welcome to custom pytube downloader\nhow do you want to proceed?\n    1) you have a url to the video\n    2)you want to search youtube from here\n    3) you need to download a playlist\n")
switch1 = int(input("pick an option   "))

# no switch command availible in python hence using if...else 

if switch1 == 1:
    url = input("enter the url of the video     ")
    download_from_url(url)

elif switch1 == 2:
    query = input("enter the search query    ")
    url = get_url(query)
    download_from_url(url)

else:
    print("feature not availible yet, exiting now")


# """to add:
#
# set the path to where to download the file
# add playlist functionality
# get tags of song from spotify to add to song
# select bitrate and quality of audio/video
# include a mailing system
# use selenium to automate everything
# pull data from form csv
# make everything more user friendly

# """
