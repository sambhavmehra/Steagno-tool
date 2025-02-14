Stego Tool Overview
This is a command-line steganography tool that allows you to hide secret messages within images using the Least Significant Bit (LSB) steganography technique.
Key Features:

Message Hiding: Embeds text messages within image files without visible changes
Message Extraction: Recovers hidden messages from modified images
Progress Visualization: Shows real-time progress bars during operations
Colorful Interface: Uses colorama for an attractive CLI interface
Error Handling: Robust error checking for file operations and message size
Automatic Save Location: Intelligently selects appropriate save directories
Cross-platform Support: Works on Linux and other operating systems

Technical Details:

Uses PIL (Python Imaging Library) for image processing
Converts text to binary and modifies the least significant bits of pixel values
Supports RGB images
Stores message length in the first 32 bits
Creates timestamped output files
UTF-8 encoding for message handling
