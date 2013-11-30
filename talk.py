#!/usr/bin/env python3
import pyaudio
from math import pi, sin
import sys

SAMPLE_RATE = 44.1 * 1000 # hertz
WAVE_DURATION = 1 # seconds

class Tone:
	"""Represents a sine wave for a given frequency.

	freq - frequency (in hertz)
	duration - duration of the wave (in seconds)
	sample_rate - sampling rate (in hertz)
	"""
	def __init__(self, freq, duration, sample_rate):
		self.freq = freq
		self.duration = duration
		self.sample_rate = sample_rate

		self.generate_wave()
	
	def generate_wave(self):
		wave_len = int(self.duration * self.sample_rate)
		period = self.sample_rate / self.freq

		self.wave = [sin(2 * pi * i / period) * 127 for i in range(wave_len)]

def make_tone(freq):
	return Tone(freq, WAVE_DURATION, SAMPLE_RATE)

if  __name__ == "__main__":
	if len(sys.argv) < 2:
		print("usage: ./talk.py start_freq")
		sys.exit(1)

	try:
		start_freq = int(sys.argv[1])
	except ValueError:
		print("bad starting frequency, please provide a number in Hz (e.g. 2000)")
		sys.exit(1)

	freqs = [start_freq, start_freq + 2000]
	tones = [make_tone(freq) for freq in freqs]
