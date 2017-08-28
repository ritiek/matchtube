import pafy


term = 'everybody'
api_key = 'AIzaSyDHTKjtUchUxUOzCtYW4V_h1zzcyd0P6c0'


def generate_query(term, api_key, content='video', results=50, category=10, duration='any', order='relevance'):
    query = {
        'part': 'id,snippet',
        'safeSearch': 'none',
        'maxResults': results,
        'type': content,
        'key': api_key,
        'videoCategoryId': 10,
        'videoDuration': duration,
        'q': term,
        'order': order
        }

    return query


query = generate_query(term, api_key)
gdata = pafy.call_gdata('search', query)
