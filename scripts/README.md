
To autostart on boot:
1. Create a configuration file for OLED.service --- e.g. sudo nano /lib/systemd/system/OLED.service
2. Enter the following information:

[Unit]
Description=My Script Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/env python /home/pi/sensor/OLED_service.py <--- Make sure the directory is correct.

[Install]
WantedBy=multi-user.target

3. Save and exit the editor.
4. Set permissions by: sudo chmod 644 /lib/systemd/system/OLED.service

Configure the service
1. sudo systemctl daemon-reload
2. sudo systemctl enable OLED.service

Reboot
- sudo reboot

Check the statud of the service
- sudo systemctl status OLED_service.py
