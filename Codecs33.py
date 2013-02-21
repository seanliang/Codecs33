import sublime
import os
import sys

def plugin_loaded():
	if sublime.platform() in ('linux', 'osx') and sublime.version() > '3000':
		path = os.path.join(sublime.packages_path(), 'Codecs33', 'lib')
		if path not in sys.path:
			sys.path.append(path)
	else:
		print('Warning: Codecs33 is only working for Sublime Text 3 on linux or osx')
