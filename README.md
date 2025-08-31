# ROKAB

A Rise of Kingdoms answering bot that uses Selenium and ShareX OCR for automated question answering.

This bot is designed to be **unpatchable** in the traditional sense because it does **not interact with the game client at all**. Unlike typical game bots, it does not inject code, modify memory, or simulate in-game actions. Instead, it works entirely on the **user’s screen**:

- It captures text from screenshots using ShareX OCR.
- It sends the captured text to ChatGPT for processing.
- It returns answers in a popup — completely outside the game environment.

Because it operates only on visual data and standard browser/API interactions, updates to the game **cannot break the bot**. Additionally, the bot is highly **configurable** — by changing the "prefix" or context in the configuration, it can be adapted to work with **any application or game** that uses text-based questions, not just Rise of Kingdoms.  

This approach ensures that:
- You are never altering the game client.
- The bot is resilient to updates and patches.
- It remains fully cross-platform compatible with minimal maintenance.

⚠️ **Legal Notice:**  
For legal and ethical reasons, this project **will not accept suggestions or features that automatically click or submit answers in-game**. All interactions with the game must be manual.  
However, I may create an **educational tutorial in the future** that explores image processing and automated answer detection in a controlled, non-game context. This would be purely for learning purposes and not intended for use in any live game environment.

## ⚡ Quick Start

**For executable users:** Download from [Releases](https://github.com/wtfmerc/ROKAB/releases) on the right side of this page. Then follow the steps below.

ROKAnswerBot Tutorial - Complete Setup Guide
============================================

This tutorial will guide you through setting up ROKAnswerBot with ShareX OCR for automatic Rise of Kingdoms question answering.

PREREQUISITES:
- Windows PC
- Internet connection
- ChatGPT account
- ShareX downloaded ( links below )

STEP 1: DOWNLOAD AND INSTALL SHAREX
===================================

1. Go to https://getsharex.com/
2. Click the "Download" button
3. Click "Setup" to download the installer
4. Run the ShareX setup file
5. Keep all settings default and click through the installation
6. Make sure "Launch ShareX" is checked at the end
7. Click "Finish" to complete installation

STEP 2: CONFIGURE SHAREX OCR HOTKEY
===================================

1. ShareX will launch automatically after installation
2. On the left side of the ShareX window, click "Hotkey settings"
3. Click "Add new hotkey"
4. Click "None" to open the dropdown menu
5. Navigate to: Tools > OCR
6. Set your preferred hotkey (recommended: Ctrl+Shift+O or similar)
7. Click "OK" to save the hotkey

STEP 3: CONFIGURE SHAREX OCR TASK SETTINGS
==========================================

1. Go back to the main ShareX window
2. Click "Task settings" (on the left side)
3. Click "OCR" in the task settings menu
4. Check ALL THREE boxes:
   ☑ Process OCR silently
   ☑ Automatically copy results to clipboard
   ☑ Close OCR window after opening service link
5. Click "OK" to save settings

STEP 4: LAUNCH ROKAnswerBot
===========================

1. Double-click "ROKAnswerBot.exe" to launch the bot
2. The bot will automatically:
   - Open Chrome browser
   - Navigate to ChatGPT
   - Wait for you to log in

STEP 5: LOGIN TO CHATGPT
========================

1. When Chrome opens to ChatGPT, log in with your account
2. The bot will automatically detect when you're logged in
3. You'll see "Login detected!" message when ready

STEP 6: USING THE BOT
=====================

1. Once logged in, the bot starts monitoring your clipboard
2. When you encounter a Rise of Kingdoms question:
   - Press your ShareX OCR hotkey (e.g., Ctrl+Shift+O)
   - Select the text area containing the question
   - ShareX will automatically:
     * Extract the text using OCR
     * Copy it to your clipboard
     * Close the OCR window
3. The bot will automatically:
   - Detect the copied text
   - Send it to ChatGPT with Rise of Kingdoms context
   - Display the answer in a popup with timing information

TROUBLESHOOTING:
================

If the bot doesn't start:
- Make sure you have Chrome browser installed
- Check that your antivirus isn't blocking the executable
- Try running as administrator

If OCR doesn't work:
- Verify ShareX is properly installed
- Check that your hotkey is set correctly
- Ensure the OCR task settings are configured

If ChatGPT doesn't respond:
- Make sure you're logged into ChatGPT
- Check your internet connection
- Verify the bot detected your login

If popups don't appear:
- Check that the bot is running in the background
- Verify clipboard monitoring is active
- Look for any error messages in the console

### 🔹 Need help? Add me on Discord: **wtfmerc**
### 🔹 Or join the server! [Discord Invite](https://discord.com/invite/jCgTXpWmTK)

---

## ⚖️ Legal Disclaimer

ROKAB is intended for **personal and educational use only**. By using this tool:

- You agree that all in-game actions must be manual; the bot does **not automatically click or submit answers**.  
- The developers are **not responsible** for any account issues, bans, or losses incurred while using this software.  
- This project should **not be interpreted as a cheat or bot** — it simply automates reading text and querying ChatGPT outside the game environment.  
- Any future tutorials or educational content related to image processing or answer detection will be **strictly for learning purposes** and not intended for live game use.

Use at your own risk.

