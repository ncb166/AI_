import os
from PIL import Image, ImageEnhance
import random

# Thư mục gốc chứa các thư mục con như Bear, Cat, Dog,...
input_dir = r'C:\Bach\AI\animal_data'
output_dir = r'C:\Bach\AI\animal_data_new'

# Tạo thư mục output gốc nếu chưa có
os.makedirs(output_dir, exist_ok=True)

def random_color(image):
    image = image.convert("RGB")
    r, g, b = image.split()

    enhancer_r = ImageEnhance.Brightness(r)
    enhancer_g = ImageEnhance.Brightness(g)
    enhancer_b = ImageEnhance.Brightness(b)

    r = enhancer_r.enhance(random.uniform(0.3, 1.5))
    g = enhancer_g.enhance(random.uniform(0.3, 1.5))
    b = enhancer_b.enhance(random.uniform(0.3, 1.5))

    return Image.merge("RGB", (r, g, b))

# Duyệt qua các thư mục con trong input_dir
for folder_name in os.listdir(input_dir):
    subfolder_path = os.path.join(input_dir, folder_name)
    
    if not os.path.isdir(subfolder_path):
        continue  # Bỏ qua nếu không phải thư mục

    # Tạo thư mục con trong output_dir tương ứng
    output_subfolder = os.path.join(output_dir, folder_name)
    os.makedirs(output_subfolder, exist_ok=True)

    for idx, filename in enumerate(os.listdir(subfolder_path)):
        if filename.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif')):
            image_path = os.path.join(subfolder_path, filename)
            image = Image.open(image_path).convert("RGB")
            image = image.resize((224, 224))

            base_name = f"{folder_name.lower()}_{idx+1}"

            # 1. Ảnh gốc
            image.save(os.path.join(output_subfolder, f"{base_name}_1.jpg"))

            # 2. Ảnh xoay 180
            image.rotate(180, expand=True).save(os.path.join(output_subfolder, f"{base_name}_2.jpg"))

            # 3. Ảnh làm tối
            dark_image = ImageEnhance.Brightness(image).enhance(0.2)
            dark_image.save(os.path.join(output_subfolder, f"{base_name}_3.jpg"))

            # 4. Ảnh xoay 90
            image.rotate(90, expand=True).save(os.path.join(output_subfolder, f"{base_name}_4.jpg"))

            # 5–10. Ảnh xoay ngẫu nhiên và đổi màu
            for i in range(6):
                rotated = image.rotate(random.uniform(0, 360), expand=True)
                rotated = rotated.resize((224, 224))
                colored = random_color(rotated)
                colored.save(os.path.join(output_subfolder, f"{base_name}_{5+i}.jpg"))

print("Done.")
