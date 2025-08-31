# ROKAB

A Rise of Kingdoms answering bot that uses Selenium and ShareX OCR for automated question answering.

## ⚡ Quick Start

**For executable users:** Download from [Releases](https://github.com/wtfmerc/ROKAB/releases) on the right side of this page. Then follow the steps below.

### 🔹 Need help? Add me on Discord: **wtfmerc**

Or join the server! [Discord Invite](https://discord.com/invite/jCgTXpWmTK)


ROKAnswerBot Tutorial - Complete Setup Guide
============================================

This tutorial will guide you through setting up ROKAnswerBot with ShareX OCR for automatic Rise of Kingdoms question answering.

PREREQUISITES:
- Windows PC
- Internet connection
- ChatGPT account

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

SUPPORT:
========

For issues or questions:
- Check the console output for error messages
- Ensure all prerequisites are met
- Verify ShareX and ChatGPT are working independently

ENJOY YOUR AUTOMATED RISE OF KINGDOMS ASSISTANT!
===============================================

The bot will help you quickly get answers to Rise of Kingdoms questions
by automatically sending them to ChatGPT and displaying the responses.
