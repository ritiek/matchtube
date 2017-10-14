import pafy

term = 'everybody'
api_key = 'AIzaSyDHTKjtUchUxUOzCtYW4V_h1zzcyd0P6c0'


def query_results(term, api_key, content='video', results=50, category=10, duration='any', order='relevance'):
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


def video_results(video_ids, api_key, content='video', results=50, category=10, duration='any', order='relevance'):
    query = {
        'id': video_ids,
        'part': 'snippet,statistics,contentDetails',
        'key': api_key,
    }

    gdata = pafy.call_gdata('videos', query)
    return gdata


search = query_results(term, api_key)
print(search)
exit()

video_ids = str()
for video in search['items']:
    video_ids += video['id']['videoId'] + ','

print(video_ids)

gdata = video_results(video_ids, api_key)
[print('{0}{1}'.format(x, '\n')) for x in gdata['items']]
