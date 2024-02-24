# Simple Keylog
>[!WARNING]
> This is meant for educational purposes only. Do not use any application whatsoever with malicious intent.

Simple Keylog is being developed in Python and is a *work in progress*. The purpose is to log every key that has been pressed on the host computer and save it to a .txt file
- If the file has not been created, the script will create it. If the the .txt already exists, text will be appended to it.
- For backspace, the log will be shown as <*BackSpace*> and Enter as <*Enter*>
- F10 has been added as a failsafe. In case the key is pressed, the script stops recording.
- Initially the script would send an e-mail alerting that 300KB of logs had been saved. The idea was scrapped later however, since Google disabled LSA (Less Secure Apps). A work-around is being thought out.



https://github.com/sena-00/Simple-Keylog/assets/156020094/6a44d063-b3de-4a64-9633-a97cc7e4a8d9

