import tkinter as tk

root = tk.Tk()
root.title("TfmMenu")
root.geometry("280x230")
root.configure(bg="#151515")
root.resizable(False, False)

root.attributes("-topmost", True)

title = tk.Label(
    root,
    text="TfmMenu",
    bg="#151515",
    fg="white",
    font=("Arial", 15, "bold")
)
title.pack(pady=15)

tk.Label(
    root,
    text="Transformice Menu",
    bg="#151515",
    fg="#999999"
).pack()

def toggle():
    if root.state() == "withdrawn":
        root.deiconify()
    else:
        root.withdraw()

tk.Button(
    root,
    text="Gizle",
    command=toggle,
    bg="#303030",
    fg="white"
).pack(pady=15)

tk.Label(
    root,
    text="INSERT: Açma/kapatma sonraki aşamada",
    bg="#151515",
    fg="#777777",
    font=("Arial", 8)
).pack()

root.mainloop()
