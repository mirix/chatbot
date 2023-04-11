# ChatBot

Simple example of how to deploy a minimalistic AI chatbot on consumer's hardware.

INSTRUCTIONS

1. Install a recent Python version.

2. Install flask, pytorch and transformers via pip.

2. Clone this repo.

3. Run app.py with Python from the terminal. The model may take up to a minute to load initially.

4. Ctrl + click on the terminal URL to open the app in your default browser.


NOTES

The default model is bigscience's T0_3B:

https://huggingface.co/bigscience/T0_3B

It requires 12 GB of hard disk space and about twice that amount of RAM memory.

You can switch to another model by editing the "name" variable in the app.py script.

Downloading the model may take a while. You may prefer to clone the corresponding Hugging Face repo beforehand and setting the name variable to the download path of the model folder.

This chatbot was tested on Majaro Linux and Ubuntu 22.04 with 32 GB of RAM and Intel integrated graphics (no CUDA accelerator required).

Google's flan-t5-xl also works on the same hardware, but I have found T0_3B to be a bit more accurate. 

With less RAM you may need to switch to a smaller model such as flan-t5-small, flan-t5-base or flan-t5-large, whereas the more accurate flan-t5-xxl will require humongous amounts of RAM and one or more CUDA accelerators.

To save disk space, if applicable, you can remove the all the model binaries (such as flax or tensorflow) except the pytorch ones.

