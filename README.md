# Image to ICO Converter

A minimalist, high-speed drag-and-drop Windows icon converter. Part of the **DAD (Drag and Drop)** tool suite by **CER3ERUS TECH**.

Easily convert any image (`.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`, `.tiff`) into a multi-resolution Windows icon (`.ico`) file by dropping it directly onto the shortcut or batch script.

---

## Features

- **Drag & Drop Simplicity**: Drag one or multiple image files and drop them onto `Cer3erusI2ICO.bat` or its desktop shortcut.
- **Multi-Resolution Icon**: Generates a Windows `.ico` with standard sizes up to `256x256`. Pillow uses high-quality Lanczos resampling for smaller sizes; sizes larger than the source image are not added:
  - `256x256` (High-DPI / Large Icons)
  - `128x128`
  - `64x64`
  - `48x48` (Windows Desktop standard)
  - `32x32` (File Explorer standard)
  - `16x16` (Taskbar / Title bar standard)
- **Transparency Preservation**: Automatically converts to `RGBA` to preserve full alpha channel transparency.
- **Duplicate-Safe Output Names**: Never replaces an existing output file. If `photo.ico` already exists, the next result is saved as `photo (1).ico`, then `photo (2).ico`, and so on.
- **Verified Source Cleanup**: Deletes the original only after the output file is found and verified as a readable `.ico`. If verification fails, the original is kept. Back it up first if you need to keep it regardless.
- **Batch Processing**: Supports dragging and converting multiple files simultaneously.

---

## Requirements

- **Operating System**: Windows 10 / Windows 11
- **Python**: Python 3.10+
- **Library**: `Pillow`

Install dependency:
```powershell
pip install -r requirements.txt
```

---

## Setup

1. Keep the downloaded program files together in the folder where you want to use the converter.
2. Double-click `Shortcut Creator for Distribution.vbs`. It creates `Cer3erusI2ICO.lnk` beside the launcher and applies the included `.ico` file.
3. Copy `Cer3erusI2ICO.lnk` to your Desktop if you want a convenient drop target. If you move the program folder, run the shortcut creator again and replace any old shortcut.

## How to Use

1. Drag and drop one or more supported image files onto `Cer3erusI2ICO.lnk` or `Cer3erusI2ICO.bat`.
2. The `.ico` file will be generated in the same directory as the original image.
3. If an output with that name already exists, a numbered filename is used. The source image is removed only after the new `.ico` is found and verified as readable.

> **Image quality:** The converter preserves transparency and uses Lanczos resampling when creating smaller icon sizes. Converting between formats or reducing image dimensions can change pixel values and cannot restore detail that was absent from the source.

---
---

## Author & Organization

- **Organization**: CER3ERUS TECH
- **Project**: DAD (Drag and Drop Tool Suite)

## Voluntary Support

If you find this project useful, you may optionally support its development with TUSD on the TRON network. Support is entirely voluntary and does not provide additional features or change the project's usage terms.

**TUSD (TRON) address:** `TQSPCZAYQGe5pAbMMLtoDpS2gyQMWvXuQW`

![TUSD on TRON donation QR code](TUSD-TRON-QR.png)
