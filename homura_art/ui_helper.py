def shortcut_button_connect(shortcut, button, slot):
    """Connecting a shortcut key and a button to the same slot"""
    shortcut.activated.connect(slot)
    button.clicked.connect(slot)
