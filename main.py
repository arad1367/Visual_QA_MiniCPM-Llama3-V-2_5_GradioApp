# -*- coding: utf-8 -*-
"""Visual-QA-Multi-models-100done.ipynb

# Visual Question Answering App
* Made with love by `Pejman`

### 1. Salesforceblip_vqa_base Model (Simple model)
"""

!pip install transformers Pillow requests

from PIL import Image
import requests
from io import BytesIO

img_url = 'https://theedgemalaysia.com/_next/image?url=https%3A%2F%2Fassets.theedgemarkets.com%2FBeyond-Insights_AdvDec_thumb_12Dec2022.jpg&w=1920&q=75'
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))
img

import requests
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering

processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base").to("cuda")

img_url = 'https://theedgemalaysia.com/_next/image?url=https%3A%2F%2Fassets.theedgemarkets.com%2FBeyond-Insights_AdvDec_thumb_12Dec2022.jpg&w=1920&q=75'
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

question = "Describe the image in detail with all informations in 100 words"
inputs = processor(raw_image, question, return_tensors="pt").to("cuda")

out = model.generate(**inputs)
print(processor.decode(out[0], skip_special_tokens=True))

"""### 2. MiniCPM-Llama3-V-2_5 Model (Trend model)"""

!pip install Pillow==10.1.0 torch==2.1.2 torchvision==0.16.2 transformers==4.40.0 sentencepiece==0.1.99

import transformers
print(f"transformers versio: {transformers.__version__}")

# test.py
import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True, torch_dtype=torch.float16)
model = model.to(device='cuda')

tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True)
model.eval()

image = Image.open('/content/finC.png').convert('RGB')
question = 'Describe the image in detail?'
msgs = [{'role': 'user', 'content': question}]

res = model.chat(
    image=image,
    msgs=msgs,
    tokenizer=tokenizer,
    sampling=True, # if sampling=False, beam_search will be used by default
    temperature=0.7,
    # system_prompt='' # pass system_prompt if needed
)
print(res)

## if you want to use streaming, please make sure sampling=True and stream=True
## the model.chat will return a generator
res = model.chat(
    image=image,
    msgs=msgs,
    tokenizer=tokenizer,
    sampling=True,
    temperature=0.7,
    stream=True
)

generated_text = ""
for new_text in res:
    generated_text += new_text
    print(new_text, flush=True, end='')

"""### 3. Make a Gradio App and make it live!"""

!pip install gradio

import gradio as gr
import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer

# Load the model and tokenizer
model = AutoModel.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True, torch_dtype=torch.float16)
model = model.to(device='cuda')
tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True)
model.eval()

# Define a function to generate a response
def generate_response(image, question):
    msgs = [{'role': 'user', 'content': question}]
    res = model.chat(
        image=image,
        msgs=msgs,
        tokenizer=tokenizer,
        sampling=True,
        temperature=0.7,
        stream=True
    )
    generated_text = ""
    for new_text in res:
        generated_text += new_text
    return generated_text


# Create a Gradio interface
iface = gr.Interface(
    fn=generate_response,
    inputs=[gr.Image(type="pil"), "text"],
    outputs="text",
    title="Visual Question Answering",
    description="Input an image and a question related to the image to receive a response.",
)

# Launch the app
iface.launch(debug=True)

