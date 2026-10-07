import os
from PIL import Image

img_dir = "assets/images"
files = [
    "BurningBlueFireOrb.jpg", "HologramAvatar.jpg", "GoldShield.jpg", 
    "CrimsonGlassSlab.jpg", "ObsidianGoldSlab.jpg", "GlassCapsuleTube.jpg", "GoldMicrochip.jpg"
]

def convert():
    for f in files:
        in_path = os.path.join(img_dir, f)
        if not os.path.exists(in_path):
            print(f"File not found: {in_path}")
            continue
            
        out_path = os.path.join(img_dir, f.replace('.jpg', '.png'))
        try:
            img = Image.open(in_path).convert("RGBA")
            datas = img.getdata()
            
            newData = []
            for item in datas:
                lum = max(item[0], item[1], item[2])
                if lum < 15:
                    newData.append((item[0], item[1], item[2], 0))
                elif lum < 40:
                    alpha = int(((lum - 15) / 25.0) * 255)
                    newData.append((item[0], item[1], item[2], alpha))
                else:
                    newData.append(item)
                    
            img.putdata(newData)
            img.save(out_path, "PNG")
            print(f"Saved {out_path}")
        except Exception as e:
            print(f"Error on {f}: {e}")

if __name__ == "__main__":
    convert()
