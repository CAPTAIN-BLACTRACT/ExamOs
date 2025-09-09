import tkinter as tk
import os

def launch_student_ui(root):
    """Sets up the UI for the student."""
    root.title("ExamOS - Student Mode")
    root.attributes('-fullscreen', True)
    # Potentially add a cursor hide command: root.config(cursor="none")
    
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True)
    
    tk.Label(main_frame, text="Exam Kiosk is Active", font=("Helvetica", 36)).pack(pady=100)
    
    # Example exit button for testing. In production, this would be removed.
    exit_button = tk.Button(main_frame, text="Exit (for testing)", command=root.destroy)
    exit_button.pack(pady=20)

if __name__ == "__main__":
    app_window = tk.Tk()
    
    # In a real scenario, you might have logic here to check the user
    # but for the live user, we can assume it's always the student.
    launch_student_ui(app_window)
    
    app_window.mainloop()

