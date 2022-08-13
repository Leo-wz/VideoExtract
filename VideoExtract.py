import os, subprocess, threading
from utils.get_dir import get_dir
from utils.all_video_files import valid_files

input('Press Enter to select a folder: ')
input_path = get_dir()
video_files = valid_files(input_path)

def job(full_path, thread_num):
    os.system(f"echo Thread{thread_num} started")

    subprocess.run(['ffmpeg','-i', full_path[thread_num],
                    '-v', '0', '-c:v', 'copy', '-an',
                    f'{output_path}\{thread_num+1}.mp4'])

    os.system(f"echo Thread{thread_num} finished")

input('Press Enter to select a folder to save the results: ')
output_path = get_dir()

for thread_num in range(len(video_files)):
    threading.Thread(target=job, args=(tuple(video_files),thread_num)).start()

print('Job finished, exit')
