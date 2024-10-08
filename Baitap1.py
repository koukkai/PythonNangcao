import tkinter as tk
from tkinter import ttk
from datetime import datetime
import calendar

class DaysLivedCalculator:
    def __init__(self, master):
        self.master = master
        master.title("RIZZ MÈO")
        master.geometry("450x400")
        master.configure(bg='#E6E6FA')  # Lavender background

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#E6E6FA')
        self.style.configure('TLabel', background='#E6E6FA', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12, 'bold'))

        self.frame = ttk.Frame(master, padding="20")
        self.frame.pack(expand=True, fill="both")

        self.title_label = ttk.Label(self.frame, text="TÍNH SỐ NGÀY BẠN SỐNG", 
                                     font=("Arial", 18, "bold"), foreground='#4B0082')  # Indigo color
        self.title_label.pack(pady=20)

        self.date_frame = ttk.Frame(self.frame)
        self.date_frame.pack(pady=10)

        # Date inputs
        self.day_var = tk.StringVar()
        self.month_var = tk.StringVar()
        self.year_var = tk.StringVar()

        self.day_label = ttk.Label(self.date_frame, text="Ngày:")
        self.day_label.grid(row=0, column=0, padx=5, pady=5)
        self.day_combobox = ttk.Combobox(self.date_frame, width=3, textvariable=self.day_var, 
                                         values=[str(i).zfill(2) for i in range(1, 32)])
        self.day_combobox.grid(row=0, column=1, padx=5, pady=5)

        self.month_label = ttk.Label(self.date_frame, text="Tháng:")
        self.month_label.grid(row=0, column=2, padx=5, pady=5)
        self.month_combobox = ttk.Combobox(self.date_frame, width=3, textvariable=self.month_var,
                                           values=[str(i).zfill(2) for i in range(1, 13)])
        self.month_combobox.grid(row=0, column=3, padx=5, pady=5)

        self.year_label = ttk.Label(self.date_frame, text="Năm:")
        self.year_label.grid(row=0, column=4, padx=5, pady=5)
        self.year_entry = ttk.Entry(self.date_frame, width=6, textvariable=self.year_var)
        self.year_entry.grid(row=0, column=5, padx=5, pady=5)

        self.calculate_button = ttk.Button(self.frame, text="Tính toán", command=self.calculate_days, 
                                           style='Accent.TButton')
        self.style.configure('Accent.TButton', background='#4B0082', foreground='white')
        self.calculate_button.pack(pady=20)

        self.result_frame = ttk.Frame(self.frame, style='Result.TFrame')
        self.result_frame.pack(pady=10, fill='x')
        self.style.configure('Result.TFrame', background='#D8BFD8')  # Thistle color

        self.result_label = ttk.Label(self.result_frame, text="", font=("Arial", 14, "bold"), 
                                      foreground='#4B0082', background='#D8BFD8')
        self.result_label.pack(pady=10)

    def calculate_days(self):
        try:
            day = int(self.day_var.get())
            month = int(self.month_var.get())
            year = int(self.year_var.get())
            
            # Validate date
            if not self.is_valid_date(year, month, day):
                raise ValueError("Ngày không hợp lệ")

            birth_date = datetime(year, month, day)
            today = datetime.now()
            days_lived = (today - birth_date).days
            self.result_label.config(text=f"Bạn đã sống được {days_lived:,} ngày!")
        except ValueError as e:
            self.result_label.config(text=f"Lỗi: {str(e)}")

    def is_valid_date(self, year, month, day):
        try:
            datetime(year, month, day)
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    calculator = DaysLivedCalculator(root)
    root.mainloop()
