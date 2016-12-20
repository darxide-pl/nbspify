import sublime, sublime_plugin, re

class NbspifyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        for region in view.sel():
            self.view.replace(edit,region,re.sub('\s([a-z]{1})(\s)',' '+r'\1&nbsp;',view.substr(region)))