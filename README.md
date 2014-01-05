midi-spc-kit (WIP)
==================

Tools for importing MIDI to N-SPC to ROM.  I might even finish this
before 2017.


Toolset
=======

Note that as a WIP, neither of these are actually usable yet.

1. midi2spc.py – import MIDI file to NSPC PSRAM image
2. spc2rom.py – import SPC image to SFC file

Configuration
-------------

Both tools are driven by a common configuration file format, controlling
some settings not natively present within the file formats.  A fully
developed config file will look something like this:

	[general]
	brr3 = trumpet.brr ; all filenames relative to config
	game = supermetroid ; implies lorom addressing
	
	[midi2spc]
	label = 00:01:45.00
	jump = 00:04:00.00  ; return to label time at this time
	song = 5    ; spc song number to overwrite
	track0 = 0  ; spc track = midi channel
	; ...
	
	[spc2rom]
	collection = 6
	song = 5

midi2spc
--------

Usage:

	midi2spc.py [-c config] [-o spcfile] file.mid

Imports the midi according to settings in the config and exports it to
the output SPC file.  Default filenames are the MIDI's basename with the
appropriate extension, e.g. `file.ini` for the config and `file.spc`.

A config file is required, as it sets the mapping between MIDI tracks
and SPC tracks, as well as the infinite loop points.

spc2rom
-------

Usage:

	spc2rom.py [-c config] [-o romfile] file.spc

Imports the pattern and track data in the SPC according to settings in
the config and exports them back to the ROM.  The default filenames are
once again the input file with the extension replaced, e.g. `file.ini`
for configuration and `file.sfc` for the ROM.  Note that the ROM should
be **unheadered**.

A config file is required, as it specifies what song to overwrite in the
ROM, and what game it actually is.

