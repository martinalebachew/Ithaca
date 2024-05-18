# Parser.py
# (C) Martin Alebachew, 2023

import argparse
from datetime import datetime
from Report import Report
from Packets import parsePackets
from Bridge import encodePackets, encodeParsingError
from NativeMessaging import out


def save_pdf(filename: str, title: str, author: str, packets):
    timestamp = datetime.now().strftime("%B %d, %Y at %H:%M:%S")
    
    report = Report(timestamp, title, author)
    
    # TODO: Allow no-ATR / not first
    report.addATRScan(packets[0])
    report.addRecords(packets[1:])
    report.save(filename)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Path of .pcap file to parse.")
    args = parser.parse_args()
    
    try:
        packets = parsePackets(args.filename)
    except:
        out(encodeParsingError())
    
    encoded = encodePackets(packets)
    out(encoded)
    

if __name__ == '__main__':
    main()
