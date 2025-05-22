import customtkinter as ctk
import os
from tkinter import filedialog, messagebox

class PGTIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("PGT IDE")
        self.root.geometry("800x600")
        
        # Настройка темы и внешнего вида
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Основной фрейм
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Текстовый редактор
        self.text_area = ctk.CTkTextbox(self.main_frame, wrap="none", font=("Courier New", 12))
        self.text_area.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Меню
        self.menu_bar = ctk.CTkFrame(self.main_frame, height=30)
        self.menu_bar.pack(fill="x", padx=5, pady=5)
        
        # Кнопки меню
        self.new_button = ctk.CTkButton(self.menu_bar, text="Новый", command=self.new_file)
        self.new_button.pack(side="left", padx=5)
        
        self.open_button = ctk.CTkButton(self.menu_bar, text="Открыть", command=self.open_file)
        self.open_button.pack(side="left", padx=5)
        
        self.save_button = ctk.CTkButton(self.menu_bar, text="Сохранить", command=self.save_file)
        self.save_button.pack(side="left", padx=5)
        
        self.run_button = ctk.CTkButton(self.menu_bar, text="Запустить", command=self.run_code)
        self.run_button.pack(side="left", padx=5)
        
        self.current_file = None
        
    def new_file(self):
        if messagebox.askyesno("Новый файл", "Сохранить текущий файл перед созданием нового?"):
            self.save_file()
        self.text_area.delete("1.0", "end")
        self.current_file = None
        
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PGT Files", "*.pgt")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.text_area.delete("1.0", "end")
                    self.text_area.insert("1.0", file.read())
                    self.current_file = file_path
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл: {str(e)}")
                
    def save_file(self):
        if not self.current_file:
            self.current_file = filedialog.asksaveasfilename(defaultextension=".pgt", filetypes=[("PGT Files", "*.pgt")])
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as file:
                    file.write(self.text_area.get("1.0", "end-1c"))
                messagebox.showinfo("Успех", "Файл успешно сохранен")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {str(e)}")
                
    def run_code(self):
        code = self.text_area.get("1.0", "end-1c")
        try:
            # Здесь можно добавить логику выполнения .pgt кода
            # Пока просто выводим код в консоль
            print("Выполняется код:")
            print(code)
            messagebox.showinfo("Выполнение", "Код успешно выполнен (вывод в консоли)")
        except Exception as e:
            messagebox.showerror("Ошибка выполнения", f"Ошибка: {str(e)}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = PGTIDE(root)
    root.mainloop()