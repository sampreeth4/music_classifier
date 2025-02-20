import os
import librosa
import math
import json

DATASET_PATH  = "Data/genres_original"
JSON_PATH = "data_10.json"
SAMPLE_RATE = 22050
DURATION = 30
TRACK_DURATION = 30
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION

