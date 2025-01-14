import os
import pyheif
from PIL import Image

def convert_all_heic_to_jpeg(input_dir, output_dir):
    # 確保輸出目錄存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 遍歷輸入目錄中的所有 .HEIC 檔案
    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(".HEIC"):
            input_path = os.path.join(input_dir, file_name)
            base_name = os.path.splitext(file_name)[0]
            output_path = os.path.join(output_dir, f"{base_name}.jpeg")
            
            try:
                # 解碼 HEIC 並轉換為 JPEG
                heif_file = pyheif.read(input_path)
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw",
                    heif_file.mode,
                    heif_file.stride,
                )
                
                # 儲存 JPEG 檔案
                image.save(output_path, "JPEG")
                print(f"Converted: {input_path} -> {output_path}")
            except Exception as e:
                print(f"Failed to convert {input_path}: {e}")

# 指定輸入與輸出目錄
input_directory = "path/to/input_directory"  # 替換為包含 HEIC 檔案的目錄
output_directory = "path/to/output_directory"  # 替換為要儲存輸出的目錄

# 執行批次轉換
convert_all_heic_to_jpeg(input_directory, output_directory)