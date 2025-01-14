# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 15:22:41 2020

@author: The Absolute Tinkerer

https://www.openstreetmap.org/export
"""

import os
import sys

from PyQt5.QtWidgets import QApplication

# Simplify our imports from other files
sourcePath = 'src'
sys.path.append(sourcePath)

# Gather all of the python source files and add them to the system path
for subdir, dirs, files in os.walk(os.path.join(os.getcwd(), sourcePath)):
    for directory in dirs:
        if directory != '__pycache__':
            sys.path.append(os.path.join(subdir, directory))

import constants as c
from MainWindowHandlers import MainWindowHandlers
from mapwidget import MapWidget
from configuration import Configuration


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Ensure we create the necesary folders if they don't exist
    if not os.path.exists(c.FOLDER_DATA):
        os.mkdir(c.FOLDER_DATA)
    if not os.path.exists(c.FOLDER_OUTPUT):
        os.mkdir(c.FOLDER_OUTPUT)
    if not os.path.exists(c.FOLDER_CONFIGS):
        os.mkdir(c.FOLDER_CONFIGS)
    if not os.path.exists(c.FOLDER_USER_CONFIGS):
        os.mkdir(c.FOLDER_USER_CONFIGS)
    if not os.path.exists(c.FOLDER_OUTPUT_CONSOLE):
        os.mkdir(c.FOLDER_OUTPUT_CONSOLE)

    if '--no-gui' in  sys.argv:
        print(sys.argv)
        input_fname = 'planet_48.9,55.703_49.317,55.871.osm'
        output_fname = 'output/console/map.jpg'
        max_dim = 6000

        # Create and save map render using the MapWidget object
        widget = MapWidget()
        
        # Same size as in MainWindowHandlers
        widget.resize(986, 631)
        widget.setConfiguration(Configuration())
        widget.setOSMFile(input_fname)
        widget.saveImage(max_dim, output_fname)

        # Kill application
        app.quit()
    else:
        # Start the program
        window = MainWindowHandlers()
        window.initialize()
        window.show()

        sys.exit(app.exec_())
