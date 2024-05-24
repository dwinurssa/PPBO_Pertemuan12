import tkinter as tk

def tambah_teks():
    teks = entry.get()
    text_box.insert(tk.END, teks + "\n")

root = tk.Tk()
root.title("Program Tulisan Sederhana")

frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame, text="Masukkan teks:")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

button = tk.Button(frame, text="Tambahkan", command=tambah_teks)
button.grid(row=0, column=2)

canvas = tk.Canvas(root, width=200, height=100, bg='White')
canvas.pack(pady=10)

text_box = tk.Text(root, height=5, width=30)
text_box.pack(padx=10, pady=10)

root.mainloop()
