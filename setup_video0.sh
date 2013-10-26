#!/bin/bash

uv4l --driver raspicam --auto-video_nr --width 1280 --height 720
cd ~/temp/mjpg-streamer-code/mjpg-streamer/```
export LD_LIBRARY_PATH="$(pwd)"
LD_PRELOAD=/usr/lib/uv4l/uv4lext/armv6l/libuv4lext.so ./mjpg_streamer -i "input_uvc.so -d /dev/video0 -r 1280x720 -f 2" -o "output_http.so -w ./www"
