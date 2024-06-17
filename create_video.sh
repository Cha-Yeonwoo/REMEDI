pdf_file="mnt/disk1/ivymm02/my_profile.pdf"
img="mnt/disk1/ivymm02/my_img.png"
voice="mnt/disk1/ivymm02/my_voice"
mode ="Webtoon"

source /home/ivymm02/anaconda3/etc/profile.d/conda.sh
conda init bash
conda activate tortoise3
python gpt_qna.py --pdf pdf_file

CUDA_VISIBLE_DEVICES=0 python3 ./tortoise-tts/tortoise/read.py --textfile /mnt/disk1/ivymm02/gpt_answer.txt --voice me --output_path ./voices --preset fast --kv_cache True --half True
conda deactivate 
conda activate stylegan
CUDA_VISIBLE_DEVICES=0 python ./stylegan2-ada-pytorch/toonify.py --source {img} --mode {mode}
python ./D-ID/api.py # --img mnt/disk1/ivymm02/temp/toon.png --voice mnt/disk1/ivymm02/temp/voice.wav 
