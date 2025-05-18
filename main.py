import qrcode

DEFAULT_INPUT_FILE = 'input.txt'

def generate_qr_code():
    try:
        with open(DEFAULT_INPUT_FILE, 'r') as file:
            url = file.readline().strip()
            filename = file.readline().strip()
    except FileNotFoundError:
        print(f"Error: Required file '{DEFAULT_INPUT_FILE}' not found.")
        print(f"Create a file named '{DEFAULT_INPUT_FILE}' with:")
        print("Line 1: URL to encode\nLine 2: Output filename (e.g., qr.png)")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if not url:
        print("Error: Missing URL in first line of input file")
        return
    if not filename:
        print("Error: Missing filename in second line of input file")
        return

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print(f"Successfully generated QR code saved as '{filename}'")
    except Exception as e:
        print(f"Error generating QR code: {e}")

if __name__ == "__main__":
    generate_qr_code()