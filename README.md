# Harmonizer

Real time microphone harmonizer inspired on Jacob Collier's keyboard. It relies on the great Sound eXchange (SoX) command line tool.

[![IMAGE ALT TEXT HERE](https://i.ytimg.com/vi/DnpVAyPjxDA/hqdefault.jpg)](https://youtu.be/DnpVAyPjxDA?t=30)

## How it works

This is a work in progress. The script waits for number keys to be pressed, then triggers a process that runs [sox](https://en.wikipedia.org/wiki/SoX) with a pitch shift.

## Requirements

I tested it only in linux, help adding compatibility for other platforms is very welcomed :)

- sox: (If you are in ubuntu it'd be like this `sudo apt install sox`)
- python 3
- python libraries (Try something like: `pip3 install -r requirements.txt`)

## Usage

Run the script and then press some numbers in the keyboard.

```bash
python3 harmonizer.py
```

For example if you keep pressed 0, 4 and 7 it should make a major chord. But 0, 3 and 7 make a minor chord. It's because 0 is the root note here, the second semitone is 1 and so on.

Press any letter key to exit, 'q' for example.
