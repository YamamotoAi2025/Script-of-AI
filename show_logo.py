import tkinter as tk
from PIL import Image, ImageTk

# 画像ファイルのパス
LOGO_PATH = "https://github.com/YamamotoAi2025/Script-of-AI/blob/main/file_00000000ec8861f7bf20daa1fce08f09.png"  # logo.pngを置いた場所

def main():
    root = tk.Tk()
    root.title("πAI Boot")
    root.attributes("-fullscreen", True)  # 全画面表示
    root.configure(bg="black")

    # 画像読み込み
    img = Image.open(LOGO_PATH)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    img = img.resize((screen_width, screen_height))
    tk_img = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=tk_img, bg="black")
    label.pack(expand=True)

    # 数秒後に閉じる（例: 5秒）
    root.after(5000, root.destroy)
    root.mainloop()

if __name__ == "__main__":
    main()
