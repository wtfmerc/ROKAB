##EVERYTHING HERE WAS CREATED WITH CURSOR AI##

import time
import pickle
import os
import threading
import pyperclip
import pyautogui
import tkinter as tk
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver as uc

# --- CONFIG ---
AUTO_SEND = True
COOKIES_FILE = "chatgpt_cookies.pkl"
CHATGPT_URL = "https://chatgpt.com"

# --- GUI POPUP ---
class ResponsePopup:
    def __init__(self):
        self.current_popup = None
    
    def show_response(self, service_name, response_text, response_time=None):
        try:
            # Destroy any existing popup first
            if self.current_popup and self.current_popup.winfo_exists():
                self.current_popup.destroy()
            
            mouse_x, mouse_y = pyautogui.position()
            self.current_popup = tk.Toplevel()
            popup = self.current_popup
            popup.title(f"{service_name} Response")
            popup.geometry("300x200")
            popup.configure(bg='#2b2b2b')
            popup.attributes('-topmost', True)
            popup.attributes('-alpha', 0.7)
            popup.overrideredirect(True)

            border_frame = tk.Frame(popup, bg='#4a9eff', bd=2, relief=tk.SOLID)
            border_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

            content_frame = tk.Frame(border_frame, bg='#2b2b2b')
            content_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

            title_frame = tk.Frame(content_frame, bg='#2b2b2b')
            title_frame.pack(fill=tk.X, pady=(0, 5))

            # Create title with response time if provided
            title_text = f"{service_name} Response"
            if response_time:
                title_text += f" ({response_time})"
            
            title_label = tk.Label(title_frame,
                                   text=title_text,
                                   bg='#2b2b2b',
                                   fg='#00ff00',
                                   font=('Arial', 10, 'bold'))
            title_label.pack(side=tk.LEFT)

            close_btn = tk.Button(title_frame,
                                  text="✕",
                                  command=self.close_popup,
                                  bg='#ff4444',
                                  fg='white',
                                  font=('Arial', 8, 'bold'),
                                  relief=tk.FLAT,
                                  borderwidth=0,
                                  width=2,
                                  height=1)
            close_btn.pack(side=tk.RIGHT)

            display_text = response_text[:200] + "..." if len(response_text) > 200 else response_text

            text_widget = tk.Text(content_frame,
                                  bg='#2b2b2b',
                                  fg='#00ff00',
                                  font=('Arial', 9),
                                  wrap=tk.WORD,
                                  relief=tk.FLAT,
                                  borderwidth=0,
                                  height=8,
                                  state=tk.DISABLED)
            text_widget.pack(fill=tk.BOTH, expand=True)
            text_widget.config(state=tk.NORMAL)
            text_widget.insert(tk.END, display_text)
            text_widget.config(state=tk.DISABLED)

            window_x = mouse_x + 15
            window_y = mouse_y - 100
            screen_width = popup.winfo_screenwidth()
            screen_height = popup.winfo_screenheight()

            if window_x + 300 > screen_width:
                window_x = mouse_x - 315
            if window_y < 0:
                window_y = 10
            if window_y + 200 > screen_height:
                window_y = screen_height - 210

            popup.geometry(f"300x200+{window_x}+{window_y}")
            popup.after(15000, self.close_popup)
            
            # Handle window close event
            popup.protocol("WM_DELETE_WINDOW", self.close_popup)

        except Exception as e:
            print(f"Error showing response popup: {e}")
    
    def close_popup(self):
        """Safely close the current popup and reset the reference"""
        try:
            if self.current_popup and self.current_popup.winfo_exists():
                self.current_popup.destroy()
        except Exception as e:
            print(f"Error closing popup: {e}")
        finally:
            self.current_popup = None

# --- MAIN BOT ---
class ChatGPTBot:
    def __init__(self):
        self.driver = None
        self.last_clipboard = pyperclip.paste()
        self.last_response = None
        self.response_popup = ResponsePopup()

    def setup_browser(self):
        print("Launching browser...")
        self.driver = uc.Chrome()
        self.driver.get(CHATGPT_URL)

        # Try cookies
        if self.load_cookies():
            print("Reloading page with cookies...")
            self.driver.refresh()
            time.sleep(3)

        if not self.is_logged_in():
            print("Please login manually...")
            self.wait_for_login()
            self.save_cookies()

        print("Ready!")

    def save_cookies(self):
        cookies = self.driver.get_cookies()
        with open(COOKIES_FILE, "wb") as f:
            pickle.dump(cookies, f)
        print("Cookies saved.")

    def load_cookies(self):
        if not os.path.exists(COOKIES_FILE):
            return False
        with open(COOKIES_FILE, "rb") as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            try:
                self.driver.add_cookie(cookie)
            except:
                pass
        print("Cookies loaded.")
        return True

    def is_logged_in(self):
        """Check if user is logged in by looking for the absence of the 'Log in' button"""
        try:
            # Check if we're on the main ChatGPT page
            current_url = self.driver.current_url
            if not current_url.startswith("https://chatgpt.com"):
                return False
            
            # Allow for trailing slash variations
            if current_url not in ["https://chatgpt.com", "https://chatgpt.com/"]:
                return False
            
            # Look for the "Log in" button - if it exists, user is not logged in
            try:
                login_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div/div/header/div[3]/div/div/div/button[1]/div")
                button_text = login_button.text.strip().lower()
                if "log in" in button_text:
                    return False
                else:
                    pass  # Button found but text is different, check other indicators
            except NoSuchElementException:
                return True
            
            # Fallback: also check for chat input elements
            try:
                chat_input = self.driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true'][id='prompt-textarea']")
                if chat_input.is_displayed() and chat_input.is_enabled():
                    return True
            except NoSuchElementException:
                pass
            
            return False
        except Exception as e:
            print(f"Error checking login status: {e}")
            return False

    def wait_for_login(self, timeout=300):
        """Wait for login by monitoring the disappearance of the 'Log in' button"""
        print("Please log in to ChatGPT. The bot will detect when you're logged in.")
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                # Check if we're on the main ChatGPT page
                current_url = self.driver.current_url
                if not current_url.startswith("https://chatgpt.com"):
                    time.sleep(2)
                    continue
                
                # Allow for trailing slash variations
                if current_url not in ["https://chatgpt.com", "https://chatgpt.com/"]:
                    time.sleep(2)
                    continue
                
                # Check if the "Log in" button is gone
                try:
                    login_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div/div/header/div[3]/div/div/div/button[1]/div")
                    button_text = login_button.text.strip().lower()
                    if "log in" in button_text:
                        time.sleep(2)
                        continue
                except NoSuchElementException:
                    print("Login detected!")
                    return
                
            except Exception as e:
                time.sleep(2)
        
        print("Login timeout - please check if you're logged in manually")

    def paste_to_chat(self, text):
        try:
            # 🔧 Define your custom prefix/suffix here (or make them class attributes)
            custom_prefix = "ONLY ANSWER WITH THE ANSWER, DONT GIVE ME ANYMORE INFORMATION, ONLY DO THE BARE MINIMUM(plus the full answer).Search online for the answer, remember this question is from the game Rise Of Kingdoms: "
            custom_suffix = ""

            # Combine everything
            final_text = f"{custom_prefix}{text}{custom_suffix}"

            chat_input = self.driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true'][id='prompt-textarea']")
            chat_input.click()
            time.sleep(0.1)

            # Clear and insert text
            self.driver.execute_script("arguments[0].innerHTML = '';", chat_input)
            self.driver.execute_script("arguments[0].textContent = arguments[1];", chat_input, final_text)

            if AUTO_SEND:
                chat_input.send_keys(Keys.RETURN)
                print("Message sent!")
        except Exception as e:
            print(f"Error pasting to chat: {e}")

    def get_response_count(self):
        """Get the current number of assistant responses"""
        elements = []
        
        # First try the new structure
        elements = self.driver.find_elements(By.CSS_SELECTOR, "article[data-turn='assistant'] div[data-message-author-role='assistant']")
        
        # If not found, try the old structure
        if not elements:
            elements = self.driver.find_elements(By.CSS_SELECTOR, "article div[data-message-author-role='assistant']")
        
        # If still not found, try a broader search
        if not elements:
            elements = self.driver.find_elements(By.CSS_SELECTOR, "[data-message-author-role='assistant']")
        
        return len(elements)

    def wait_for_response_complete(self, initial_response_count, timeout=60):
        """Wait until ChatGPT finishes typing before capturing the response"""
        end_time = time.time() + timeout
        last_text = ""

        while time.time() < end_time:
            # Try multiple selectors to find assistant responses
            elements = []
            
            # First try the new structure
            elements = self.driver.find_elements(By.CSS_SELECTOR, "article[data-turn='assistant'] div[data-message-author-role='assistant']")
            
            # If not found, try the old structure
            if not elements:
                elements = self.driver.find_elements(By.CSS_SELECTOR, "article div[data-message-author-role='assistant']")
            
            # If still not found, try a broader search
            if not elements:
                elements = self.driver.find_elements(By.CSS_SELECTOR, "[data-message-author-role='assistant']")
            
            if not elements:
                time.sleep(0.5)
                continue

            # Only process if we have more responses than when we started
            if len(elements) > initial_response_count:
                latest = elements[-1]
                current_text = latest.text.strip()

                if current_text == last_text and current_text != "":
                    # Stable text, assume finished
                    return current_text

                last_text = current_text
            
            time.sleep(1)

        return last_text

    def monitor_clipboard(self):
        while True:
            try:
                clipboard_text = pyperclip.paste()
                if clipboard_text != self.last_clipboard and clipboard_text.strip():
                    self.last_clipboard = clipboard_text
                    print(f"Clipboard detected: {clipboard_text[:50]}...")

                    # Get response count before sending new message
                    initial_response_count = self.get_response_count()
                    
                    # Start timer
                    start_time = time.time()
                    
                    self.paste_to_chat(clipboard_text)

                    # Wait for full response
                    response = self.wait_for_response_complete(initial_response_count)
                    if response and response != self.last_response:
                        # Calculate response time
                        response_time = time.time() - start_time
                        response_time_str = f"{response_time:.1f}s"
                        
                        self.last_response = response
                        print(f"\n=== ChatGPT Response ({response_time_str}) ===")
                        print(response)
                        print("=" * 50)
                        self.response_popup.show_response("ChatGPT", response, response_time_str)

                time.sleep(1)
            except Exception as e:
                print(f"Clipboard monitor error: {e}")
                time.sleep(2)

    def run(self):
        self.setup_browser()
        threading.Thread(target=self.monitor_clipboard, daemon=True).start()
        print("Clipboard monitor started. Copy text and watch it send to ChatGPT!")

        # Keep alive
        root = tk.Tk()
        root.withdraw()  # no root window, just popups
        root.mainloop()

if __name__ == "__main__":
    bot = ChatGPTBot()
    bot.run()
