import os
import shutil

# Cấu hình thư mục cần dọn dẹp ('.' nghĩa là thư mục hiện tại chứa file code này)
SOURCE_DIR = '.'

# Từ điển phân loại file dựa trên phần mở rộng (đuôi file)
CATEGORIES = {
    'Music': ['.mp3', '.wav', '.flac', '.ogg'],
    'Code': ['.py', '.html', '.css', '.js'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.csv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz']
}

def organize_files(source_path):
    # Lấy danh sách tất cả các file trong thư mục
    for filename in os.listdir(source_path):
        file_path = os.path.join(source_path, filename)
        
        # Bỏ qua nếu nó là thư mục, không phải file
        if os.path.isdir(file_path):
            continue
            
        # Bỏ qua chính file code đang chạy và các file hệ thống bị ẩn
        if filename == 'main.py' or filename == 'README.md' or filename.startswith('.'):
            continue

        # Lấy đuôi file và chuyển thành chữ thường
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False
        
        # Duyệt qua từng danh mục để kiểm tra đuôi file
        for category, extensions in CATEGORIES.items():
            if file_ext in extensions:
                dest_dir = os.path.join(source_path, category)
                
                # Tạo thư mục nếu chưa có
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                    
                # Di chuyển file vào đúng thư mục
                shutil.move(file_path, os.path.join(dest_dir, filename))
                print(f"✅ Đã chuyển: {filename} -> {category}/")
                moved = True
                break
        
        # Nếu đuôi file không nằm trong danh sách trên, đưa vào thư mục 'Others'
        if not moved:
            other_dir = os.path.join(source_path, 'Others')
            if not os.path.exists(other_dir):
                os.makedirs(other_dir)
            shutil.move(file_path, os.path.join(other_dir, filename))
            print(f"📦 Đã chuyển: {filename} -> Others/")

if __name__ == "__main__":
    print("🚀 Bắt đầu dọn dẹp thư mục...")
    organize_files(SOURCE_DIR)
    print("✨ Hoàn tất!")
