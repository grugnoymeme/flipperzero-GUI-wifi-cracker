# (flipperzero)-GUI-wifi-cracker
Would you like to be able to extract WPA/WPA2 handshakes from FlipperZero's captured .pcap files, and analyze them with hashcat, and find out passwords JUST IN ONE CLICK?

This is the GUI (Graphic User Interface) version of my other script and repo [`flipperzero-CLI-wifi-cracker`](https://github.com/grugnoymeme/flipperzero-CLI-wifi-cracker), i just wanted to make the process easyest as possible, and this is the result.

```
BEFORE RUNNING THE SCRIPT:

cd dictionary/brutefoce-attack

pip install -r requirements.txt
```      

---
## Extarcion of .pcap file.

You can automatize the extraction of .pcap files from flipper zero, using the [@0xchocolate](https://github.com/0xchocolate) 's companion app, of the [@JustCallMeKoKo's](https://github.com/justcallmekoko) ESP32marauder. Once you've connected the devboard and opened the app,follow these instructions:
```
Menu       
Apps       
WIFI / GPIO / GPIO EXTRA            
[ESP32] WiFi Marauder       
Scripts   
[+]ADD SCRIPT    
< Enter a name for your script >   
Save    
< Select your script >    
[+]EDIT STAGES    
[+]ADD STAGE    
[+]Deauth     
< Select Deauth >     
Timeout 1    
Save    
Back    
[+]ADD STAGE    
[+]Sniff RAW     
< Select Sniff RAW >    
Timeout 15 (or 10, maybe also 5 is ok)     
Save    
Back     
Back     
[*]SAVE
```
  
---
# Disclaimer
This tool is not developed by the Flipper Zero staff.    
Please note that the code you find on this repo is only proposed for educational purposes and should NEVER be used for illegal activities.
