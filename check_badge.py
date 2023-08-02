from PIL import Image, ImageDraw


def check_badge(image_path):
    # Load the image using Pillow
    image = Image.open(image_path)
    # Verify image size
    if image.size != (512, 512):
        return False, "Image size should be 512x512."

    # Verify if non-transparent pixels are within a circle
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse([(0, 0), image.size], fill=255)
    pixel_colors = image.getdata()
    has_alpha_channel = image.mode == "RGBA"
    for pixel in pixel_colors:
        if has_alpha_channel and pixel[3] == 0:
            # Check if the corresponding mask pixel is inside the circle
            x, y = pixel[0], pixel[1]
            if mask.getpixel((x, y)) == 255:
                return False, "Non-transparent pixels are not within a circle."

    color_ranges = {
        # Yellow
        "yellow": ((230, 180, 0), (255, 255, 130)),
        # Orange
        "orange": ((240, 61, 0), (255, 179, 0)),
        # Pink
        "pink": ((224, 110, 180), (255, 192, 219)),
        # Red
        "red": ((240, 0, 0), (255, 60, 50)),
        # Peach
        "peach": ((240, 180, 90), (255, 220, 185)),
        # Light Pink
        "light_pink": ((200, 110, 130), (255, 182, 193)),
        # Lilac
        "lilac": ((190, 150, 200), (200, 170, 200)),
    }

    for pixel in pixel_colors:
        # Extract RGB components from the pixel
        r, g, b = pixel[:3]
        #print(r,g,b)

        # Check if the pixel colour matches any of the colour ranges above
        for color_name, (color_min, color_max) in color_ranges.items():
            if color_min[0] <= r <= color_max[0] and \
                    color_min[1] <= g <= color_max[1] and \
                    color_min[2] <= b <= color_max[2]:
                break
        else:
            return False, "Image does not contain happy colors"

    return True, "Image passes all conditions."


# Example usage:
result, message = check_badge("C:/Users/mehak/Downloads/image_badge2.png")
print(message)
