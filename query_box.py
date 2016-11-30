import Tkinter as tk
import os

class query_box:
	def __init__(self, parent):
		self.parent = parent
		self.frame = tk.Frame(self.parent)

		self.select_str = tk.StringVar()
		self.select_box = tk.Entry(self.frame, textvariable = self.select_str, width = 50, font = "Times\ New\ Roman 20")
		self.select_box.pack(pady = 8)
		self.select_str.set("Select What?")

		self.table_str = tk.StringVar()
		self.table_box = tk.Entry(self.frame, textvariable = self.table_str, width = 50, font = "Times\ New\ Roman 20")
		self.table_box.pack(pady = 8)
		self.table_str.set("From which table(s)")

		self.where_str = tk.StringVar()
		self.where_box = tk.Entry(self.frame, textvariable = self.where_str, width = 50, font = "Times\ New\ Roman 20")
		self.where_box.pack(pady = 8)
		self.where_str.set("Any Condition? <If no conditions, then put '1'>")

		self.button = tk.Button(self.frame, text = "Query", command = self.query, bg = "black", fg = "white").pack(pady = 5)

		self.frame.pack()

	def query(self):
		fil = open("temp.txt", "w")
		sel = self.select_box.get()+"\n"
		tab = self.table_box.get()+"\n"
		whe = self.where_box.get()

		fil.write(sel)
		fil.write(tab)
		fil.write(whe)
		
		fil.close()
		
		os.system("python table.py")

if __name__ == "__main__":
	root = tk.Tk()
	app = query_box(root)
	root.mainloop()