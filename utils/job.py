import os, subprocess, threading, time

def _job(file_path, file_name, arguments, output_path):
    os.system(f"echo {file_name} started")

    subprocess.run(['ffmpeg','-i', os.path.join(file_path, file_name),
                    '-v', '0', *arguments,
                    f'{output_path}\{file_name}.mp4'])

    os.system(f"echo {file_name} finished")

def make_job(files_list, file_path, arguments, output_path):
    job_list = []
    for file_name in files_list:
        job_list.append(threading.Thread(target=_job, args=(file_path, file_name, arguments, output_path)))
    return job_list

def do_job(job_list):
    for job in job_list:
        while threading.active_count() > 4: pass
        else:
            job.start()
    pass