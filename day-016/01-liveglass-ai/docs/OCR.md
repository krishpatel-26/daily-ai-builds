# OCR notes

Tesseract.js recognizes text lines and bounding boxes from a captured primary-display PNG. Source language selections map to these OCR models: auto/en uses eng; German deu; French fra; Spanish spa; Italian ita; Portuguese por; Dutch nld; Turkish tur; Russian rus; Japanese jpn; Simplified Chinese chi_sim.

The first scan may download OCR language data. Not every model has been manually tested. Coordinates are scaled from capture thumbnail pixels to the logical display bounds, so DPI scaling must be validated on Windows 10/11, especially on mixed-resolution displays.

The main process filters lines shorter than two characters and confidence below 30. Small, rotated, low-contrast or animated text can be missed.