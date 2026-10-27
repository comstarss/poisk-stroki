

import tkinter as tk
from tkinter import messagebox, scrolledtext
import re


class StringSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Поиск вхождения строки в тексте")
        self.root.geometry("700x550")
        self.root.resizable(True, True)

        # Заголовок
        title_label = tk.Label(
            root,
            text="Поиск слов, содержащих заданную подстроку",
            font=("Times New Roman", 14, "bold")
        )
        title_label.pack(pady=10)

        # Поле для ввода текста
        tk.Label(root, text="Введите текст:", font=("Times New Roman", 12)).pack(anchor="w", padx=20)
        self.text_input = scrolledtext.ScrolledText(
            root, height=8, width=70, font=("Times New Roman", 12), wrap=tk.WORD
        )
        self.text_input.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

        # Поле для ввода искомой строки
        tk.Label(root, text="Введите искомую строку (подстроку):", font=("Times New Roman", 12)).pack(anchor="w", padx=20)
        self.search_entry = tk.Entry(root, width=70, font=("Times New Roman", 12))
        self.search_entry.pack(padx=20, pady=5)

        # Кнопка поиска
        search_btn = tk.Button(
            root,
            text="Найти",
            command=self.search,
            font=("Times New Roman", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=15
        )
        search_btn.pack(pady=10)

        # Поле результатов
        tk.Label(root, text="Результаты поиска:", font=("Times New Roman", 12)).pack(anchor="w", padx=20)
        self.result_text = scrolledtext.ScrolledText(
            root, height=8, width=70, font=("Times New Roman", 12), wrap=tk.WORD, state=tk.DISABLED
        )
        self.result_text.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

        # Кнопка очистки
        clear_btn = tk.Button(
            root,
            text="Очистить",
            command=self.clear_all,
            font=("Times New Roman", 12),
            width=15
        )
        clear_btn.pack(pady=5)

    def search(self):
        """Выполнение поиска с обработкой ошибок"""
        text = self.text_input.get("1.0", tk.END).strip()
        search_str = self.search_entry.get().strip()

        # Очистка предыдущих результатов
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)

        # Проверка на пустой ввод
        if not text:
            messagebox.showerror("Ошибка ввода", "Текст не может быть пустым!\nВведите текст для поиска.")
            self.result_text.insert(tk.END, "Ошибка: текст не введён.\n")
            self.result_text.config(state=tk.DISABLED)
            return

        if not search_str:
            messagebox.showerror("Ошибка ввода", "Искомая строка не может быть пустой!\nВведите подстроку для поиска.")
            self.result_text.insert(tk.END, "Ошибка: искомая строка не введена.\n")
            self.result_text.config(state=tk.DISABLED)
            return

        # Разбиение текста на слова (учитываем знаки препинания)
        # Используем регулярное выражение для извлечения слов
        words = re.findall(r'\b\w+\b', text, flags=re.UNICODE)

        if not words:
            messagebox.showwarning("Предупреждение", "В тексте не найдено ни одного слова.")
            self.result_text.insert(tk.END, "В тексте не найдено слов.\n")
            self.result_text.config(state=tk.DISABLED)
            return

        # Поиск слов, содержащих искомую подстроку (без учёта регистра)
        found_words = []
        search_lower = search_str.lower()

        for word in words:
            if search_lower in word.lower():
                if word not in found_words:  # уникальные слова
                    found_words.append(word)

        # Вывод результатов
        if found_words:
            result_msg = f"Найдено слов, содержащих «{search_str}»: {len(found_words)}\n\n"
            result_msg += "Список слов:\n"
            for i, word in enumerate(found_words, 1):
                result_msg += f"{i}. {word}\n"
            self.result_text.insert(tk.END, result_msg)
            messagebox.showinfo("Результат поиска", f"Найдено {len(found_words)} слов(а), содержащих «{search_str}».")
        else:
            self.result_text.insert(tk.END, f"Строка «{search_str}» не найдена ни в одном слове текста.\n")
            messagebox.showinfo("Результат поиска", f"Строка «{search_str}» не найдена в тексте.")

        self.result_text.config(state=tk.DISABLED)

    def clear_all(self):
        """Очистка всех полей"""
        self.text_input.delete("1.0", tk.END)
        self.search_entry.delete(0, tk.END)
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = StringSearchApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
