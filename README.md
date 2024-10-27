# Background Removal with `rembg`

This project provides a simple solution for removing image backgrounds using the `rembg` library.

## Overview

This script uses the `rembg` library to remove the background from an input image and save the output as a transparent PNG.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/azafar224/image_Background_Remover.git
   cd image_Background_Remover
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Place your input image in the `images` folder, or specify the full path to the image.

Run the script with:

```bash
python main.py
```

## Example

The script will load `images/input.jpg` and save the background-removed image as `images/output.png`.

## File Structure

```plaintext
background_removal/
├── README.md
├── requirements.txt
├── main.py
└── images/
    ├── input.jpg
    └── output.png
```

- **`README.md`**: Contains instructions and project information.
- **`requirements.txt`**: Lists the necessary Python packages.
- **`main.py`**: The main Python script that removes the background from the input image.
- **`images/`**: Folder containing example images.
  - `input.jpg`: Example input image.
  - `output.png`: Generated output with the background removed.

## Requirements

- `rembg`
- `Pillow`

## License

This project is licensed under the MIT License.
