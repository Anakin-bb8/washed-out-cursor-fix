import winreg
import os
from tkinter import messagebox
import ctypes

def fix_cursor():
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    try:
        # Open the registry key
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Mouse", 0, winreg.KEY_SET_VALUE)
        
        # Set the value of MouseTrails to -1
        winreg.SetValueEx(reg_key, "MouseTrails", 0, winreg.REG_SZ, "-1")
        
        # Close the registry key
        winreg.CloseKey(reg_key)
        
        # Display a message box
        disconnect = messagebox.askyesno("Success", "The fix was applied successfully.\nDo you want to disconnect from your computer to apply the changes?")

        if disconnect:
            os.system("shutdown /l")
        else:
            messagebox.showinfo("Info", "The changes will be applied at the next login.")
        
    except Exception as e:
        print(f"An error as occurred: {e}")

# execute
if __name__ == "__main__":
    fix_cursor()