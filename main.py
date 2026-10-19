import os
import subprocess

import ttkbootstrap as ttk
from tkinter import filedialog, messagebox
import tkinter as tk

def main():
    app = ttk.Window(title="Windows别名设置")
    folder_var = tk.StringVar(value="")
    ttk.Label(app, text="目录：").grid(row=0, column=0, padx=8, pady=4)
    ttk.Entry(app, width=50, textvariable=folder_var).grid(row=0, column=1, padx=4, pady=4)
    def select_folder_action():
        folder_path = filedialog.askdirectory(
            title="选择目录",
            initialdir=os.getcwd()
        )
        if folder_path:
            folder_var.set(folder_path)
    select_folder = ttk.Button(app, text="选择目录", bootstyle="warning", command=select_folder_action)
    select_folder.grid(row=0, column=2, padx=4, pady=4)
    alias_var = tk.StringVar(value="")
    ttk.Label(app, text="别名：").grid(row=1, column=0, padx=8, pady=4)
    ttk.Entry(app, width=50, textvariable=alias_var).grid(row=1, column=1, padx=4, pady=4)
    def set_alias_action():
        folder = folder_var.get()
        alias = alias_var.get()
        with open(os.path.join(folder, "desktop.ini"), 'w', encoding='gbk') as f:
            f.write("[.ShellClassInfo]\n")
            f.write(f"LocalizedResourceName={alias}")
        subprocess.run(["attrib", "+s", "+h", os.path.join(folder, "desktop.ini")])
        subprocess.run(["attrib", "+r", folder])
        messagebox.showinfo("成功", "文件夹别名设置成功")
    def remove_alias_action():
        folder = folder_var.get()
        os.remove(os.path.join(folder, "desktop.ini"))
        subprocess.run(["attrib", "-r", folder])
        messagebox.showinfo("成功", "文件夹别名移除成功")
    frame = ttk.Frame(app)
    frame.grid(row=2, column=1, padx=4, pady=8)
    ttk.Button(frame, text="设置别名", command=set_alias_action, bootstyle="success").grid(row=0, column=0, padx=8, pady=4)
    ttk.Button(frame, text="移除别名", command=remove_alias_action, bootstyle="danger").grid(row=0, column=1, padx=8, pady=4)
    app.mainloop()

if __name__ == "__main__":
    main()