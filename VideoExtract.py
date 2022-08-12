import os, subprocess, threading
from tkinter import filedialog as fd

input('Press Enter to select a folder: ')
input_path = fd.askdirectory()
all_files = os.listdir(input_path)
print('All files are below')
full_path = []

for item in all_files:
    print(f'{item}')
    full_path.append(os.path.join(input_path, item))

input('Press Enter to select a folder to save the results: ')
output_path = fd.askdirectory()

# Prepare output folder
if not os.path.exists(output_path): os.mkdir(output_path)

def job(full_path, thread_num):
    os.system(f"echo Thread{thread_num} started")

    subprocess.run(['ffmpeg','-i', full_path[thread_num],
                    '-v', '0', '-c:v', 'copy', '-an',
                    f'{output_path}\{thread_num+1}.mp4'])

    os.system(f"echo Thread{thread_num} finished")

for i in range(len(full_path)):
    threading.Thread(target=job, args=(tuple(full_path),i)).start()

print('Job finished, exit')
exit()