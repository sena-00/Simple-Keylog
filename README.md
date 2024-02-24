# Simple Keylog
>[!WARNING]
> This is meant for educational purposes only. Do not use any application whatsoever with malicious intent.

Simple Keylog is being developed in Python and is a *work in progress*. The purpose is to log every key that has been pressed on the host computer and save it to a .txt file

## Functions
- Log keys used in `keyfile.txt`. If the file `keyfile.txt` has not been created, the script will create it. If the the .txt already exists, text will be appended to it.
- Table for Logging symbols:

| Key Pressed | Logged as |
| ----------- | ----------- |
| Backspace   | <*BackSpace*> |
| Enter   | <*Enter*>         |
| Tab   | <*Tab*>             |
| Other Symbols   | <*Unhandled Special Key*>|
- F10 has been added as a failsafe. In case the key is pressed, the script stops recording.

## Demo
The video below show a the demo for the current state of the application.

https://github.com/sena-00/Simple-Keylog/assets/156020094/6a44d063-b3de-4a64-9633-a97cc7e4a8d9

## To-do List
- [x] Create the original file
- [x] Add Error handling for special characters
- [ ] Set a hidden path for the "keyfile.txt" to be stored
- [ ] Enable Dropbox token usage (Send log files to a rmeote dropbox account)
