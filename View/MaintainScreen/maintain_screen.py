from View.base_screen import BaseScreenView


class MaintainScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def exit(self):
        # import pdb
        # pdb.set_trace()
        # self.app.root_window.close()
        self.apps.stop()
        pass

    def home(self):
        self.apps.stop()
        pass
