__author__ = 'Administrator'

import time
import os
import re

one_hour_new = time.strftime("%H:%M:%S",time.localtime(int(time.time() / 3600) * 3600))
one_hour_day = time.strftime("%Y%m%d%H",time.localtime(int(time.time() / 3600) * 3600 - 3600))
one_hour_ago = time.strftime("%H:%M:%S",time.localtime(int(time.time() / 3600) * 3600 - 3600))

hostname = os.popen('echo $HOSTNAME').read().strip()
log_path = "/qudian_server/db1_server/cobar/logs/"
log_output_path = ""
log_file_name = log_path + "stdout.log"
log_tmp_cfg  = os.path.split(os.path.realpath(__file__))[0] + "/" + "tmp_cfg.txt"
log_file_output = log_output_path + "stdout" + one_hour_day +".log" + "." + hostname

log_file = open(log_file_name, "rb")
log_filter_output = open(log_file_output, "wb")
log_read = log_file.readlines()

if os.path.exists(log_tmp_cfg):
    tmp_cfg_read = open(log_tmp_cfg, "rb")
    for tmp_cfg_line in tmp_cfg_read.readlines():
        tmp_cfg_line = tmp_cfg_line.split(";",2)
    tmp_cfg_read.close()
else:
    tmp_cfg_line = [1, "00:00:00"]

tmp_cfg_write = open(log_tmp_cfg, "wb")
line_flag = 0
for line in log_read:
    line_patten_f = re.search(r'(\d+?:\d+?:\d+?).\d+?.*', line)
    line_flag += 1
    if line_patten_f:
        if line_patten_f.group() >= str(tmp_cfg_line[1]):
            if line_patten_f.group() >= str(one_hour_new):
                tmp_cfg_write.write(str(line_flag) + ";" + one_hour_new)
                break
            else:
                log_filter_output.write("\n" + line.strip())
                line_flag = 1
    if line_flag == 1:
        if not line_patten_f:
           log_filter_output.write(line.strip())
        else:
           line_flag = 0
           continue


tmp_cfg_write.close()
log_file.close()
log_filter_output.close()

tmp_cfg_write.close()
log_file.close()
log_filter_output.close()