# Stego Tool 🔐

A powerful command-line steganography tool for hiding secret messages in images using LSB (Least Significant Bit) technique.

```
███████╗████████╗███████╗ ██████╗  ██████╗ 
██╔════╝╚══██╔══╝██╔════╝██╔════╝ ██╔═══██╗
███████╗   ██║   █████╗  ██║  ███╗██║   ██║
╚════██║   ██║   ██╔══╝  ██║   ██║██║   ██║
███████║   ██║   ███████╗╚██████╔╝╚██████╔╝
╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ 
```

## Features ✨

- Hide text messages within images
- Extract hidden messages from images
- Real-time progress visualization
- Colorful command-line interface
- Automatic save location detection
- Robust error handling
- Cross-platform compatibility

## Prerequisites 📋

- Python 3.6 or higher
- pip (Python package installer)

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/yourusername/stego-tool.git
cd stego-tool
```

2. Create and activate a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage 🛠️

Run the tool:
```bash
python3 stego.py
```

### Hide a Message 📝

1. Choose option 1 from the menu
2. Enter the path to your source image
3. Type your secret message
4. The modified image will be saved automatically

### Extract a Message 🔍

1. Choose option 2 from the menu
2. Enter the path to the image containing the hidden message
3. The tool will display the extracted message

## Technical Details 🔧

- Uses PIL (Python Imaging Library) for image processing
- Implements LSB steganography technique
- Supports RGB images
- UTF-8 encoding for message handling
- 32-bit message length header
- Timestamped output files

## Dependencies 📚

- Pillow (PIL): Image processing
- NumPy: Array operations
- Colorama: Terminal colors

## Limitations ⚠️

- Maximum message length depends on image size (1 character = 8 pixels)
- Works best with PNG or BMP images
- JPEG compression may corrupt hidden messages
- Requires read/write permissions in save directory

## Best Practices 💡

1. Use uncompressed image formats (PNG, BMP)
2. Ensure sufficient image size for your message
3. Keep backup of original images
4. Use virtual environment for installation
5. Check terminal permissions before running

## Error Messages 🚫

The tool provides clear error messages for common issues:
- File not found
- Insufficient image size
- Invalid message length
- Permission denied
- Decoding errors

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Author ✨

Sambhav

## Acknowledgments 🙏

- Python Imaging Library (PIL) team
- NumPy developers
- Colorama project contributors

## Support 💪

If you encounter any issues or have questions, please open an issue in the repository.

---

Made with ❤️ by Sambhav
