from PIL import Image
from tkinter import Tk, filedialog
import os

# Hide main tkinter window
Tk().withdraw()

# Select multiple PNG files
files = filedialog.askopenfilenames(
    title="Select at least 5 PNG images",
    filetypes=[("PNG Images", "*.png")]
)

if len(files) < 5:
    print("❌ Please select at least 5 images.")
    exit()

# Output folder
output_folder = "webp_images"
os.makedirs(output_folder, exist_ok=True)

for file in files:
    img = Image.open(file)

    # Preserve transparency if present
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA")

    # Optional resize for size reduction
    MAX_WIDTH = 1920
    if img.width > MAX_WIDTH:
        ratio = MAX_WIDTH / img.width
        img = img.resize(
            (MAX_WIDTH, int(img.height * ratio)),
            Image.LANCZOS
        )

    filename = os.path.basename(file)
    webp_name = os.path.splitext(filename)[0] + ".webp"

    img.save(
        os.path.join(output_folder, webp_name),
        format="WEBP",
        quality=60,      # Adjust quality (0-100)
        method=6         # Best compression
    )

print(f"✅ Converted {len(files)} PNG images to WebP.")