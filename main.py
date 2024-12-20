import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageTk


class CustomOverlayWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("block")

        # 设置窗口的初始大小和背景颜色
        self.root.geometry("400x300")
        self.root.config(bg="pink")
        self.is_pinned = True  # 默认置顶状态

        # 顶部按钮栏
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.X, pady=5)

        # 设置置顶按钮
        self.pin_button = tk.Button(button_frame, text="置顶", command=self.toggle_pin)
        self.pin_button.pack(side=tk.LEFT, padx=5)

        # 设置颜色选择按钮
        color_button = tk.Button(button_frame, text="选择颜色", command=self.change_color)
        color_button.pack(side=tk.LEFT, padx=5)

        # 设置图片导入按钮
        image_button = tk.Button(button_frame, text="导入图片", command=self.load_image)
        image_button.pack(side=tk.LEFT, padx=5)

        # 关于按钮
        about_button = tk.Button(button_frame, text="关于", command=self.show_about)
        about_button.pack(side=tk.LEFT, padx=5)

        # 默认背景图片为空
        self.background_image = None
        self.canvas = tk.Canvas(self.root, bg="pink")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def toggle_pin(self):
        self.is_pinned = not self.is_pinned
        self.root.attributes("-topmost", self.is_pinned)
        self.pin_button.config(text="取消置顶" if self.is_pinned else "置顶")

    def change_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.root.config(bg=color)
            self.canvas.config(bg=color)
            self.background_image = None  # 移除当前背景图片

    def load_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("图片文件", "*.jpg;*.png;*.gif")])
        if image_path:
            img = Image.open(image_path)
            img = img.resize((self.root.winfo_width(), self.root.winfo_height()), Image.Resampling.LANCZOS)
            self.background_image = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

    def show_about(self):
        messagebox.showinfo("关于", "欢迎使用 block\nDesign by sakura\n博客：sakurablogs.top")


# 主程序入口
if __name__ == "__main__":
    root = tk.Tk()
    app = CustomOverlayWindow(root)
    root.mainloop()
