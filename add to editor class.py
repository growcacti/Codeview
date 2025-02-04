import importlib.util
import os

class MultiTabTextEditor:
    def __init__(self, parent):
        # Other initializations
        self.plugins = []
        self.plugin_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Plugins", menu=self.plugin_menu)
        self.load_plugins()

    def load_plugins(self):
        plugin_dir = "./plugins"
        if not os.path.exists(plugin_dir):
            os.makedirs(plugin_dir)
        
        for file in os.listdir(plugin_dir):
            if file.endswith(".py") and file != "__init__.py":
                plugin_path = os.path.join(plugin_dir, file)
                module_name = os.path.splitext(file)[0]
                spec = importlib.util.spec_from_file_location(module_name, plugin_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for attr in dir(module):
                    plugin_class = getattr(module, attr)
                    if isinstance(plugin_class, type) and issubclass(plugin_class, PluginBase) and plugin_class is not PluginBase:
                        plugin_instance = plugin_class(self)
                        self.plugins.append(plugin_instance)
                        self.plugin_menu.add_command(label=plugin_class.__name__, command=plugin_instance.execute)

