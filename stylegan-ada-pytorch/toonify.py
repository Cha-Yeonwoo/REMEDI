import numpy as np
import PIL.Image
import torch

import dnnlib
import legacy
import pickle
from PIL import Image
import torch.nn as nn
import cv2

from fine_toon_project import run_projection

input_image_path = "/mnt/disk1/ivymm02/trump3.png"
network = "https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/transfer-learning-source-nets/ffhq-res256-mirror-paper256-noaug.pkl"
outdir = "./outputs"

projected_w = run_projection(network, input_image_path, outdir, False, 303, 1000)

device = torch.device('cuda')
ours_network = './models/ours_Webtoon.pkl'
with open(ours_network,'rb') as f:
    G = pickle.load(f).requires_grad_(False).to(device)
    
recon_image = G.synthesis(projected_w.unsqueeze(0), noise_mode='const')
recon_image = (recon_image + 1) * (255/2)
recon_image = recon_image.permute(0, 2, 3, 1).clamp(0, 255).to(torch.uint8)[0].cpu().numpy()
PIL.Image.fromarray(recon_image, 'RGB')
image = Image.fromarray(recon_image)
image.save('output.png')
