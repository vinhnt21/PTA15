from PIL import Image
import os


def resize_images_in_folder(folder_path, output_folder, size=(500, 500)):
    # Tạo thư mục đầu ra nếu chưa có
    os.makedirs(output_folder, exist_ok=True)

    # Duyệt qua tất cả các file trong thư mục
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)

        # Kiểm tra nếu là file ảnh
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            with Image.open(img_path) as img:
                # Tính toán kích thước mới, giữ nguyên tỷ lệ
                img.thumbnail(
                    size, Image.LANCZOS
                )  # Sửa từ Image.ANTIALIAS thành Image.LANCZOS

                # Tạo nền trắng
                new_img = Image.new("RGB", size, (255, 255, 255))

                # Tính toán vị trí để đặt ảnh vào giữa nền
                paste_position = (
                    (size[0] - img.width) // 2,
                    (size[1] - img.height) // 2,
                )

                # Dán ảnh vào nền trắng
                new_img.paste(img, paste_position)

                # Lưu ảnh mới vào thư mục đầu ra
                output_path = os.path.join(output_folder, filename)
                new_img.save(output_path)

                print(f"Processed {filename}")


# Sử dụng hàm này với folder và kích thước mong muốn
resize_images_in_folder("anh_dang_ig", "result", size=(1000, 1000))
