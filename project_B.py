#		python code
#
#		script_name: Project B
#
#		author: Domingo Gallardo Saavedra
#

from earsketch import *
from random import *

init()
setTempo(128)

# Track numbers
introTrack = 1
guitarTracks = [2]
drumTracks = [3, 4]
beatTrack = [5, 6, 7]
melodyTrack = 8

#Other Variables
melodyStartMeasure = 6

# Intro
fitMedia(EIGHT_BIT_ANALOG_DRUM_LOOP_004, introTrack, 1, 3)

# Guitar Tracks
fitMedia(Y25_GUITAR_1, guitarTracks[0], 2, 6)

# Drum Tracks
fitMedia(DUBSTEP_DRUMLOOP_MAIN_001, drumTracks[0], 2, 6)

#
# Big loop for repeat the rhythm

for i in range(2):

	fitMedia(EIGHT_BIT_ANALOG_DRUM_LOOP_004, drumTracks[1], 6 + 16*i, 12 + 16*i)
	fitMedia(DUBSTEP_DRUMLOOP_MAIN_001, drumTracks[0], 16 + 16*i, 22 + 16*i)

	# Random melody

	melodyAudio = [ELECTRO_ANALOGUE_LEAD_009, ELECTRO_ANALOGUE_LEAD_010, ELECTRO_ANALOGUE_LEAD_011,
				   ELECTRO_ANALOGUE_LEAD_012]

	fitMedia(melodyAudio[randint(0, len(melodyAudio) - 1)], melodyTrack, melodyStartMeasure + 16*i, melodyStartMeasure + 2 + 16*i)
	fitMedia(melodyAudio[randint(0, len(melodyAudio) - 1)], melodyTrack, melodyStartMeasure + 4 + 16*i, melodyStartMeasure + 6 + 16*i)
	fitMedia(melodyAudio[randint(0, len(melodyAudio) - 1)], melodyTrack, melodyStartMeasure + 8 + 16*i, melodyStartMeasure + 10 + 16*i)
	fitMedia(melodyAudio[randint(0, len(melodyAudio) - 1)], melodyTrack, melodyStartMeasure + 12 + 16*i, melodyStartMeasure + 14 + 16*i)


	beatAudio = [ELECTRO_DRUM_MAIN_LOOPPART_010, OS_OPENHAT01, OS_LOWTOM04]
	beatList = ["0---0---0-----0-", "0---0-0-0---0-0-", "0---0---0---0---"]
	drumsStartMeasure = 6

	for j in range(8):

		makeBeat(beatAudio[0], beatTrack[0], drumsStartMeasure + j + 16*i, beatList[0])
		makeBeat(beatAudio[1], beatTrack[1], drumsStartMeasure + j + 16*i, beatList[1])
		makeBeat(beatAudio[2], beatTrack[2], drumsStartMeasure + j + 16*i, beatList[2])

# Effects

setEffect(1, REVERB, REVERB_TIME, 100.0)
setEffect(3, DISTORTION, DISTO_GAIN, 0, 0, 0, 0)
setEffect(3, DISTORTION, DISTO_GAIN, 0, 8, 30, 22)
setEffect(3, DISTORTION, DISTO_GAIN, 30, 35, 0, 38)


finish()
