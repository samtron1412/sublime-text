import sublime_plugin
class AlwaysCenterCommand(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        sel = view.sel()
        region = sel[0] if len(sel) == 1 else None
        if region != None:
            view.show_at_center(region)
