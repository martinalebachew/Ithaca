# Shared.py
# (C) Martin Alebachew, 2023

VERSION = "1.0.0"
TABLE_WIDTH = 190

HEADERS = {
    "CardToHost": {
        "titles": ["NO", "DIR", "Data", "SW1", "SW2"],
        "widths": [(size * 100 / TABLE_WIDTH) for size in (15, 12, 143, 10, 10)]
    },

    "HostToCard": {
        "titles": ["NO", "DIR", "CLA", "INS", "P1", "P2", "Lc", "Data", "Le"],
        "widths": [(size * 100 / TABLE_WIDTH) for size in (15, 12, 10, 10, 10, 10, 10, 103, 10)]
    }
}

RESPONSE_COLOR = {
    "Unknown": "BLACK",
    "Success": "GREEN",
    "Info": "BLACK",
    "Warning": "YELLOW",
    "Error": "RED",
}

COLOR_SCHEME = {
    "BLACK": (0, 0, 0),
    "GREEN": (93, 187, 99),
    "RED": (220, 40, 40),
    "YELLOW": (255, 191, 0)
}

# https://github.com/elafargue/smart-tools/blob/master/atr/lib/calypso-xplore.html
CHIP_TYPE = {
    "01": "ST16V623",
    "02": "ST16601",
    "03": "ST16RF42",
    "04": "M35101",
    "05": "Type 05",
    "06": "ST16SF4F",
    "07": "ST16RF58",
    "08": "ST16RF820",
    "09": "ST16VF52",
    "0A": "ST16RF52",
    "14": "ST16SF48",
    "21": "ST19XR08",
    "22": "ST19XR34",
    "23": "ST19NM34",
    "28": "ST19WR02",
    "29": "ST19WR08",
    "30": "AT05SC4002RF",
    "31": "SLE66CLX320P",
    "41": "Philips ProX",
    "C0": "JavaCard"
}

# https://github.com/elafargue/smart-tools/blob/master/atr/lib/calypso-xplore.html
APPLICATION = {
    "01": "CD97, Calypso revision 1",
    "02": "Modeus v1.1, Calypso revision 1",
    "03": "GTML, Calypso revision 1",
    "04": "CT2000, Calypso revision 1",
    "06": "Calypso application, Calypso revision 2",
    "07": "Extended Calypso application, Calypso revision 2",
    "11": "Calypso card without token purse application, Calypso revision 2",
    "13": "Calypso card with token purse application, Calypso revision 2",
    "80": "Calypso SAM"
}

# https://github.com/elafargue/smart-tools/blob/master/atr/lib/calypso-xplore.html
SOFTWARE_ISSUER = {
    "00": "ASK",
    "01": "Intec",
    "02": "Calypso",
    "03": "Ascom",
    "04": "Thalès",
    "06": "Axalto",
    "07": "Bull",
    "08": "Spirtech",
    "09": "BMS",
    "0A": "Oberthur",
    "0B": "Gemplus",
    "0C": "Magnadata",
    "0D": "Calmell",
    "0E": "Mecstar",
    "0F": "ACG Identification",
    "10": "STMicroelectronics",
    "11": "Calypso",
    "12": "Giesecke & Devrient",
    "13": "OTI",
    "20": "Calypso",
    "2E": "Calypso"
}

# https://www.digitalwhisper.co.il/files/Zines/0x7C/DW124-2-RavKavRE.pdf
INSTRUCTIONS = {
    "04": "DEACTIVATE FILE",
    "0e": "ERASE BINARY",
    "10": "FABRICATION READ",
    "20": "VERIFY PIN",
    "30": "DECREASE",
    "32": "INCREASE",
    "38": "DECREASE MULTIPLE",
    "3a": "INCREASE MULTIPLE",
    "44": "ACTIVATE FILE / REHABILITATE",
    "52": "CHANGE SPEED",
    "7c": "SV GET",
    "82": "EXTERNAL AUTHENTICATE / MANAGE SECURE SESSION",
    "84": "GET CHALLENGE",
    "86": "GENERAL AUTHENTICATE / GIVE RANDOM",
    "8a": "OPEN SECURE SESSION",
    "8c": "ABORT SECURE SESSION",
    "8e": "CLOSE SECURE SESSION",
    "a2": "SEARCH RECORD",
    "a4": "SELECT FILE / SELECT APPLICATION",
    "b0": "READ BINARY",
    "b2": "SEARCH RECORD(S)",
    "b3": "READ RECORDS MULTIPLE",
    "b6": "READ RECORD STAMPED",
    "b8": "SV RELOAD",
    "ba": "SV DEBIT",
    "bc": "SV UNDEBIT",
    "be": "GET ATR",
    "c0": "GET RESPONSE",
    "ca": "RETRIEVE DATA",
    "d0": "WRITE BINARY",
    "d2": "WRITE RECORD",
    "d6": "UPDATE BINARY",
    "d8": "CHANGE KEY / CHANGE PIN",
    "da": "SET DATA",
    "dc": "UPDATE RECORD",
    "e0": "CREATE FILE",
    "e1": "GET AVAILABLE MEMORY",
    "e2": "APPEND RECORD",
    "f2": "STATUS",
}

# https://www.eftlab.com/knowledge-base/complete-list-of-apdu-responses
RESPONSES = {
    "06——": "[Error] Class not supported",
    "61——": "[Info] Response bytes still available",
    "61XX": "[Success] [SW2] bytes of data are available and can be requested using GET RESPONSE",
    "62——": "[Warning] State of non-volatile memory unchanged",
    "6200": "[Warning] No information given (NV-Ram not changed)",
    "6201": "[Warning] NV-Ram not changed 1",
    "6281": "[Warning] Part of returned data may be corrupted",
    "6282": "[Warning] End of file/record reached before reading Le bytes",
    "6283": "[Warning] Selected file invalidated",
    "6284": "[Warning] Selected file is not valid. FCI not formatted according to ISO",
    "6285": "[Warning] No input data available from a sensor on the card. No Purse Engine enslaved for R3bc",
    "62A2": "[Warning] Wrong R-MAC",
    "62A4": "[Warning] Card locked (during reset( ))",
    "62CX": "[Warning] Counter with value x (command dependent)",
    "62F1": "[Warning] Wrong C-MAC",
    "62F3": "[Warning] Internal reset",
    "62F5": "[Warning] Default agent locked",
    "62F7": "[Warning] Cardholder locked",
    "62F8": "[Warning] Basement is current agent",
    "62F9": "[Warning] CALC Key Set not unblocked",
    "62FX": "[Warning] Unknown",
    "62XX": "[Warning] RFU",
    "63——": "[Warning] State of non-volatile memory changed",
    "6300": "[Warning] No information given (NV-Ram changed)",
    "6381": "[Warning] File filled up by the last write. Loading/updating is not allowed",
    "6382": "[Warning] Card key not supported",
    "6383": "[Warning] Reader key not supported",
    "6384": "[Warning] Plaintext transmission not supported",
    "6385": "[Warning] Secured transmission not supported",
    "6386": "[Warning] Volatile memory is not available",
    "6387": "[Warning] Non-volatile memory is not available",
    "6388": "[Warning] Key number not valid",
    "6389": "[Warning] Key length is not correct",
    "63C0": "[Warning] Verify fail, no try left",
    "63C1": "[Warning] Verify fail, 1 try left",
    "63C2": "[Warning] Verify fail, 2 tries left",
    "63C3": "[Warning] Verify fail, 3 tries left",
    "63CX": "[Warning] The counter has reached the value 'x' (0 = x = 15) (command dependent)",
    "63F1": "[Warning] More data expected",
    "63F2": "[Warning] More data expected and proactive command pending",
    "63FX": "[Warning] Unknown",
    "63XX": "[Warning] RFU",
    "64——": "[Error] State of non-volatile memory unchanged",
    "6400": "[Error] No information given (NV-Ram not changed)",
    "6401": "[Error] Command timeout. Immediate response required by the card",
    "64XX": "[Error] RFU",
    "65——": "[Error] State of non-volatile memory changed",
    "6500": "[Error] No information given",
    "6501": "[Error] Write error. Memory failure. There have been problems in writing or reading the EEPROM. Other hardware problems may also cause this error",
    "6581": "[Error] Memory failure",
    "65FX": "[Error] Unknown",
    "65XX": "[Error] RFU",
    "66——": "[Success] Unknown",
    "6600": "[Success] Error while receiving (timeout)",
    "6601": "[Success] Error while receiving (character parity error)",
    "6602": "[Success] Wrong checksum",
    "6603": "[Success] The current DF file without FCI",
    "6604": "[Success] No SF or KF under the current DF",
    "6669": "[Success] Incorrect Encryption/Decryption Padding",
    "66XX": "[Success] Unknown",
    "67——": "[Error] Unknown",
    "6700": "[Error] Wrong length",
    "67XX": "[Error] length incorrect (procedure)(ISO 7816-3)",
    "68——": "[Error] Functions in CLA not supported",
    "6800": "[Error] No information given (The request function is not supported by the card)",
    "6881": "[Error] Logical channel not supported",
    "6882": "[Error] Secure messaging not supported",
    "6883": "[Error] Last command of the chain expected",
    "6884": "[Error] Command chaining not supported",
    "68FX": "[Error] Unknown",
    "68XX": "[Error] RFU",
    "69——": "[Error] Command not allowed",
    "6900": "[Error] No information given (Command not allowed)",
    "6901": "[Error] Command not accepted (inactive state)",
    "6981": "[Error] Command incompatible with file structure",
    "6982": "[Error] Security condition not satisfied",
    "6983": "[Error] Authentication method blocked",
    "6984": "[Error] Referenced data reversibly blocked (invalidated)",
    "6985": "[Error] Conditions of use not satisfied",
    "6986": "[Error] Command not allowed (no current EF)",
    "6987": "[Error] Expected secure messaging (SM) object missing",
    "6988": "[Error] Incorrect secure messaging (SM) data object",
    "698D": "[Unknown] Reserved",
    "6996": "[Error] Data must be updated again",
    "69E1": "[Error] POL1 of the currently Enabled Profile prevents this action",
    "69F0": "[Error] Permission Denied",
    "69F1": "[Error] Permission Denied – Missing Privilege",
    "69FX": "[Error] Unknown",
    "69XX": "[Error] RFU",
    "6A——": "[Error] Wrong parameter(s) P1-P2",
    "6A00": "[Error] No information given (Bytes P1 and/or P2 are incorrect)",
    "6A80": "[Error] The parameters in the data field are incorrect",
    "6A81": "[Error] Function not supported",
    "6A82": "[Error] File not found",
    "6A83": "[Error] Record not found",
    "6A84": "[Error] There is insufficient memory space in record or file",
    "6A85": "[Error] Lc inconsistent with TLV structure",
    "6A86": "[Error] Incorrect P1 or P2 parameter",
    "6A87": "[Error] Lc inconsistent with P1-P2",
    "6A88": "[Error] Referenced data not found",
    "6A89": "[Error] File already exists",
    "6A8A": "[Error] DF name already exists",
    "6AF0": "[Error] Wrong parameter value",
    "6AFX": "[Error] Unknown",
    "6AXX": "[Error] RFU",
    "6B——": "[Error] Unknown",
    "6B00": "[Error] Wrong parameter(s) P1-P2",
    "6BXX": "[Error] Reference incorrect (procedure byte), (ISO 7816-3)",
    "6C——": "[Error] Wrong length Le",
    "6C00": "[Error] Incorrect P3 length",
    "6CXX": "[Error] Bad length value in Le; [SW2] is the correct exact Le",
    "6D——": "[Error] Unknown",
    "6D00": "[Error] Instruction code not supported or invalid",
    "6DXX": "[Error] Instruction code not programmed or invalid (procedure byte), (ISO 7816-3)",
    "6E——": "[Error] Unknown",
    "6E00": "[Error] Class not supported",
    "6EXX": "[Error] Instruction class not supported (procedure byte), (ISO 7816-3)",
    "6F——": "[Error] Internal exception",
    "6F00": "[Error] Command aborted – more exact diagnosis not possible (e.g., operating system error)",
    "6FFF": "[Error] Card dead (overuse, …)",
    "6FXX": "[Error] No precise diagnosis (procedure byte), (ISO 7816-3)",
    "9000": "[Success] OK",
    "9004": "[Warning] PIN not successfully verified, 3 or more PIN tries left",
    "9008": "[Error] Key/file not found",
    "9080": "[Warning] Unblock Try Counter has reached zero",
    "9100": "[Success] OK",
    "9101": "[Error] States.activity, States.lock Status or States.lockable has wrong value",
    "9102": "[Error] Transaction number reached its limit",
    "910C": "[Error] No changes",
    "910E": "[Error] Insufficient NV-Memory to complete command",
    "911C": "[Error] Command code not supported",
    "911E": "[Error] CRC or MAC does not match data",
    "9140": "[Error] Invalid key number specified",
    "917E": "[Error] Length of command string invalid",
    "919D": "[Error] Not allow the requested command",
    "919E": "[Error] Value of the parameter invalid",
    "91A0": "[Error] Requested AID not present on PICC",
    "91A1": "[Error] Unrecoverable error within application",
    "91AE": "[Error] Authentication status does not allow the requested command",
    "91AF": "[Error] Additional data frame is expected to be sent",
    "91BE": "[Error] Out of boundary",
    "91C1": "[Error] Unrecoverable error within PICC",
    "91CA": "[Error] Previous command was not fully completed",
    "91CD": "[Error] PICC was disabled by an unrecoverable error",
    "91CE": "[Error] Number of Applications limited to 28",
    "91DE": "[Error] File or application already exists",
    "91EE": "[Error] Could not complete NV-write operation due to loss of power",
    "91F0": "[Error] Specified file number does not exist",
    "91F1": "[Error] Unrecoverable error within file",
    "920x": "[Info] Writing to EEPROM successful after 'x' attempts",
    "9210": "[Error] Insufficient memory. No more storage available",
    "9240": "[Error] Writing to EEPROM not successful",
    "9301": "[Error] Integrity error",
    "9302": "[Error] Candidate S2 invalid",
    "9303": "[Error] Application is permanently locked",
    "9400": "[Error] No EF selected",
    "9401": "[Error] Candidate currency code does not match purse currency",
    "9402": "[Error] Candidate amount too high / Address range exceeded",
    "9403": "[Error] Candidate amount too low",
    "9404": "[Error] FID not found, record not found or comparison pattern not found",
    "9405": "[]Error Problems in the data field",
    "9406": "[Error] Required MAC unavailable",
    "9407": "[Error] Bad currency: purse engine has no slot with R3bc currency",
    "9408": "[Error] Selected file type does not match command / R3bc currency not supported in purse engine",
    "9580": "[Error] Bad sequence",
    "9681": "[Error] Slave not found",
    "9700": "[Error] PIN blocked and Unblock Try Counter is 1 or 2",
    "9702": "[Error] Main keys are blocked",
    "9704": "[Error] PIN not successfully verified, 3 or more PIN tries left",
    "9784": "[Error] Base key",
    "9785": "[Error] Limit exceeded – C-MAC key",
    "9786": "[Error] SM error – Limit exceeded – R-MAC key",
    "9787": "[Error] Limit exceeded – sequence counter",
    "9788": "[Error] Limit exceeded – R-MAC length",
    "9789": "[Error] Service not available",
    "9802": "[Error] No PIN defined",
    "9804": "[Error] Access conditions not satisfied, authentication failed",
    "9835": "[Error] ASK RANDOM or GIVE RANDOM not executed",
    "9840": "[Error] PIN verification not successful",
    "9850": "[Error] INCREASE or DECREASE could not be executed because a limit has been reached",
    "9862": "[Error] Authentication Error, application specific (incorrect MAC)",
    "9900": "[Error] 1 PIN try left",
    "9904": "[Error] PIN not successfully verified, 1 PIN try left",
    "9985": "[Error] Wrong status – Cardholder lock",
    "9986": "[Error] Missing privilege",
    "9987": "[Error] PIN is not installed",
    "9988": "[Error] Wrong status – R-MAC state",
    "9A00": "[Error] 2 PIN try left",
    "9A04": "[Error] PIN not successfully verified, 2 PIN try left",
    "9A71": "[Error] Wrong parameter value – Double agent AID",
    "9A72": "[Error] Wrong parameter value – Double agent Type",
    "9D05": "[Error] Incorrect certificate type",
    "9D07": "[Error] Incorrect session data size",
    "9D08": "[Error] Incorrect DIR file record size",
    "9D09": "[Error] Incorrect FCI record size",
    "9D0A": "[Error] Incorrect code size",
    "9D10": "[Error] Insufficient memory to load application",
    "9D11": "[Error] Invalid AID",
    "9D12": "[Error] Duplicate AID",
    "9D13": "[Error] Application previously loaded",
    "9D14": "[Error] Application history list full",
    "9D15": "[Error] Application not open",
    "9D17": "[Error] Invalid offset",
    "9D18": "[Error] Application already loaded",
    "9D19": "[Error] Invalid certificate",
    "9D1A": "[Error] Invalid signature",
    "9D1B": "[Error] Invalid KTU",
    "9D1D": "[Error] MSM controls not set",
    "9D1E": "[Error] Application signature does not exist",
    "9D1F": "[Error] KTU does not exist",
    "9D20": "[Error] Application not loaded",
    "9D21": "[Error] Invalid Open command data length",
    "9D30": "[Error] Check data parameter is incorrect (invalid start address)",
    "9D31": "[Error] Check data parameter is incorrect (invalid length)",
    "9D32": "[Error] Check data parameter is incorrect (illegal memory check area)",
    "9D40": "[Error] Invalid MSM Controls ciphertext",
    "9D41": "[Error] MSM controls already set",
    "9D42": "[Error] Set MSM Controls data length less than 2 bytes",
    "9D43": "[Error] Invalid MSM Controls data length",
    "9D44": "[Error] Excess MSM Controls ciphertext",
    "9D45": "[Error] Verification of MSM Controls data failed",
    "9D50": "[Error] Invalid MCD Issuer production ID",
    "9D51": "[Error] Invalid MCD Issuer ID",
    "9D52": "[Error] Invalid set MSM controls data date",
    "9D53": "[Error] Invalid MCD number",
    "9D54": "[Error] Reserved field error",
    "9D55": "[Error] Reserved field error",
    "9D56": "[Error] Reserved field error",
    "9D57": "[Error] Reserved field error",
    "9D60": "[Error] MAC verification failed",
    "9D61": "[Error] Maximum number of unblocks reached",
    "9D62": "[Error] Card was not blocked",
    "9D63": "[Error] Crypto functions not available",
    "9D64": "[Error] No application loaded",
    "9E00": "[Error] PIN not installed",
    "9E04": "[Error] PIN not successfully verified, PIN not installed",
    "9F00": "[Error] PIN blocked and Unblock Try Counter is 3",
    "9F04": "[Error] PIN not successfully verified, PIN blocked and Unblock Try Counter is 3",
    "9FXX": "[Success] [SW2] bytes of data are available and can be requested using GET RESPONSE",
    "9XXX": "[Unknown] Application related status (ISO/IEC 7816-3)",
}
