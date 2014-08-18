import sublime, sublime_plugin, datetime

class InsertDatetimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()
        fmt = '%d-%m-%Y'
        dt = datetime.datetime.now().strftime(fmt)
        for s in sel:
            self.view.insert(edit, 0, dt + ": ")
