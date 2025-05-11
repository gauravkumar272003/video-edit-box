from PIL import Image, ImageDraw

image_path = "WIN_20240102_14_23_43_Pro.jpg" 
img = Image.open(image_path)
draw = ImageDraw.Draw(img)
left_eye_box = (490, 250, 540, 290)   # (x1, y1, x2, y2)
right_eye_box = (580, 250, 630, 290)

# === Step 3: Create zoomed versions ===
zoom_size = (100, 100)
left_eye_zoom = img.crop(left_eye_box).resize(zoom_size)
right_eye_zoom = img.crop(right_eye_box).resize(zoom_size)

# === Step 4: Paste zoomed images ===
left_eye_pos = (50, 50)
right_eye_pos = (200, 50)
img.paste(left_eye_zoom, left_eye_pos)
img.paste(right_eye_zoom, right_eye_pos)

# === Step 5: Draw rectangles on original image ===
draw.rectangle(left_eye_box, outline="white", width=3)
draw.rectangle(right_eye_box, outline="white", width=3)

# === Step 6: Draw connecting lines ===
draw.line([left_eye_box[0], left_eye_box[1], left_eye_pos[0], left_eye_pos[1]], fill="white", width=2)
draw.line([right_eye_box[0], right_eye_box[1], right_eye_pos[0], right_eye_pos[1]], fill="white", width=2)

# === Step 7: Save output ===
output_path = "output_zoomed_eyes.jpg"
img.save(output_path)
print(f"Zoomed image saved as '{output_path}'")