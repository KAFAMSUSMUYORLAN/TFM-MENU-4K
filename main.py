import tkinter as tk
import time
from pynput import keyboard

MAX_TIME = 15.0

root = tk.Tk()
root.title("X-4K")
root.geometry("280x160")
root.attributes("-topmost", True)
root.resizable(False, False)

running = False
m_held = False
start_time = 0.0


tk.Label(
    root,
    text="X-4K",
    font=("Arial", 22, "bold")
).pack(pady=(12, 5))

timer_label = tk.Label(
    root,
    text="0.0 / 15.0 s",
    font=("Arial", 14)
)
timer_label.pack(pady=4)

status_label = tk.Label(
    root,
    text="READY",
    font=("Arial", 10)
)
status_label.pack(pady=4)


def start_timer():
    global running, start_time

    if running:
        return

    running = True
    start_time = time.monotonic()
    status_label.config(text="ACTIVE")
    update_timer()


def stop_timer():
    global running

    running = False
    status_label.config(text="READY")


def update_timer():
    if not running:
        return

    elapsed = time.monotonic() - start_time

    if elapsed >= MAX_TIME:
        timer_label.config(text="15.0 / 15.0 s")
        stop_timer()
        return

    timer_label.config(
        text=f"{elapsed:.1f} / {MAX_TIME:.1f} s"
    )

    root.after(50, update_timer)


def on_press(key):
    global m_held

    try:
        if key.char and key.char.lower() == "m":
            if not m_held:
                m_held = True
                root.after(0, start_timer)
    except AttributeError:
        pass


def on_release(key):
    global m_held

    try:
        if key.char and key.char.lower() == "m":
            m_held = False
            root.after(0, stop_timer)
    except AttributeError:
        pass


def close_app():
    listener.stop()
    root.destroy()


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)
listener.start()

root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()
