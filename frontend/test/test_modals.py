

def test_modals():
    try:
        modal = src.poll_commands.components.modals.MCPollModal(title="MC Question")
    except RuntimeError as e:
        return

def test_callback():
    src.poll_commands.components.modals.MCPollModal.callback(None, None)