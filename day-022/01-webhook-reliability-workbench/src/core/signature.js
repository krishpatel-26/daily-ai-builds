function toHex(buffer) { return [...new Uint8Array(buffer)].map((value) => value.toString(16).padStart(2, "0")).join(""); }
export async function hmacSha256(rawBody, secret) {
  if (!globalThis.crypto?.subtle) throw new Error("Web Crypto is unavailable in this context.");
  const key = await crypto.subtle.importKey("raw", new TextEncoder().encode(String(secret)), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  return toHex(await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(String(rawBody))));
}
export function constantTimeEqual(left, right) {
  const a = String(left ?? ""); const b = String(right ?? ""); let mismatch = a.length ^ b.length;
  const max = Math.max(a.length, b.length);
  for (let index = 0; index < max; index += 1) mismatch |= (a.charCodeAt(index) || 0) ^ (b.charCodeAt(index) || 0);
  return mismatch === 0;
}
export async function verifyHmacSha256(rawBody, secret, expectedHex) {
  const actual = await hmacSha256(rawBody, secret); const expected = String(expectedHex ?? "").replace(/^sha256=/i, "").trim().toLowerCase();
  return constantTimeEqual(actual, expected);
}
