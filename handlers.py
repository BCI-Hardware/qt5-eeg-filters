# from loguru import logger
from PyQt5.QtWidgets import QApplication


class Handler:

    def __init__(self, config, model, view, controller):
        self.model = model
        self.config = config
        self.view = view
        self.controller = controller

    def bandwidths_activated(self, item) -> None:
        """handler change bandwidth.
        Returns - True if ok.
        """
        if item.text() == 'source' and not self.config.source_filepath:
            self.show_dialog_open()
            return None
        self.view.show_progress_bar()
        self.controller.counter_proc = 0
        self.controller.counter_factor = 50
        self.controller.get_data_show_graphics()
        self.view.hide_progress_bar()

    def change_range_search_extremums(self) -> None:
        """
        Handler event change region search extremums.

        Returns - True if ok.

        """
        if self.model.total_count == 0 or not self.model.dict_showed_extremums:
            return None

        self.view.lineEditMaxStart.setText(
            str(round(self.view.range_search_maxmums.getRegion()[0], 5))
        )
        self.view.lineEditMaxEnd.setText(
            str(round(self.view.range_search_maxmums.getRegion()[1], 5)))

        self.view.lineEditMinStart.setText(
            str(round(self.view.range_search_minimums.getRegion()[0], 5))
        )
        self.view.lineEditMinEnd.setText(
            str(round(self.view.range_search_minimums.getRegion()[1], 5)))
        self.view.show_progress_bar()
        self.controller.counter_proc = 0
        self.controller.counter_factor = 100
        self.controller.calc_and_show_extremums()
        self.view.hide_progress_bar()

    def change_value_slider(self) -> bool:
        """Handler event change value slider.
        Returns - True if ok.
        """
        self.view.iter_value = (
                self.view.slider1.value()
                * self.config.max_iter_value
                / self.config.max_step_iter
        )
        QApplication.processEvents()
        self.view.show_progress_bar()
        self.controller.counter_proc = 0
        self.controller.counter_factor = 50
        self.controller.get_data_show_graphics()
        self.view.hide_progress_bar()
        return True

    def show_dialog_open(self) -> bool:
        """Show dialog window.
        Returns - True if ok.
        """
        self.config.source_filepath = self.view.get_source_file_name()

        if not self.config.source_filepath:
            return False
        item = self.view.listBandwidths.item(0)
        item.setSelected(True)
        self.view.listBandwidths.setCurrentItem(item)
        self.view.show_progress_bar()
        self.controller.counter_proc = 0
        self.controller.counter_factor = 25
        self.controller.prepare_data()
        self.controller.get_data_show_graphics()
        self.view.hide_progress_bar()
        return True

    def save_button_pressed(self) -> bool:
        """handler event save button pressed.
        Returns - True if ok.
        """
        if not self.config.target_dirpath:
            self.config.target_dirpath = self.view.get_target_file_name()
        if not self.config.target_dirpath:
            return False
        QApplication.processEvents()
        self.view.show_progress_bar()
        self.controller.counter_proc = 0
        self.controller.counter_factor = 100
        self.controller.export_data()
        self.view.hide_progress_bar()
        return True

    def hide_show_regions(self):
        # logger.debug("start hiding")
        if self.view.range_search_minimums.isVisible():
            self.view.range_search_minimums.setVisible(0)
            self.view.range_search_maxmums.setVisible(0)
            return
        self.view.range_search_minimums.setVisible(1)
        self.view.range_search_maxmums.setVisible(1)

    def close_button_pressed(self) -> None:
        """Handler event pressed close button.
        Returns: None.
        """
        if self.model.dict_bandwidth_data:
            self.save_button_pressed()
        QApplication.quit()

    def change_text_line_extremums_edits(self) -> bool:
        """
        Handler event change text search extremums.

        Returns - True if ok.

        """
        if self.model.total_count == 0 or not self.model.dict_showed_extremums:
            return False
        self.view.range_search_maxmums.setRegion([
            float(self.view.lineEditMaxStart.text()),
            float(self.view.lineEditMaxEnd.text())
        ])
        self.view.range_search_minimums.setRegion([
            float(self.view.lineEditMinStart.text()),
            float(self.view.lineEditMinEnd.text())
        ])
        self.view.show_progress_bar()
        self.controller.counter_proc = 0
        self.controller.counter_factor = 100
        self.controller.calc_and_show_extremums()
        self.view.hide_progress_bar()
        return True

    def add_new_bandwidth(self) -> None:
        """handler event pressed button add bandwidth."""
        text = self.view.lineEdit_3.text()
        self.view.listBandwidths.addItem(text)
        splitted_text = text.split(',')
        value = [
            int(splitted_text[0].replace('[', '')),
            int(splitted_text[1].replace(']', '').replace(' ', ''))
        ]
        self.config.bandwidths.append(value)
        self.view.lineEdit_3.clear()