import * as protobuf_container from 'protobufjs';
import { env } from '$env/dynamic/private';
import { runCommand } from '$lib/helpers/server/subprocess';

const protobuf = protobuf_container.default;
const bridge = protobuf.loadSync(`${env.CODE_ROOT_PATH}/Interface/interface.proto`);
const PcapParseResponse = bridge.lookupType("PcapParseResponse");

const PARSER_PREFIX = `python3 ${env.CODE_ROOT_PATH}/Parser/Parser.py`;
const LENGTH_SIZE = 4;

function decodeLengthBE(buffer) {
  let length = 0;
  for (let i = 0; i < LENGTH_SIZE; i++) {
    length *= (2 ** 8);
    length += buffer[i];
  }

  return length;
}

export function parsePcapFile(filename) {
  const output = runCommand(`${PARSER_PREFIX} ${env.PCAP_FILES_DIRECTORY}/${filename}`);
  if ((output.length <= LENGTH_SIZE) || ((output.length - LENGTH_SIZE) != decodeLengthBE(output))) {
    return;
  }

  const rawResponse = output.subarray(LENGTH_SIZE);
  if (PcapParseResponse.verify(rawResponse)) return;

  const response = PcapParseResponse.decode(rawResponse);
  if (!response.status) return;

  return [response.commands, response.responses];
}