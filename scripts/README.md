
To autostart on boot:
1. Create a configuration file for OLED.service:
- sudo nano /lib/systemd/system/OLED.service

2. Enter the following information into the file:

[Unit]
Description=My Script Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/env python /home/pi/sensor/OLED_service.py <--- Make sure the directory is correct.

[Install]
WantedBy=multi-user.target

3. Save and exit the editor.
Set permissions by:
- sudo chmod 644 /lib/systemd/system/OLED.service

4. Configure the service
- sudo systemctl daemon-reload
- sudo systemctl enable OLED.service

5. Reboot
- sudo reboot

6. Check the statud of the service
- sudo systemctl status OLED_service.py
