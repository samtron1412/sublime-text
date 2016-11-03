import sublime, sublime_plugin

class ToggleGutter(sublime_plugin.WindowCommand):
    def run(self):
        setts = sublime.load_settings('Preferences.sublime-settings')
        checkGutter = setts.has('gutter')

        if checkGutter:
            gutter = setts.get('gutter')
            setts.set('gutter', not(gutter))
        else:
            setts.set('gutter', 'false')

        sublime.save_settings('Preferences.sublime-settings')
