Device 2
--------------------
Reads in LoRa messages and sends the message through serial. 

Setup
--------------------
(Follow instructions at blog.scphillips.com/post/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)

    > chmod 755 read_lora_write_serial.py
    > sudo cp start_device2.sh /etc/init.d
    > sudo chmod 755 /etc/init.d/start_device2.sh
    > dos2unix read_lora_write_serial.py
    > sudo update-rc.d start_device2.sh defaults

If properly setup, typing 

    > ls -l /etc/rc?.d/*start_device2.sh 

should display the symbolic link. 

To uninstall the startup script, use 

    > sudo update-rc.d -f start_device2.sh remove

. 
