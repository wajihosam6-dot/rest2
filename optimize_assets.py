import os
import shutil
from PIL import Image, ImageEnhance, ImageFilter

input_dir = 'ABOUT'
output_dir = 'rest-landing-v5-fixed/public/assets/real'
os.makedirs(output_dir, exist_ok=True)

# Copy videos
for v in ['video_2026-10-28_19-45-26.mp4', 'video_2026-10-28_19-45-26 (2).mp4']:
    src = os.path.join(input_dir, v)
    if os.path.exists(src):
        dst_name = 'pool_live_water.mp4' if 'video_2026-10-28_19-45-26.mp4' == v else 'rest_intro_silk.mp4'
        dst = os.path.join(output_dir, dst_name)
        shutil.copy2(src, dst)
        print(f"Copied {v} -> {dst_name}")

# Photo curation mapping with semantic names
photo_map = {
    'photo_4_2026-10-28_19-45-25.jpg': 'pool_waterfall_fountain',
    'photo_11_2026-10-28_19-45-25.jpg': 'hikaya_sunken_lounge',
    'photo_21_2026-10-28_19-45-26.jpg': 'hikaya_firepit_detail',
    'photo_22_2026-10-28_19-45-26.jpg': 'majlis_golden_sunlight',
    'photo_18_2026-10-28_19-45-26.jpg': 'majlis_grand_hall',
    'photo_15_2026-10-28_19-45-26.jpg': 'majlis_seating_luxury',
    'photo_17_2026-10-28_19-45-26.jpg': 'bustan_stone_terrace',
    'photo_13_2026-10-28_19-45-25.jpg': 'neon_rest_floral_swing',
    'photo_23_2026-10-28_19-45-26.jpg': 'indoor_floral_swing_staircase',
    'photo_9_2026-10-28_19-45-25.jpg': 'dining_pergola_cafe',
    'photo_10_2026-10-28_19-45-25.jpg': 'courtyard_cabin_cabana',
    'photo_6_2026-10-28_19-45-25.jpg': 'courtyard_playground_lawn',
    'photo_12_2026-10-28_19-45-25.jpg': 'courtyard_heritage_facade',
    'photo_14_2026-10-28_19-45-26.jpg': 'courtyard_panoramic_canopy',
    'photo_16_2026-10-28_19-45-26.jpg': 'signboard_facilities_directory',
    'photo_7_2026-10-28_19-45-25.jpg': 'sunken_seating_courtyard',
    'photo_1_2026-10-28_19-45-25.jpg': 'kids_wooden_cabin',
    'photo_8_2026-10-28_19-45-25.jpg': 'sunset_beach_roses',
    'photo_2_2026-10-28_19-45-25.jpg': 'bougainvillea_sea_balcony',
    'photo_19_2026-10-28_19-45-26.jpg': 'window_mirror_floral',
    'photo_20_2026-10-28_19-45-26.jpg': 'decor_table_piece',
}

def enhance_image(img):
    # Convert to RGB if needed
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # 1. Subtle Contrast boost (+12%)
    enh_con = ImageEnhance.Contrast(img)
    img = enh_con.enhance(1.12)
    
    # 2. Rich Color Saturation boost (+15%)
    enh_col = ImageEnhance.Color(img)
    img = enh_col.enhance(1.15)
    
    # 3. Brightness adjustment (+4%)
    enh_bri = ImageEnhance.Brightness(img)
    img = enh_bri.enhance(1.04)
    
    # 4. Sharpness boost (+25%)
    enh_sha = ImageEnhance.Sharpness(img)
    img = enh_sha.enhance(1.25)
    
    return img

print("Processing and enhancing photos...")
for orig_name, clean_name in photo_map.items():
    p = os.path.join(input_dir, orig_name)
    if not os.path.exists(p):
        continue
    
    with Image.open(p) as img:
        enhanced = enhance_image(img)
        
        # Save as high quality WebP
        webp_path = os.path.join(output_dir, f"{clean_name}.webp")
        enhanced.save(webp_path, 'WEBP', quality=90, method=6)
        
        # Also save high-res jpg fallback
        jpg_path = os.path.join(output_dir, f"{clean_name}.jpg")
        enhanced.save(jpg_path, 'JPEG', quality=90, optimize=True)
        
        print(f"Enhanced {orig_name} -> {clean_name}.webp ({enhanced.size})")

# Process logo
for logo_f in ['logo.jpg', 'logo.webp', 'logo_alt.jpg']:
    lp = os.path.join('rest_logo', logo_f)
    if os.path.exists(lp):
        with Image.open(lp) as limg:
            clean_l = enhance_image(limg)
            base = os.path.splitext(logo_f)[0]
            clean_l.save(os.path.join(output_dir, f"brand_{base}.webp"), 'WEBP', quality=95)
            print(f"Processed logo: brand_{base}.webp")

print("All enhancements complete!")
