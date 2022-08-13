import os, subprocess, threading
from utils.get_dir import get_dir
from utils.all_video_files import valid_files
from utils.get_args import get_args
from utils.job import make_job, do_job

input('Press Enter to select a folder: ')
input_path = get_dir()
video_files = valid_files(input_path)
arguments = get_args()

input('Press Enter to select a folder to save the results: ')
output_path = get_dir()

job_list = make_job(video_files, input_path, arguments, output_path)

do_job(job_list)

print('Job finished, exit')
