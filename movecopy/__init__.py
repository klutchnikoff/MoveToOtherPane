from fman import DirectoryPaneCommand, show_alert

from fman.url import join, basename
from fman.fs import move, copy


def get_path_to_other_pane(pane):
	panes = pane.window.get_panes()
	this_pane = panes.index(pane)
	other_pane = panes[(this_pane + 1) % len(panes)]
	path = other_pane.get_path()
	return path

class MoveToOtherPane(DirectoryPaneCommand):

	def __call__(self):
		target_path = get_path_to_other_pane(self.pane)
		chosen_files = self.get_chosen_files()
		for filep in chosen_files:
			move(filep,  target_path)
		

class CopyToOtherPane(DirectoryPaneCommand):
	
	def __call__(self):
		target_path = get_path_to_other_pane(self.pane)
		chosen_files = self.get_chosen_files()
		for filep in chosen_files:
			dest_url = join(
				target_path,
				basename(filep)
			)
			copy(filep,  dest_url)
		