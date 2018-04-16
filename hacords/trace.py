#!/usr/bin/env python
import os
import time
import subprocecss
import math
import paramiko

hostlist = ['172.18.0.2','172.18.0.3','172.18.0.4','172.18.0.5']
ERRFS_HOME=os.path.dirname(os.path.realpath(_file_))
fuse_command_trace = ERRFS_HOME + "/errfs -f -omodules=subdir,subdir=%s %s trace %s &"

#trace file is set trace0.txt an so on in the directory 
parser = argparse.ArgumentParser()
trace_files=['trace0']
parser.add_argument('--data_dirs', nargs='+', required = True, help = 'Location of data directories')
parser.add_argument('--workload_command', required = True, type = str)

args = parser.parse_args()


for i in range(0, len(args.data_dirs)):
	args.data_dirs[i] = os.path.abspath(args.data_dirs[i])

trace_files = args.trace_files
data_dirs = args.data_dirs

assert len(trace_files) == len(data_dirs)
machine_count = len(trace_files)

workload_command = args.workload_command

for data_dir in data_dirs:
	assert os.path.exists(data_dir)

uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])

data_dir_snapshots = []
data_dir_mount_points = []

for i in range(0,4)
    data_dir_snapshots.append(os.path.join(uppath(data_dirs[i], 1), os.path.basename(os.path.normpath(data_dirs[i]))+ ".snapshot"))
	data_dir_mount_points.append(os.path.join(uppath(data_dirs[i], 1), os.path.basename(os.path.normpath(data_dirs[i]))+ ".mp"))
	subprocess.check_output("rm -rf " + data_dir_snapshots[i], shell = True)
	subprocess.check_output("rm -rf " + data_dir_mount_points[i], shell = True)
	subprocess.check_output("mkdir " + data_dir_mount_points[i], shell = True)