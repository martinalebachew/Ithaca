# main.py
# (C) Martin Alebachew, 2023

from datetime import datetime
from Report import Report
from Shared import VERSION
from Packets import parsePackets
from os.path import expanduser


def intro():
    print(f"Traffic Analyser {VERSION}")
    print("RavKav Traffic Analysis Reports")
    print("(C) Martin Alebachew, 2023\n")


def main():
    intro()

    print("Generating report...")
    timestamp = datetime.now().strftime("%B %d, %Y at %H:%M:%S")
    title = "Charging RavKav"
    author = "Martin Alebachew"

    pcap_filename = "/Users/martin/Documents/Other/Ithaca Captures/Ithaca_charging.pcap"
    pdf_filename = expanduser("~/Desktop/generated.pdf")

    report = Report(timestamp, title, author)
    recordedPackets = parsePackets(pcap_filename)
    report.addATRScan(recordedPackets[0])
    report.addRecords(recordedPackets[1:])
    report.save(pdf_filename)

    print(f"Saved to {pdf_filename}")


if __name__ == '__main__':
    main()
