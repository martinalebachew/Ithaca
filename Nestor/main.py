# main.py
# (C) Martin Alebachew, 2023
# Nestor — RavKav Traffic Analysis Reports [ PROJECT ITHACA ]

from datetime import datetime
from Report import Report
from Shared import VERSION
from ParsedPacket import ParsedPacket


def intro():
    print(f"""                                      
         ,--.                                                  
       ,--.'|                        ___                       
   ,--,:  : |                      ,--.'|_                     
,`--.'`|  ' :                      |  | :,'   ,---.    __  ,-. 
|   :  :  | |            .--.--.   :  : ' :  '   ,'\ ,' ,'/ /| 
:   |   \ | :   ,---.   /  /    '.;__,'  /  /   /   |'  | |' | 
|   : '  '; |  /     \ |  :  /`./|  |   |  .   ; ,. :|  |   ,' 
'   ' ;.    ; /    /  ||  :  ;_  :__,'| :  '   | |: :'  :  /   
|   | | \   |.    ' / | \  \    `. '  : |__'   | .; :|  | '    
'   : |  ; .''   ;   /|  `----.   \|  | '.'|   :    |;  : |    
|   | '`--'  '   |  / | /  /`--'  /;  :    ;\   \  / |  , ;    
'   : |      |   :    |'--'.     / |  ,   /  `----'   ---'     
;   |.'       \   \  /   `--'---'   ---`-'                     
'---'          `----'                                          

      RavKav Traffic Analysis Reports | Project Ithaca
               (C) Martin Alebachew, 2023
                       Version {VERSION}
""")


def main():
    intro()
    report = Report(datetime.now().strftime("%B %d, %Y at %H:%M:%S"), "Charging RavKav", "Martin Alebachew")
    report.addRecord(ParsedPacket("in"))
    report.addRecord(ParsedPacket("out"))
    report.save("/Users/martin/Desktop/generated.pdf")


if __name__ == '__main__':
    main()
