# 🖼️ Graphical CLI Editor

This project is a simple graphical editor operated from the command line (CLI) that allows you to perform various basic graphical operations on images.

## ✨ Features
The editor supports the following operations:
- `--mirror`: Mirrors the image horizontally.
- `--lighten <0-100>`: Lightens the image by the specified percentage.
- `--darken <0-100>`: Darkens the image by the specified percentage.
- `--inverse`: Creates an inverse image (negative).
- `--bw`: Converts the image to grayscale.
- `--sharpen`: Applies a sharpening filter to the image.
- `--blur`: Applies a blurring filter to the image.
- `--ed`: Applies the Sobel–Feldman edge detection filter.
- `--rc`: Applies the Roberts cross edge detection filter.
- `--rotate [90, 180, 270]`: Rotates the image 90, 180, or 270 degrees to the right.

## ⚙️ Installation
* Clone the repository using SSH or HTTPS
    * SSH: `git@gitlab.fit.cvut.cz:BI-PYT/B232/princrom.git`
    * HTTPS: `https://gitlab.fit.cvut.cz/BI-PYT/B232/princrom.git`
* Navigate to the project directory
    * `cd editor`
* Create and activate a virtual environment
    * `python3 -m venv venv`
    * `source venv/bin/activate`
* Install dependencies
    * `pip install -r requirements.txt`

## 🚀 Usage
Run the program from the command line with the desired parameters:
* `python main.py [OPERATION] INPUT_IMAGE_PATH OUTPUT_IMAGE_PATH`

### 📝 Command Examples

* Rotate an image 90 degrees to the right:
    * `python main.py --rotate 90 input.jpg output.jpg`
* Convert an image to grayscale and lighten it by 25%:
    * `python main.py --bw --lighten 25 input.jpg output.jpg`
* Apply a sharpening filter and then darken the image by 10%:
    * `python main.py --sharpen --darken 10 input.jpg output.jpg`

## ✅ Testing
To run the tests, use the command `pytest`.

## 👤 Author
Roman Princ, CTU-FIT, princrom@fit.cvut.cz
