import os
from PIL import Image

def process_image(img_path, out_path):
    print(f"Processing {img_path} -> {out_path}")
    img = Image.open(img_path).convert("RGBA")
    datas = img.getdata()

    newData = []
    # Simple threshold for near-black/dark-navy
    # We will make pixels with R<30, G<30, B<40 transparent
    for item in datas:
        if item[0] < 35 and item[1] < 35 and item[2] < 45:
            # Calculate alpha based on how close it is to black for smooth feathering
            # the closer to 0, the more transparent
            # max val is ~35, let's map 0-35 to 0-255 alpha
            alpha = int(max(item[0], item[1], item[2]) * (255.0 / 35.0))
            # Just make it fully transparent if it's very dark
            if max(item[0], item[1], item[2]) < 15:
                newData.append((item[0], item[1], item[2], 0))
            else:
                newData.append((item[0], item[1], item[2], alpha))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(out_path, "PNG")

img_dir = "assets/images"
for f in os.listdir(img_dir):
    if f.lower().endswith(".jpg"):
        in_path = os.path.join(img_dir, f)
        out_path = os.path.join(img_dir, f.rsplit('.', 1)[0] + '.png')
        process_image(in_path, out_path)

print("Conversion complete.")
