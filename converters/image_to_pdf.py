from PIL import Image
import sys

# run this script with the following command:
# python image_to_pdf.py <image_file> <output_file>.pdf

if len(sys.argv) != 3:
    print("Usage: python image_to_pdf.py <image_file> <output_file>")
    sys.exit(1)

image_file = sys.argv[1]
output_file = sys.argv[2]

image_extensions = ["png", "jpg", "jpeg", "gif"]
if image_file.split(".")[-1] not in image_extensions:
    print("Image file must be one of the following types: ", image_extensions)
    sys.exit(1)

try:
    with Image.open(image_file) as im:
        image  = im.convert('RGB')
        if not output_file.endswith(".pdf"):
            output_file = output_file + ".pdf"
        image.save(output_file)
except FileNotFoundError:
    print("Image file not found")
    sys.exit(1)
    

    
