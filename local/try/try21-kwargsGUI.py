import tkinter as tk

def check_passed(**scores):
  math = scores.get('math')
  physics = scores.get('physics')
  english = scores.get('english')

  text = ''
  if math is not None and math >= 50:
    text += 'สอบผ่านคณิต\n'
  if physics is not None and physics >= 50:
    text += 'สอบผ่านฟิสิกส์\n'
  if english is not None and english >= 50:
    text += 'สอบผ่านอังกฤษ\n'

  return text

def show_passed():
  output_text = check_passed(
    math=int(entry1.get()),
    physics=int(entry2.get()),
    english=int(entry3.get())
  )
  output_label.configure(text=output_text)

window = tk.Tk()
window.title('ผ่านอันไหนมั่งอ่ะ')
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

go_button = tk.Button(master=window, text='ตรวจสอบวิชาที่ผ่าน', command=show_passed)
go_button.pack(pady=(15, 0), ipadx=5, ipady=5)

output_label = tk.Label(master=window)
output_label.pack(pady=15)

window.mainloop()