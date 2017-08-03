v4l2-ctl -c exposure_auto=1
v4l2-ctl -c exposure_absolute=5
v4l2-ctl -c white_balance_temperature_auto=0
v4l2-ctl -c white_balance_temperature=10000
v4l2-ctl -c contrast=10
v4l2-ctl -c saturation=200

v4l2-ctl -c exposure_auto=1
v4l2-ctl -c exposure_absolute=5
v4l2-ctl -c white_balance_temperature_auto=0
v4l2-ctl -c white_balance_temperature=10000
v4l2-ctl -c contrast=10
v4l2-ctl -c saturation=200

v4l2-ctl -c exposure_auto=1
v4l2-ctl -c exposure_absolute=5
v4l2-ctl -c white_balance_temperature_auto=0
v4l2-ctl -c white_balance_temperature=10000
v4l2-ctl -c contrast=10
v4l2-ctl -c saturation=200

g++ /home/ubuntu/STEAMWORKS_VISION_CODE.cpp -o pandavisionfinal -std=c++11 `pkg-config --cflags --libs opencv`

./pandavisionfinal
