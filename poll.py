import requests, time, subprocess, platform

def notify(user_msg):
    """Function to notify the user"""
    # Run app.py as a separate process to avoid blocking the main thread
    os_name = platform.system()
    if os_name == 'Windows':
        # Using a class for Windows to hide the console window
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW  
        subprocess.Popen(["python", "notify.py", user_msg], startupinfo=startupinfo)
    elif os_name == 'Darwin':
        subprocess.Popen(["python", "notify.py", user_msg], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    elif os_name == 'Linux':
        print('This is a Linux operating system.')
    else:
        print('This is an unknown operating system.')


# Request from http://127.0.0.1:5000/msg
while True:
    try:
        res = requests.get("http://127.0.0.1:5000/msg").json()
        if res['global_msg']:
            print(res['global_msg'])
            notify(res['global_msg'])
            time.sleep(5)  # Wait 5 seconds so all computers see the message
            requests.post("http://127.0.0.1:5000/reset")
        else:
            print("No new messages.")
            time.sleep(1)
    except requests.exceptions.ConnectionError as e:
        print("Server is not running. Please start the server.")
        time.sleep(1)