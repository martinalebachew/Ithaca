import { execSync } from 'node:child_process';

export function runCommand(command, timeoutMs=20*1000) {
  return execSync(
    command, {
      timeout: timeoutMs,
      encoding: 'buffer',
      windowsHide: true
    }
  );
}
