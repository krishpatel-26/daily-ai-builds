# Troubleshooting

## npm is not recognized
Install Node.js 22 LTS and reopen PowerShell.

## First scan is slow
Tesseract may need to download model data. Allow this to complete, then retry.

## Local translation unavailable
Install Argos Translate in the Python environment used by the app and install a source-to-English package. Confirm python or py -3 is available.

## API fallback fails
Check endpoint URL, response shape, API key requirements and quotas. Remote endpoints require HTTPS and must return a translatedText field.

## Overlay position is wrong
Test at 100% scaling first. This MVP maps thumbnail pixels to primary display bounds and needs validation for mixed-DPI setups.

## Shortcut does nothing
Close software that uses the same key combination. Secure desktop windows or elevated apps may not be capturable in the normal user session.