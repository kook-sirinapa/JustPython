import tkinter as tk

def average(*scores):
  sum_score = sum(scores)
  average_score = sum_score / len(scores)
  return average_score

def show_average():
  average_score = average(
    int(entry1.get()), 
    int(entry2.get()), 
    int(entry3.get())
  )
  output_text = 'คะแนนเฉลี่ย = ' + str(average_score)
  output_label.configure(text=output_text)

window = tk.Tk()
window.title('คะแนนเฉลี่ยเท่ห์ๆ')
window.minsize(width=400, height=400)

label1 = tk.Label(master=window, text='คณิต')
label1.pack(pady=(10, 0))

entry1 = tk.Entry(master=window, bg='#F6F6F6')
entry1.pack(pady=(10, 0))

label2 = tk.Label(master=window, text='ฟิสิกส์')
label2.pack(pady=(10, 0))

entry2 = tk.Entry(master=window, bg='#F6F6F6')
entry2.pack(pady=(10, 0))

label3 = tk.Label(master=window, text='อังกฤษ')
label3.pack(pady=(10, 0))

entry3 = tk.Entry(master=window, bg='#F6F6F6')
entry3.pack(pady=(10, 0))

go_button = tk.Button(master=window, text='คำนวณคะแนนเฉลี่ย', command=show_average)
go_button.pack(pady=(15, 0), ipadx=5, ipady=5)

output_label = tk.Label(master=window)
output_label.pack(pady=15)

window.mainloop()