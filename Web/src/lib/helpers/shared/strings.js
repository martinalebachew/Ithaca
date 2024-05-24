const EMPTY_VALUES = [undefined, null, ""];
const HEX_DELIMITER = ":";

export function safeAccess(value, fallback="") {
  if (EMPTY_VALUES.includes(value)) return fallback;
  return value;
}

export function hex(value) {
  if (value === undefined) return "";
  if (value === null) return "";

  if (typeof(value) === "number") {
    return value.toString(16).padStart(2, '0');
  }

  throw TypeError("Unsupported type!");
}

export function decimal(value) {
  if (value === undefined) return "";
  if (value === null) return "";

  if (typeof(value) !== "number") {
    throw TypeError("Unsupported type!");
  }

  return safeAccess(value.toString(10));
}

export function hexify64(encoded) {
  if (encoded === undefined) return "";
  if (encoded === null) return "";
  if (encoded === "") return "";

  let output = [];
  for (const byte of atob(encoded)) {
    output.push(hex(byte.charCodeAt(0)));
  }

  return output.join(HEX_DELIMITER);
}