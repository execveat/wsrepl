import pyperclip

from textual.widgets import Button
from textual.message import Message

from wsrepl.WSMessage import WSMessage

SYSTEM_COPY_WORKING = not not pyperclip.determine_clipboard()[0]

class CopyButton(Button):
    """A button that copies its data to the clipboard when pressed"""
    class Copied(Message):
        """Copy selected message."""
        def __init__(self, message: WSMessage) -> None:
            self.message = message
            super().__init__()

    def __init__(self, message: WSMessage, small) -> None:
        if small:
            name = "[Click to copy]"
        else:
            name = "Click to copy"

        super().__init__(name, classes="history-btn")
        self.message = message

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if SYSTEM_COPY_WORKING:
            pyperclip.copy(self.message.msg)
        else:
            self.post_message(self.Copied(self.message))
        self.blur()
