#copy
#this file copies from stdout
#clone of pipe in windows

import sys
import subprocess
import platform

def copy_to_clipboard(input_text):
    try:
        os_name = platform.system()
        if os_name == "Windows":
            process = subprocess.Popen('clip', stdin=subprocess.PIPE)
        elif os_name == 'Darwin':
            process = subprocess.Popen('pbcopy', stdin=subprocess.PIPE)
        elif os_name == "Linux":
            process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
        process.communicate(input_text.encode())
    except Exception as e:
        print("error: ", e)

if __name__ == "__main__":
    input_text = sys.stdin.read()
    copy_to_clipboard(input_text)

        
        
