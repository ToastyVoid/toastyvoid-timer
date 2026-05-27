import tkinter as tk
from tkinter import messagebox
import time
import threading

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Qwasker's Timer")
        self.root.geometry("400x300")
        self.root.configure(bg="#2c3e50")

        # Title Label
        self.title_label = tk.Label(root, text="ToastyVoid's Timer", font=("Helvetica", 20, "bold"), fg="white", bg="#2c3e50")
        self.title_label.pack(pady=10)

        # Time selection frame
        time_frame = tk.Frame(root, bg="#2c3e50")
        time_frame.pack(pady=10)

        # Hours Spinbox
        tk.Label(time_frame, text="Hours", font=("Helvetica", 12), fg="white", bg="#2c3e50").grid(row=0, column=0, padx=5)
        self.hours_spin = tk.Spinbox(time_frame, from_=0, to=23, width=5, font=("Helvetica", 14))
        self.hours_spin.grid(row=1, column=0, padx=5)

        # Minutes Spinbox
        tk.Label(time_frame, text="Minutes", font=("Helvetica", 12), fg="white", bg="#2c3e50").grid(row=0, column=1, padx=5)
        self.minutes_spin = tk.Spinbox(time_frame, from_=0, to=59, width=5, font=("Helvetica", 14))
        self.minutes_spin.grid(row=1, column=1, padx=5)

        # Seconds Spinbox
        tk.Label(time_frame, text="Seconds", font=("Helvetica", 12), fg="white", bg="#2c3e50").grid(row=0, column=2, padx=5)
        self.seconds_spin = tk.Spinbox(time_frame, from_=0, to=59, width=5, font=("Helvetica", 14))
        self.seconds_spin.grid(row=1, column=2, padx=5)

        # Countdown Label
        self.countdown_label = tk.Label(root, text="", font=("Helvetica", 18, "bold"), fg="#f1c40f", bg="#2c3e50")
        self.countdown_label.pack(pady=20)

        # Start Button
        self.start_button = tk.Button(root, text="Start Timer", font=("Helvetica", 14, "bold"), bg="#27ae60", fg="white", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.title_label = tk.Label(root, text="Coded by Qwasker (a.k.a: ToastyVoid)", font=("Helvetica", 20, "bold"), fg="white", bg="#2c3e50")
        self.title_label = tk.Label(root, text="I'm known as Qwasker by people on Discord.", font=("Helvetica", 20, "bold"), fg="white", bg="#2c3e50")

    def start_timer(self):
        try:
            hours = int(self.hours_spin.get())
            minutes = int(self.minutes_spin.get())
            seconds = int(self.seconds_spin.get())
            total_time = hours * 3600 + minutes * 60 + seconds
            if total_time <= 0:
                messagebox.showerror("Invalid Time", "Please select a time greater than 0!")
                return
            threading.Thread(target=self.run_timer, args=(total_time,), daemon=True).start()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers!")

    def run_timer(self, total_time):
        for remaining in range(total_time, -1, -1):
            mins, secs = divmod(remaining, 60)
            hrs, mins = divmod(mins, 60)
            time_format = f"{hrs:02}:{mins:02}:{secs:02}"
            self.countdown_label.config(text=time_format)
            time.sleep(1)
        self.show_popup()

    def show_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Time's Up!")
        popup.geometry("300x150")
        popup.configure(bg="#c0392b")
        popup.attributes("-topmost", True)  # Force window to stay on top
        popup.lift()
        popup.focus_force()

        label = tk.Label(popup, text="⏰ Your timer has finished!", font=("Helvetica", 14, "bold"), fg="white", bg="#c0392b")
        label.pack(expand=True)

        ok_button = tk.Button(popup, text="OK", font=("Helvetica", 12, "bold"), bg="white", fg="#c0392b", command=popup.destroy)
        ok_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
