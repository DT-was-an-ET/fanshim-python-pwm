#!/bin/bash
cd /home/pi/fanshim
echo looking to kill any existing fanshim session
tmux kill-session -t fanshim
tmux kill-session -t mnt
echo now new tmux fanshim session
tmux new-session -d -s fanshim 'python3 examples/automatic.py --off-threshold 54 --on-threshold 56 --verbose'
tmux new-session -d -s mnt 'python3 mount_drives.py'



#!/bin/bash
#cd /home/pi/code
#tmux kill-session -t wd
#tmux kill-session -t ctrl
#tmux kill-session -t test
#tmux kill-session -t mnt
#tmux kill-session -t cpu
#tmux new-session -d -s wd 'python3 watch_dog.py'
#tmux new-session -d -s ctrl 'python3 temp_control.py'
#tmux new-session -d -s cpu 'python3 cpu_monitor.py'
#tmux new-session -d -s mnt 'python3 mount_drives.py'
#tmux new-session -d -s test 'python3 test_text_buffer.py'
