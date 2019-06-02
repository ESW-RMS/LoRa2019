Device 1
--------------------
Reads in voltage, etc. from the PCB board and sends readings through LoRa. 

Setup
--------------------
(Follow instructions at blog.scphillips.com/post/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/)

    > chmod 755 read_pcb_write_lora.py
    > sudo cp start_device1.sh /etc/init.d
    > sudo chmod 755 /etc/init.d/start_device1.sh
    > dos2unix read_pcb_write_lora.py
    > sudo update-rc.d start_device1.sh defaults

If properly setup, typing 

    > ls -l /etc/rc?.d/*start_device1.sh 

should display the symbolic link. 

To uninstall the startup script, use 

    > sudo update-rc.d -f start_device1.sh remove

. 
