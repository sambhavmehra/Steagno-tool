import os
import time
from PIL import Image
import numpy as np
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

def print_banner():
    """Print a colorful banner."""
    print(f"\n{Fore.CYAN}{'='*50}")
    print(Fore.YELLOW + Style.BRIGHT + """
    ███████╗████████╗███████╗ ██████╗  ██████╗ 
    ██╔════╝╚══██╔══╝██╔════╝██╔════╝ ██╔═══██╗
    ███████╗   ██║   █████╗  ██║  ███╗██║   ██║
    ╚════██║   ██║   ██╔══╝  ██║   ██║██║   ██║
    ███████║   ██║   ███████╗╚██████╔╝╚██████╔╝
    ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ 
    """)
    print(f"{Fore.MAGENTA}Created by: {Fore.GREEN}Sambhav")
    print(f"{Fore.White} Follow me on Insta :- Sambhav_7")
    print(f"{Fore.White}A Steganography Tool for Hiding Messages in Images")
    print(f"{Fore.CYAN}{'='*50}\n")

def text_to_binary(text):
    """Convert text to binary string."""
    byte_data = text.encode('utf-8')
    return ''.join(format(byte, '08b') for byte in byte_data)

def binary_to_text(binary):
    """Convert binary string back to text."""
    bytes_list = [binary[i:i+8] for i in range(0, len(binary), 8)]
    try:
        byte_values = [int(byte, 2) for byte in bytes_list]
        byte_data = bytes(byte_values)
        return byte_data.decode('utf-8', errors='replace')
    except Exception as e:
        return f"Error decoding message: {str(e)}"

def get_save_directory():
    """Get the appropriate save directory."""
    possible_paths = [
        os.path.expanduser("~/Pictures"),
        os.path.expanduser("~/Downloads"),
        os.path.expanduser("~")
    ]
    
    for path in possible_paths:
        if os.path.exists(path) and os.access(path, os.W_OK):
            return path
    return None

def print_progress(current, total):
    """Print a progress bar."""
    percent = (current / total) * 100
    bar_length = 40
    filled_length = int(bar_length * current // total)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'\r{Fore.CYAN}Progress: |{bar}| {percent:.1f}% ', end='\r')
    if current == total:
        print()

def hide_message(image_path, message):
    """Hide a message in an image."""
    try:
        print(f"\n{Fore.YELLOW}Processing image...")
        
        # Process the image
        image = Image.open(image_path)
        image = image.convert('RGB')
        image_array = np.array(image)

        binary_text = text_to_binary(message)
        binary_length = format(len(binary_text), '032b')
        binary_data = binary_length + binary_text

        flat_image = image_array.flatten()
        if len(binary_data) > len(flat_image):
            raise ValueError("Message is too large for this image.")

        # Modify LSBs with progress bar
        total_steps = len(binary_data)
        for i in range(total_steps):
            flat_image[i] = (flat_image[i] & 0xFE) | int(binary_data[i])
            if i % (total_steps // 100 + 1) == 0:
                print_progress(i, total_steps)
        print_progress(total_steps, total_steps)

        modified_array = flat_image.reshape(image_array.shape)
        modified_image = Image.fromarray(modified_array.astype('uint8'))

        # Save image
        save_dir = get_save_directory()
        if save_dir:
            timestamp = int(time.time())
            output_path = os.path.join(save_dir, f"stego_image_{timestamp}.png")
            modified_image.save(output_path)
            return f"{Fore.GREEN}Message hidden successfully!{Style.RESET_ALL}\nSaved to: {output_path}"
        else:
            raise ValueError("Could not find a writable directory to save the image.")

    except Exception as e:
        return f"{Fore.RED}Error: {str(e)}"

def extract_message(image_path):
    """Extract a message from an image."""
    try:
        print(f"\n{Fore.YELLOW}Extracting message...")
        
        image = Image.open(image_path)
        image = image.convert('RGB')
        image_array = np.array(image)
        flat_image = image_array.flatten()

        if len(flat_image) < 32:
            raise ValueError("Image too small to contain a message.")

        # Extract length
        binary_length = ''.join(str(pixel & 1) for pixel in flat_image[:32])
        message_length = int(binary_length, 2)

        if message_length <= 0 or message_length > len(flat_image) - 32:
            raise ValueError("Invalid message length detected.")

        # Extract message with progress bar
        binary_message = ''
        total_steps = message_length
        for i in range(32, 32 + message_length):
            binary_message += str(flat_image[i] & 1)
            if (i-32) % (total_steps // 100 + 1) == 0:
                print_progress(i-32, total_steps)
        print_progress(total_steps, total_steps)
        
        return binary_to_text(binary_message)

    except Exception as e:
        return f"{Fore.RED}Error: {str(e)}"

def print_menu():
    """Print the main menu."""
    print(f"\n{Fore.CYAN}Available Options:")
    print(f"{Fore.YELLOW}1. {Fore.WHITE}Hide a message in an image")
    print(f"{Fore.YELLOW}2. {Fore.WHITE}Extract a message from an image")
    print(f"{Fore.YELLOW}3. {Fore.WHITE}Exit")

def main():
    print_banner()
    
    while True:
        print_menu()
        choice = input(f"\n{Fore.GREEN}Enter your choice (1-3): {Fore.WHITE}")

        if choice == '1':
            image_path = input(f"\n{Fore.CYAN}Enter the path to the image: {Fore.WHITE}")
            if not os.path.exists(image_path):
                print(f"{Fore.RED}Error: Image file not found.")
                continue
                
            message = input(f"{Fore.CYAN}Enter the message to hide: {Fore.WHITE}")
            if not message:
                print(f"{Fore.RED}Error: Message cannot be empty.")
                continue
                
            result = hide_message(image_path, message)
            print(f"\n{result}")

        elif choice == '2':
            image_path = input(f"\n{Fore.CYAN}Enter the path to the image: {Fore.WHITE}")
            if not os.path.exists(image_path):
                print(f"{Fore.RED}Error: Image file not found.")
                continue
                
            result = extract_message(image_path)
            print(f"\n{Fore.GREEN}Extracted message: {Fore.WHITE}{result}")

        elif choice == '3':
            print(f"\n{Fore.YELLOW}Thank you for using Stego Tool! Goodbye!")
            print(f"{Fore.MAGENTA}Created by Sambhav{Style.RESET_ALL}")
            break

        else:
            print(f"\n{Fore.RED}Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
