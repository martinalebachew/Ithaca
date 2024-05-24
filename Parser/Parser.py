# Parser.py
# (C) Martin Alebachew, 2023

import argparse
from typing import List
from Report import Report
from NativeMessaging import out
from Datagrams import parse_datagrams, Command, Response
from Bridge import encode_datagrams, encode_parsing_error


def safe_parse(filename: str) -> List[Command | Response]:
    try:
        return parse_datagrams(filename)
    except:
        out(encode_parsing_error())
        exit()


def save_pdf(filename: str, pdf_output: str) -> None:    
    report = Report(filename)
    datagrams = safe_parse(filename)
    
    # TODO: Allow no-ATR / not first
    report.add_atr_scan(datagrams[0])
    report.add_records(datagrams[1:])
    report.save(pdf_output)


def parse_to_stdout(filename: str) -> None:
    datagrams = safe_parse(filename)
    encoded = encode_datagrams(datagrams)
    out(encoded)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", help="Path of .pcap file to parse.", required=True)
    parser.add_argument("--pdf", help="Path of PDF output file.", required=False)
    args = parser.parse_args()
    
    if args.pdf:
        save_pdf(args.filename, args.pdf)
    else:
        parse_to_stdout(args.filename)


if __name__ == '__main__':
    main()
