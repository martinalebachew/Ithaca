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
    recordedPackets = parsePackets("/Users/martin/Desktop/Ithaca Captures/Ithaca_charging.pcap")
    report.addATRScan(recordedPackets[0])
    report.addRecords(recordedPackets[1:])
    report.save("/Users/martin/Desktop/generated.pdf")


if __name__ == '__main__':
    main()
