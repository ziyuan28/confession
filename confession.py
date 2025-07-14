import tkinter as tk
import random
import time

def show_love_message():
    """
    创建一个新的顶层窗口来显示表白信息。
    """
    # 创建一个新的窗口
    window = tk.Toplevel(root)
    window.title("给你的悄悄话")

    # 从列表中随机选择一句表白
    message = random.choice(love_messages)

    # 在窗口中添加标签来显示文字
    label = tk.Label(window, text=message, font=("Helvetica", 16), padx=20, pady=20)
    label.pack()

    # 获取屏幕的宽度和高度
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 随机生成窗口的坐标
    x = random.randint(0, screen_width - 200)
    y = random.randint(0, screen_height - 200)

    # 设置窗口的位置
    window.geometry(f"+{x}+{y}")

    # 设置一个定时器，在5秒后自动关闭这个小窗口
    window.after(5000, window.destroy)

def main_loop():
    """
    主循环，定时调用显示信息的函数。
    """
    show_love_message()
    # 设置下一次弹出的随机时间间隔（例如，10到30秒之间）
    next_popup_delay = random.randint(10, 30)
    root.after(next_popup_delay * 1000, main_loop)


# --- 程序主入口 ---

# 准备你的表白话语
love_messages = [
    "我喜欢你，不是一时兴起，是深思熟虑。",
    "遇见你，我才发现，原来春天可以这么美。",
    "我的世界，因为有你而精彩。",
    "我想和你一起，看遍世间所有风景。",
    "你的笑容，是我见过最美的风景。",
    "可以认识你，是我最大的幸运。",
    "你知道吗？我的心，早就被你偷走了。",
    "我想把我的全世界，都给你。",
]

# 创建一个主窗口
root = tk.Tk()
# 隐藏主窗口，让程序在后台运行
root.withdraw()

# 启动主循环
main_loop()

# 运行Tkinter事件循环
root.mainloop()