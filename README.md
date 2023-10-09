# Image to ASCII
> A simple tool to generate Images in ASCII-Format

## Summary 
This Image to ASCII project creates a txt file with a black and white image in ASCII-Style.

## How it's done?
Based on a given width value, we calculate the average luminosity per pixels and choose an ASCII-Letter to match a certain 
range of luminosity-values. Then based on given preference we either print the picture to the terminal or save it to a file.

## Installation
You will need to install the required packages, just run:
```shell
pip install -r requirements.txt
```

## Usage
To run the program, just run:
```shell
python3 main.py Arguments
```

### Arguments
To see all available arguments, run:
```shell
python3 main.py --help
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
