# TrashSort
This is a project that uses image detection and AI for sorting trash, modeled with an ESP8266 and Raspberry Pi as a web server.
##  Hardware
[Raspberry Pi (Any Wifi enabled)]() 
[NodeMCU ESP8266 ESP-12]() 
[ov7670 camera]() 
## Installation process
Install Apache server: `sudo apt-get install apache2 -y`
Change to default website directory, delete old dir: `sudo cd /var/www && rm -r html` 
Clone this repository: `git clone https://github.com/alexlynd/trashsort` 
Change ownership: `chown -R pi trashsort` 
`cd /etc/apache2/` 
*incomplete*
