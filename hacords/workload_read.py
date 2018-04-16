import sys
import os
import time
import subprocess
import logging

logging.basicConfig()

hostlist = ['172.18.0.2','172.18.0.3','172.18.0.4','172.18.0.5']
HD_HOME='/hadoop-3.0.0'
CUR_DIR=os.path.dirname(os.path.realpath(_file_))
ha_logfile_name='hadoop.out'

