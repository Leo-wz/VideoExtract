import os

'''
Scan the directory and return all video files
'''

valid_extensions = ['.mp4', '.m2ts', '.mkv', '.avi', '.mov']

def valid_files(path):
    all_items = os.listdir(path)
    videos = []
    for item in all_items:          # Sometimes extensions are in upper case
        if os.path.splitext(item)[1].lower() in valid_extensions:
            videos.append(os.path.join(path, item))
    return videos
