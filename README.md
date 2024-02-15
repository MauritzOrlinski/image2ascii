# Image to ASCII
> A simple tool to generate Images in ASCII-Format for image visualization in terminal

## Summary 
This Image to ASCII project creates a txt file with a black and white image in ASCII-Style or gives produces a colorful ascii picture in terminal.

## How it's done?
To Simulate the luminosity with ASCII, we calculate, based on a given width value, the average luminosity per pixels and choose an ASCII-Letter to match a certain 
range of luminosity-values. For the colorful output we calculate the avg rgb value for each pixel and map it to terminal color. Then based on given preference we either print the picture to the terminal or save it to a file. 

## Installation
You will need to install the required packages, just run:
```shell
pip install -r requirements.txt
```

## Usage
To run the program, just run:
```shell
python3 main.py [-h] [-s] [-p] [-o OUTPUT_FILE] [-dl] [-c] input_file width [extendchar]

```

### Arguments
To see all available arguments, run:
```shell
python3 main.py --help
```
This will give you this explanation for the program arguments:
```shell
usage: main.py [-h] [-s] [-p] [-o OUTPUT_FILE] [-dl] [-c] input_file width [extendchar]

Convert image to text

positional arguments:
  input_file            Path to input file
  width                 Width of output text
  extendchar            you can use this to decide how wide one pixel should be, to balance out the distants between lines in your terminal or text editor

options:
  -h, --help            show this help message and exit
  -s, --store           Store output to file
  -p, --print_out       Store output to file and print to terminal
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Path to output file
  -dl, --deactivate_luminosity
                        Decide if you want the program to simulate luminosity with charsthis should be disabled when using colorful mode in terminals with no dark background. If this is disabled --colorful has to be enabled
  -c, --colorful        Make the output colorful

```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
