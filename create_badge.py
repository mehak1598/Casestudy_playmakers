from PIL import Image, ImageDraw


def convert_to_badge(image_path, output_path):
    # Load the image using Pillow
    image = Image.open(image_path)
    # Create a new image with a white background
    badge = Image.new("RGB", (512, 512), (255, 255, 255))
    width, height = image.size
    max_size = max(width, height)
    scale = 512 / max_size
    new_width = int(width * scale)
    new_height = int(height * scale)
    resized_image = image.resize((new_width, new_height))
    x_offset = (512 - new_width) // 2
    y_offset = (512 - new_height) // 2
    badge.paste(resized_image, (x_offset, y_offset))

    # Create a circular mask for the badge
    mask = Image.new("L", badge.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse([(0, 0), badge.size], fill=255)

    # Apply the circular mask to the badge
    badge.putalpha(mask)
    badge.save(output_path)
    # Check if the badge contains happy colors
    pixel_colors = badge.getdata()
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

    for pixel in pixel_colors:
        if pixel[3] != 0:  # Ignore transparent pixels
            for color_name, (color_min, color_max) in color_ranges.items():
                if color_min[0] <= r <= color_max[0] and \
                        color_min[1] <= g <= color_max[1] and \
                        color_min[2] <= b <= color_max[2]:
                    break
            else:
                return False, "Image does not contain happy colors"

    return True, "Badge created successfully"


# Example usage:
input_image_path = "C:/Users/mehak/Downloads/banner.png"
output_badge_path = "C:/Users/mehak/Downloads/output_badge.png"
result, message = convert_to_badge(input_image_path, output_badge_path)
print(message)
