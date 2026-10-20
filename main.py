import tkinter as tk

BG = "#10131c"
PANEL = "#191e2b"
ACCENT = "#8b5cf6"
TEXT = "#f1f5f9"
MUTED = "#8993a8"
GREEN = "#34d399"

root = tk.Tk()
root.title("TFM MENU 4K")
root.geometry("310x400")
root.resizable(False, False)
root.configure(bg=BG)
root.attributes("-topmost", True)

states = {}

header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=12, pady=12)

title = tk.Label(
    header,
    text="TFM / MENU 4K",
    font=("Arial", 15, "bold"),
    bg=BG,
    fg=TEXT
)
title.pack(side="left")

def minimize():
    root.iconify()

close_button = tk.Button(
    header,
    text="—",
    command=minimize,
    bg=PANEL,
    fg=TEXT,
    relief="flat",
    width=3
)
close_button.pack(side="right")

subtitle = tk.Label(
    root,
    text="TRANSFORMICE CONTROL PANEL",
    bg=BG,
    fg=MUTED,
    font=("Arial", 8)
)
subtitle.pack(pady=(0, 12))

body = tk.Frame(root, bg=BG)
body.pack(fill="both", expand=True, padx=14)

def toggle(name, button):
    states[name] = not states[name]

    if states[name]:
        button.config(
            text=f"{name}  ON",
            bg="#263d3b",
            fg=GREEN
        )
    else:
        button.config(
            text=f"{name}  OFF",
            bg=PANEL,
            fg=TEXT
        )

def add_button(name):
    states[name] = False

    button = tk.Button(
        body,
        text=f"{name}  OFF",
        command=lambda: toggle(name, button),
        bg=PANEL,
        fg=TEXT,
        activebackground=ACCENT,
        activeforeground="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        bd=0,
        anchor="w",
        padx=14,
        pady=10
    )
    button.pack(fill="x", pady=4)

add_button("Auto Win")
add_button("Gravity")
add_button("Collisionless")
add_button("Shaman Wings")

footer = tk.Label(
    root,
    text="TFM MENU 4K | UI PROTOTYPE",
    bg=BG,
    fg=MUTED,
    font=("Arial", 8)
)
footer.pack(pady=12)

root.mainloop()
