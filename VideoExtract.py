import os, subprocess, threading
from utils.get_dir import get_dir
from utils.all_video_files import valid_files
from utils.get_args import get_args

input('Press Enter to select a folder: ')
input_path = get_dir()
video_files = valid_files(input_path)
if len(video_files) == 0:
    print('No valid video file found, exiting...')
    quit()

arguments = get_args()

def job(full_path, thread_num, arguments):
    os.system(f"echo Thread{thread_num} started")

    subprocess.run(['ffmpeg','-i', full_path[thread_num],
                    '-v', '0', *arguments,
                    f'{output_path}\{thread_num+1}.mp4'])

    os.system(f"echo Thread{thread_num} finished")

input('Press Enter to select a folder to save the results: ')
output_path = get_dir()

for thread_num in range(len(video_files)):
    threading.Thread(target=job, args=(tuple(video_files),thread_num, arguments)).start()

print('Job finished, exit')
