import pafy

term = 'everybody'
api_key = 'AIzaSyDHTKjtUchUxUOzCtYW4V_h1zzcyd0P6c0'

# CONTENT_TYPE:
# channel, playlist, video

# DURATION:
# any, long, medium, short

# ORDER:
# date, rating, relevance, title, videocount, viewcount

def search_results(term, api_key, content='video', results=50, category=10, duration='any', order='relevance'):
    query = {
        'part': 'id',
        'safeSearch': 'none',
        'maxResults': results,
        'type': content,
        'key': api_key,
        'videoCategoryId': 10,
        'videoDuration': duration,
        'q': term,
        'order': order
    }

    gdata = pafy.call_gdata('search', query)
    return gdata


def video_results(video_ids, api_key):
    query = {
        'id': ','.join(video_ids),
        'part': 'snippet,statistics,contentDetails',
        'key': api_key,
    }

    gdata = pafy.call_gdata('videos', query)
    return gdata


search = search_results(term, api_key)

video_ids = [video['id']['videoId'] for video in search['items']]
gdata = video_results(video_ids, api_key)

# [print('{0}{1}'.format(x, '\n')) for x in gdata['items']]
