# This script is run by 'startx' to start the graphical session.

# Turn off screen savers and screen blanking.
xset s off s noblank -dpms

# Execute our Python application.
# When the application is closed, the graphical session will end.
python3 /home/examuser/exam_app.py

