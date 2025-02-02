from PIL import Image
import argparse
ASCII_CHARS = "@%#*+=-:.· "  

def scale_image(image, new_width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / original_width
    new_height = int(aspect_ratio * new_width * 0.55) 
    return image.resize((new_width, new_height))

def convert_to_grayscale(image):
    return image.convert("L")

def map_pixels_to_ascii(image):
    pixels = image.getdata()
    range_width = 256 // len(ASCII_CHARS)  
    ascii_str = ""
    for pixel in pixels:
        clamped_pixel = min(max(pixel, 0), 255)
        index = clamped_pixel // range_width
        index = min(index, len(ASCII_CHARS)-1)
        ascii_str += ASCII_CHARS[index]
    return ascii_str

def main():
    parser = argparse.ArgumentParser(description='Convert images to ASCII art')
    parser.add_argument('-i', '--input', required=True, help='Path to input image')
    parser.add_argument('-o', '--output', help='Path to output text file')
    parser.add_argument('-w', '--width', type=int, default=100, help='Width of ASCII output')
    args = parser.parse_args()
    try:
        image = Image.open(args.input)
        image = scale_image(image, args.width)
        image = convert_to_grayscale(image)
        ascii_str = map_pixels_to_ascii(image)
        pixel_count = len(ascii_str)
        ascii_str = "\n".join(
            [ascii_str[index:(index + args.width)] 
            for index in range(0, pixel_count, args.width)]
        )
        if args.output:
            with open(args.output, 'w') as f:
                f.write(ascii_str)
            print(f"ASCII art saved to {args.output}")
        else:
            print(ascii_str)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()