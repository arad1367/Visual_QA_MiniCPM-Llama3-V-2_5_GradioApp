# Visual Question Answering Project
This repository contains Python code for a visual question answering project. The project uses various libraries and models to analyze images and answer questions related to them.

### Table of Contents
* Installation
* Usage
* Models
* Gradio App

### Installation
To run the code in this repository, you need to install the following Python libraries:

* Pillow==10.1.0 torch==2.1.2 torchvision==0.16.2 transformers==4.40.0 sentencepiece==0.1.99 gradio
You can install these libraries using pip

### Usage
The code in this repository is divided into three main sections:

- Image Description using BLIP Model (Our old model)
- MiniCPM-Llama3-V-2_5 Model (Trend model)
- Gradio App for Visual Question Answering
 
### 1. Image Description using BLIP Model
This section of the code uses the BLIP model to describe an image in detail. The image is fetched from a URL, and the description is generated using the BLIP model.

### 2. MiniCPM-Llama3-V-2_5 Model (Trend model)
This section of the code uses the MiniCPM-Llama3-V-2_5 model to describe an image in detail. The image is loaded from a local file, and the description is generated using the MiniCPM-Llama3-V-2_5 model.

### 3. Gradio App for Visual Question Answering
This section of the code creates a Gradio app for visual question answering. The app allows users to input an image and a question related to the image, and it generates a response using the MiniCPM-Llama3-V-2_5 model.

### Models
* Salesforce/blip-vqa-base
* openbmb/MiniCPM-Llama3-V-2_5

### Gradio App
The Gradio app is created using the gradio library. 
It allows users to input an image and a question related to the image, and it generates a response using the MiniCPM-Llama3-V-2_5 model. 
The app is launched using the iface.launch(debug=True) command.

# Author
* The App is made by Pejman Ebrahimi
* Email: `pejman.ebrahimi77@gmail.com` and `info@giltech-support.co.uk`
* Website: `https://www.giltech-megoldasok.com/`
