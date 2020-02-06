# qt5-eeg-filters
GUI for eeg-filters based on Qt5

## Requirements

Programm require python >= 3.6

Also:

* eeg-filters
* pyQt5
* pyqtgraph

Note: You must have Qt5 installation om your PC.

## Installation



```
$ git clone https://github.com/yaricp/qt5-eeg-filters.git
$ cd qt5-eeg-filters/
$ ./install.sh
```

## Usage

For start programm just:

```
$ ./start.sh
```

After that you can see main windows of program:

You can open a file with EEG signals data.
This file you can get from NeuroExplorer4.4 by export data to ASCII format.

When curves will be showed on main plot you can make a filter it by checking bandwith in list of bandwidths.

You can move regions for searching extremums. Also you can change boundaries of this regions by text filds over main plot.

The any stage of your reseach you can save in folder what you want.


## Settings

Main setting of program are in file settings.py in projects folder.

You can set a default list of bandwiths, begin and end for regions searching extremums.

Important values are ORDER filter and RP for Chebyshev filter.

By change this values you can mange work of filter.
