import subprocess

from pynput import keyboard

notes = {}

def run_process(command):
    return subprocess.Popen(command, shell = True)

def stop_notes(key):
    global notes
    run_process("pkill sox")
    notes = {}
    
def play_note(key):
    global notes
    try:
        note = int(key.char)
    except:
        stop_notes(None)
        exit()
    if not note in notes:
        command = f"sox --buffer 256 -c 1 -r 48000 -t alsa default -t alsa default pitch {note*100} &> /dev/null"
        notes[note] = run_process(command)

# Collect events until released
with keyboard.Listener(
        on_press=play_note,
        on_release=stop_notes) as listener:
    listener.join()
