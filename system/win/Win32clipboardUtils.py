import win32clipboard as w
import win32con

def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

def setText(s):
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.EmptyClipboard()
    w.SetClipboardText(s)
    w.CloseClipboard()