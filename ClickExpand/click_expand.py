import sublime, sublime_plugin

class ClickExpandCommand(sublime_plugin.TextCommand):
	def run(self, edit, event):
		
		if not hasattr(self, "is_drag"):
			self.is_drag = True

		selection = self.view.sel()
		if len(selection) != 1:
			self.view.run_command("drag_select", {"event": event})
			return
		region = selection[0]

		mousepos = [event['x'], event['y']]
		point = self.view.window_to_text(mousepos)
		new_region = sublime.Region(point, point)

		if region.contains(new_region):
			self.view.run_command("expand_region")
		else:
			self.view.run_command("drag_select", {"event": event})

	def want_event(self):
		return True
