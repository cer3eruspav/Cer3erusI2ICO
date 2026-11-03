"""
Image to ICO Converter
Part of the DAD (Drag and Drop) tool suite by CER3ERUS TECH.
Converts input images (.png, .jpg, .jpeg, .webp, .bmp, .tiff) into multi-resolution Windows icon (.ico) files.
Automatically installs required libraries on first launch.
"""

import os
import sys
import subprocess

REQUIRED_PACKAGES = ["Pillow"]

def ensure_dependencies():
    """Checks and automatically installs missing libraries on first run."""
    missing = []
    for pkg in REQUIRED_PACKAGES:
        try:
            __import__("PIL")
        except ImportError:
            missing.append(pkg)

    if missing:
        print("==================================================")
        print("    Image to ICO - Initial Setup                  ")
        print("==================================================")
        print(f"[*] Missing required libraries: {', '.join(missing)}")
        print("[*] Installing missing libraries via pip, please wait...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
            print("[+] All dependencies installed successfully!\n")
        except Exception as e:
            print(f"[!] Warning: Failed to install dependencies automatically: {e}")
            print("[!] Please run 'pip install -r requirements.txt' manually.\n")

ensure_dependencies()

from PIL import Image

SUPPORTED_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff')
ICON_RESOLUTIONS = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]


def convert_to_ico(image_path: str) -> str | None:
    """
    Converts a single image file into Windows ICO format with multiple standard resolutions.
    Preserves RGBA transparency channel.
    """
    try:
        with Image.open(image_path) as img:
            # Ensure RGBA mode to retain icon transparency
            if img.mode != 'RGBA':
                img = img.convert('RGBA')

            output_path = save_to_unique_path(
                img,
                image_path,
                ".ico",
                "ICO",
                sizes=ICON_RESOLUTIONS
            )
            print(f"[CREATED] {os.path.basename(output_path)}")
            return output_path
    except Exception as e:
        print(f"[ERROR] Failed to convert {image_path}: {e}")
        return None


def save_to_unique_path(image, image_path: str, extension: str, image_format: str, **save_options) -> str:
    """Saves an image without replacing an existing file, adding numbered suffixes as needed."""
    base_dir = os.path.dirname(image_path)
    file_name = os.path.splitext(os.path.basename(image_path))[0]
    suffix = 0

    while True:
        numbered_name = file_name if suffix == 0 else f"{file_name} ({suffix})"
        output_path = os.path.join(base_dir, f"{numbered_name}{extension}")

        try:
            with open(output_path, "xb") as output_file:
                try:
                    image.save(output_file, format=image_format, **save_options)
                except Exception:
                    output_file.close()
                    os.remove(output_path)
                    raise
            return output_path
        except FileExistsError:
            suffix += 1


def verify_output_file(output_path: str, expected_format: str) -> bool:
    """Checks that the output exists and can be opened as the expected image format."""
    # Confirm the saved file exists and is readable before allowing source cleanup.
    if not os.path.isfile(output_path):
        print(f"[ERROR] Converted output was not found: {output_path}")
        return False

    try:
        with Image.open(output_path) as output_image:
            if output_image.format != expected_format:
                print(f"[ERROR] Unexpected output format for {output_path}: {output_image.format}")
                return False
            output_image.verify()
        return True
    except Exception as e:
        print(f"[ERROR] Converted output could not be verified: {output_path}: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Please drag and drop image file(s) onto this script or its shortcut.")
        return

    # Filter supported image files
    input_files = [
        f for f in sys.argv[1:]
        if os.path.exists(f) and f.lower().endswith(SUPPORTED_EXTENSIONS)
    ]

    if not input_files:
        print("[ERROR]: No supported image files found.")
        return

    for img_file in input_files:
        output_path = convert_to_ico(img_file)
        if output_path and verify_output_file(output_path, "ICO"):
            try:
                # Remove source file only after the output has been verified
                os.remove(img_file)
                print(f"[CLEANUP] Deleted original file: {os.path.basename(img_file)}")
            except Exception as e:
                print(f"[WARNING] Could not delete original file {img_file}: {e}")
        else:
            print(f"[WARNING] Original file was kept because the converted output was not verified: {os.path.basename(img_file)}")

    print("\nProcessing finished. Review the messages above for conversion or cleanup warnings.")
    input("Press Enter to close this window...")


if __name__ == "__main__":
    main()
