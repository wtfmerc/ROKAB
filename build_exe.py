## EVERYTHING HERE WAS MADE IN CURSOR AI ##

import os
import subprocess
import sys

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("PyInstaller is already installed.")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller installed successfully.")

def build_executable():
    """Build the standalone executable"""
    print("Building standalone executable...")
    
    # Clean up any previous builds
    if os.path.exists("dist"):
        import shutil
        shutil.rmtree("dist")
    if os.path.exists("build"):
        import shutil
        shutil.rmtree("build")
    if os.path.exists("ROKAnswerBot.spec"):
        os.remove("ROKAnswerBot.spec")
    
    # Use python -m pyinstaller with more comprehensive options
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",  # Create a single executable file
        "--console",  # Show console window for debugging
        "--name=ROKAnswerBot",  # Name of the executable
        "--collect-all=selenium",
        "--collect-all=undetected_chromedriver",
        "--collect-all=pyperclip",
        "--collect-all=pyautogui",
        "--hidden-import=selenium",
        "--hidden-import=undetected_chromedriver",
        "--hidden-import=pyperclip",
        "--hidden-import=pyautogui",
        "--hidden-import=tkinter",
        "--hidden-import=threading",
        "--hidden-import=time",
        "--hidden-import=os",
        "--hidden-import=pickle",
        "--hidden-import=subprocess",
        "--hidden-import=sys",
        "main.py"
    ]
    
    # Add cookies file if it exists
    if os.path.exists("chatgpt_cookies.pkl"):
        cmd.insert(-1, "--add-data=chatgpt_cookies.pkl;.")
    
    try:
        print(f"Running command: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("\n✅ Build completed successfully!")
            print("📁 Executable created in: dist/ROKAnswerBot.exe")
            print("\n📋 Instructions:")
            print("1. Run ROKAnswerBot.exe from the dist folder")
            print("2. The first time you run it, it will download Chrome driver automatically")
            print("3. Login to ChatGPT when the browser opens")
            print("4. Copy text to clipboard to send questions to ChatGPT")
            print("5. Close the executable when done")
            return True
        else:
            print(f"❌ Build failed!")
            print(f"Error output: {result.stderr}")
            return False
        
    except Exception as e:
        print(f"❌ Build failed with error: {e}")
        return False

def main():
    print("🚀 ROKAnswerBot Executable Builder")
    print("=" * 40)
    
    # Check if main.py exists
    if not os.path.exists("main.py"):
        print("❌ Error: main.py not found in current directory")
        return
    
    # Install PyInstaller
    install_pyinstaller()
    
    # Build the executable
    if build_executable():
        print("\n🎉 Your standalone executable is ready!")
    else:
        print("\n💥 Failed to create executable. Please check the error messages above.")

if __name__ == "__main__":
    main()
