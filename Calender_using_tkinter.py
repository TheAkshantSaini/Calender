from tkinter import *
import calendar

def showCalendar(event):
    year_str = year_field.get()
    if year_str.isdigit():
        year = int(year_str)
        if 1 <= year <= 9999:
            cal_content = calendar.TextCalendar().formatyear(year)
            cal_display.config(state="normal")
            cal_display.delete(1.0, END)
            cal_display.insert(INSERT, cal_content)
            cal_display.config(state="disabled")
        else:
            cal_display.config(state="normal")
            cal_display.delete(1.0, END)
            cal_display.insert(INSERT, "Please enter a valid year (1-9999).")
            cal_display.config(state="disabled")
    else:
        cal_display.config(state="normal")
        cal_display.delete(1.0, END)
        cal_display.insert(INSERT, "Invalid input. Please enter a valid year.")
        cal_display.config(state="disabled")

if __name__ == '__main__':
    new = Tk()
    new.config(background='black')
    new.title("Calendar")
    new.geometry("800x600+150+100")

    cal_label = Label(new, text="Enter the year to get the calendar", bg='black',
                      font=("Arial", 28, "bold"), relief='sunken', bd=5, fg='white')
    cal_label.pack(pady=20)

    year_label = Label(new, text="Enter Year", bg='black', bd=5, relief='solid',
                       fg='white', font=('Arial', 20, 'bold'))
    year_label.pack()

    year_field = Entry(new, width=10, font=('Arial', 16))
    year_field.pack()

    year_field.bind("<KeyRelease>", showCalendar)  # Automatically generate calendar on key release

    cal_display = Text(new, wrap=NONE, font=('Courier', 12), bg='black', fg='white')
    cal_display.config(state="disabled")
    cal_display.pack(fill=BOTH, expand=True)

    new.mainloop()
