# main.py
# (C) Martin Alebachew, 2023

from datetime import datetime
from Report import Report
from Shared import VERSION
from Packets import parsePackets


def intro():
    print(f"Traffic Analyser {VERSION}")
    print("RavKav Traffic Analysis Reports")
    print("(C) Martin Alebachew, 2023")


def main():
    intro()
    report = Report(datetime.now().strftime("%B %d, %Y at %H:%M:%S"), "Charging RavKav", "Martin Alebachew")
    report.addRecords(parsePackets("/Users/martin/Desktop/Ithaca Captures/Ithaca_charging.pcap"))
    report.save("/Users/martin/Desktop/generated.pdf")


if __name__ == '__main__':
    main()
