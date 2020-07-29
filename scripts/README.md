
To autostart on boot:

1. Create a configuration file for OLED.service:
- sudo nano /lib/systemd/system/OLED.service

2. Enter the following information into the file:

[Unit]
- Description=OLED Status Monitor
- After=multi-user.target

[Service]
- Type=idle
- ExecStart=/usr/bin/env python /home/pi/sensor/OLED_service.py <--- Make sure the directory is correct.

[Install]
- WantedBy=multi-user.target

3. Save and exit the editor.

4. Set permissions by:
- sudo chmod 644 /lib/systemd/system/OLED.service

5. Configure the service
- sudo systemctl daemon-reload
- sudo systemctl enable OLED.service

6. Reboot
- sudo reboot

7. Check the status of the running service
- sudo systemctl status OLED_service.py

8. Imporant note:  OLED_service.py file should match the RST pin, which is 24 for older version scanner boards and 4 revised boards.  
