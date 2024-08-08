# Steganography

# Steganography - Hide a Secret Text Message in an Image

This is a simple steganography application that allows users to hide and retrieve secret text messages in images. The application is built using Python and leverages libraries such as tkinter for the GUI, OpenCV for image processing, and hashlib for password hashing.

## Features

- Load an image from your local system.
- Enter a secret message and a password to hide the message in the image.
- Save the modified image with the hidden message.
- Retrieve the hidden message from the modified image using the correct password.

## Prerequisites

Make sure you have Python installed on your system. You will also need to install the following libraries:

- `tkinter`
- `Pillow`
- `opencv-python`
- `hashlib` (This is included in the standard Python library, so no need to install it separately)

You can install the required libraries using pip:

```sh
pip install pillow opencv-python
```

## Usage

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/steganography.git
   cd steganography
   ```

2. **Run the application:**

   ```sh
   python steganography.py
   ```

3. **Using the application:**
   - **Open Image**: Click the "Open Image" button to load an image file.
   - **Enter Secret Message**: Type your secret message in the text box provided.
   - **Enter Password**: Type a password that will be used to secure your message.
   - **Hide Data**: Click the "Hide Data" button to embed the secret message into the image.
   - **Save Image**: Click the "Save Image" button to save the modified image with the hidden message.
   - **Show Data**: Click the "Show Data" button to retrieve the hidden message from the image using the correct password.

## File Structure

- `steganography.py`: The main script for running the application.
- `icon.png`: Icon used for the application window (Make sure to have this image in the same directory).
- `cyberlogo.png`: Logo displayed in the application window (Make sure to have this image in the same directory).

## Libraries Used

- `tkinter`: For creating the GUI.
- `Pillow (PIL)`: For handling images.
- `os`: For file and directory operations.
- `opencv-python (cv2)`: For reading and manipulating images.
- `hashlib`: For hashing the password.
  ## GUI
![image](https://github.com/user-attachments/assets/f0ecbb49-73c3-488a-83fa-9908500dc73e)
## encoding
![image](https://github.com/user-attachments/assets/279b6fe4-c9f5-451d-afd0-b944de9143d3)

## decoding
![image](https://github.com/user-attachments/assets/8939afb8-0b19-4d09-8353-8f2479651c57)




## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspiration from various steganography tutorials and resources.
- Libraries and frameworks used in this project.

---
