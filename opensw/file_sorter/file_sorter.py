from pathlib import Path
import shutil

# 확장자별로 이동할 폴더와 확장자를 정리합니다.
CATEGORIES = {
    "이미지": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
    "문서": {".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".hwp"},
    "영상": {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"},
    "압축파일": {".zip", ".rar", ".7z", ".tar", ".gz"},
}


def get_category(extension):
    """확장자에 맞는 분류 이름을 반환합니다."""
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "기타"


def sort_files(folder_path):
    """선택한 폴더의 파일을 확장자에 따라 이동합니다."""
    folder = Path(folder_path)

    # 폴더가 없으면 안내하고 작업을 종료합니다.
    if not folder.is_dir():
        print("존재하지 않는 폴더입니다.")
        return

    # 바로 아래에 있는 파일만 분류합니다. (하위 폴더는 건드리지 않음)
    for file_path in folder.iterdir():
        if not file_path.is_file():
            continue

        category = get_category(file_path.suffix)
        destination_folder = folder / category

        # 분류 폴더가 없으면 자동으로 만듭니다.
        destination_folder.mkdir(exist_ok=True)
        destination = destination_folder / file_path.name

        # 같은 이름의 파일이 있으면 덮어쓰지 않고 번호를 붙입니다.
        number = 1
        while destination.exists():
            destination = destination_folder / f"{file_path.stem}_{number}{file_path.suffix}"
            number += 1

        shutil.move(str(file_path), str(destination))
        print(f"{file_path.name} -> {category} 폴더로 이동")


if __name__ == "__main__":
    # 정리할 폴더 경로를 입력받아 프로그램을 실행합니다.
    target_folder = input("정리할 폴더 경로를 입력하세요: ").strip()
    sort_files(target_folder)
