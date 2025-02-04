class PluginBase:
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        raise NotImplementedError("Plugins must implement the execute method.")

