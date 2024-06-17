import soundfile as sf
import torch
import torchaudio
import numpy as np
import jiwer
from pystoi import stoi
from pesq import pesq


def measure_metrics(target_path, preds_path):
    
    target_waveform, _ = torchaudio.load(target_path)
    preds_waveform, _  = torchaudio.load(preds_path)
    
    target_waveform = torch.nn.functional.pad(target_waveform, (0, 24000*6 - target_waveform.size(1)), "constant", 0)
    preds_waveform  = torch.nn.functional.pad(preds_waveform, (0, 24000*6 - preds_waveform.size(1)), "constant", 0)
    
    
    resampler = torchaudio.transforms.Resample(24000, 16000)
    target_waveform = resampler(target_waveform)
    preds_waveform  = resampler(preds_waveform)
    
    target_waveform = target_waveform.squeeze(0)
    preds_waveform  = preds_waveform.squeeze(0)
    
    target_waveform = np.array(target_waveform)
    preds_waveform  = np.array(preds_waveform)
    
    PESQ = pesq(16000, target_waveform, preds_waveform, 'wb')
    STOI = stoi(target_waveform, preds_waveform, 16000, extended=False)
    
    return PESQ, STOI

## Donald Trump
print("PESQ: {}, STOI: {}".format(*measure_metrics('/mnt/disk1/ivymm02/tortoise-tts/ground_truth/donald_trump_mos_gt.wav', '/mnt/disk1/ivymm02/tortoise-tts/generated_output/donald_trump_mos_ultra_fast.wav')))
print("PESQ: {}, STOI: {}".format(*measure_metrics('/mnt/disk1/ivymm02/tortoise-tts/ground_truth/donald_trump_mos_gt.wav', '/mnt/disk1/ivymm02/tortoise-tts/generated_output/donald_trump_mos_fast.wav')))
print("PESQ: {}, STOI: {}".format(*measure_metrics('/mnt/disk1/ivymm02/tortoise-tts/ground_truth/donald_trump_mos_gt.wav', '/mnt/disk1/ivymm02/tortoise-tts/generated_output/donald_trump_mos_standard.wav')))

## Elon Musk
print("PESQ: {}, STOI: {}".format(*measure_metrics('/mnt/disk1/ivymm02/tortoise-tts/ground_truth/elon_musk_mos_gt.wav', '/mnt/disk1/ivymm02/tortoise-tts/generated_output/elon_musk_mos_ultra_fast.wav')))
print("PESQ: {}, STOI: {}".format(*measure_metrics('/mnt/disk1/ivymm02/tortoise-tts/ground_truth/elon_musk_mos_gt.wav', '/mnt/disk1/ivymm02/tortoise-tts/generated_output/elon_musk_mos_fast.wav')))
print("PESQ: {}, STOI: {}".format(*measure_metrics('/mnt/disk1/ivymm02/tortoise-tts/ground_truth/elon_musk_mos_gt.wav', '/mnt/disk1/ivymm02/tortoise-tts/generated_output/elon_musk_mos_standard.wav')))

## Steve Jobs
print("PESQ: {}, STOI: {}".format(*measure_metrics('/mnt/disk1/ivymm02/tortoise-tts/ground_truth/steve_jobs_mos_gt.wav', '/mnt/disk1/ivymm02/tortoise-tts/generated_output/steve_jobs_mos_ultra_fast.wav')))
print("PESQ: {}, STOI: {}".format(*measure_metrics('/mnt/disk1/ivymm02/tortoise-tts/ground_truth/steve_jobs_mos_gt.wav', '/mnt/disk1/ivymm02/tortoise-tts/generated_output/steve_jobs_mos_fast.wav')))
print("PESQ: {}, STOI: {}".format(*measure_metrics('/mnt/disk1/ivymm02/tortoise-tts/ground_truth/steve_jobs_mos_gt.wav', '/mnt/disk1/ivymm02/tortoise-tts/generated_output/steve_jobs_mos_standard.wav')))  