import { globSync } from 'node:fs';

export function getPcapFiles(pcapDirectory) {
  return globSync(
    "**/*.pcap", {
      cwd: pcapDirectory
    }
  );
}