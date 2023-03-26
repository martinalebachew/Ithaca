# main.py
# (C) Martin Alebachew, 2023
# Nestor — RavKav Traffic Analysis Reports [ PROJECT ITHACA ]

from datetime import datetime
from Report import Report
from NestorConsts import VERSION


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
    # report.addRecord(">", "boom!")
    # report.addRecord("<", "boom!")
    report.save("/Users/martin/Desktop/generated.pdf")


if __name__ == '__main__':
    main()
