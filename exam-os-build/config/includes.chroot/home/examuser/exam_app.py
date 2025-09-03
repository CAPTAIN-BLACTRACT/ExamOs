import os
import tkinter as tk

# --- UI Definitions ---
def launch_student_ui(root):
    root.title("Exam Mode")
    root.attributes('-fullscreen', True)
    tk.Label(root, text="Student Exam Interface", font=("Helvetica", 24)).pack(pady=50)

def launch_admin_dashboard(root):
    root.title("Admin Dashboard")
    root.geometry("800x600")
    tk.Label(root, text="Welcome, Admin!", font=("Helvetica", 24)).pack(pady=50)
    tk.Button(root, text="Upload Question Paper").pack(pady=10)

# --- Main Application Logic ---
if __name__ == "__main__":
    try:
        current_user = os.getlogin()
    except OSError:
        import getpass
        current_user = getpass.getuser()

    app_window = tk.Tk()

    if current_user == "examuser":
        launch_student_ui(app_window)
    elif current_user == "admin":
        launch_admin_dashboard(app_window)
    else:
        app_window.destroy()
        print(f"Unauthorized user: {current_user}")
        exit()

    app_window.mainloop()
