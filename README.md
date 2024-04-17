# ⚙️ Heurist Miner Setup Guide

Welcome to the Heurist Miner setup guide. This document is designed to help you get started with the Heurist Miner, a tool for participating in the Heurist testnet mining program. Whether you're a seasoned miner or new to cryptocurrency mining, we've structured this guide to make the setup process as straightforward as possible.

## 📖 Introduction

Heurist Miner allows users to contribute to the Heurist network by performing AI inference tasks in exchange for rewards. This guide will take you through the necessary steps to set up your mining operation.

For curious readers to learn more about the hardware requirements for AI inference, read [Heurist's Guide to AI article](https://heuristai.medium.com/heurists-guide-to-ai-beginner-s-series-part-2-db77458a62dd).

## 🚀 Quick Start Guide

For those eager to dive in, here's a quick overview of the setup process:

1. Check system requirements and compatibility notes.
2. Configure your Miner ID(s).
3. Install necessary software (CUDA, Python).
4. Choose your setup: Windows or Linux guide.
5. Install miner scripts and dependencies.
6. Run the miner program.

## ⚠️ Important Notices

- **Preview Version**: You're working with a preview version of the Heurist Miner. Expect some bumps along the way. For assistance, join [Heurist Discord #miner-chat channel]( https://discord.com/invite/heuristai)
- **System Requirements**: Advanced users may skip steps they've already completed, but compatibility checks are recommended.
- **CUDA Compatibility**: CUDA versions 12.1 or 12.2 are advised for compatibility with PyTorch.

## 🛠️ Detailed Setup Guides

### Pre-setup Recommendations

- Python Installation: If Python 3.x is already installed on your system, you may not need to reinstall Miniconda and Python. However, managing dependencies via a Conda environment is recommended.
- CUDA Installation: For those with CUDA pre-installed, ensure that the PyTorch version (`pytorch-cuda`) installed matches your CUDA version.


### Configuring Your Miner ID

1. **Create a `.env` File:** Navigate to the root directory of your `miner-release` folder. Here, create a new file named `.env`. This file will hold the unique identifiers (miner IDs) for your mining operation. You can find the example `.env.example`
2. **Define Miner IDs:** In the `.env` file, you should assign an Ethereum wallet address as a miner ID for each of your GPUs. These Ethereum addresses will serve as the miner IDs, which are crucial for tracking your contributions and ensuring you receive rewards accurately. If you have multiple GPUs, i-th GPU will use i-th miner ID. You can use the same address or different ones, which doesn't affect your rewards. We support adding a custom tag as miner ID suffix to help you view the performance of each GPU individually.

Option 1: Use default GPU tags (obtained from GPU UUID)
```plaintext
MINER_ID_0=0xYourFirstWalletAddressHere
MINER_ID_1=0xYourSecondWalletAddressHere
```

Option 2: Customize GPU tags (only alphanumeric characters supported after a hyphen)
```plaintext
MINER_ID_0=0xYourFirstWalletAddressHere-GamingPC4090
MINER_ID_1=0xYourSecondWalletAddressHere-GoogleCloudT4
```


3. **(For SD Miners)If you have multiple GPUs** Change the `num_cuda_devices` in `config.toml` to the number of GPUs you want to use. The number should match the number of Miner IDs in `.env`

<details>
<summary><b>Stable Diffusion Miner Guide (Windows)</b></summary>

#### Step 1. (Optional) Update GPU drivers

1. Go to the [NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx) page.

2. Select your GPU model and OS.

3. Download and install the latest driver. Restart your PC if necessary.

#### Step 2. Install Miniconda

1. Download the Miniconda Installer. 
- Visit the [Miniconda Downloads page](https://docs.conda.io/projects/miniconda/en/latest/). 
- Get the latest Windows 64-bit version for Python 3.11.
conda activate pytorch-gpu-python-3-10.
#### Step 3. Create a Conda Environment

1. Open a command prompt (Win + X > “Command Prompt”).

2. Create the Environment:
- Type `conda create --name gpu-3-11 python=3.11` (or choose your Python version).
- Press Enter and wait for the process to finish.

3. Activate the Environment
- Type `conda activate gpu-3-11`

#### Step 4: Install CUDA Toolkit
1. Download and Install CUDA:
- Visit the [CUDA Toolkit 12.1 download page](https://developer.nvidia.com/cuda-12-1-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local).
- Select your OS version.
- Download and install it by following the prompts.

#### Step 5: Install PyTorch with GPU Support
1. Go to the [PyTorch Install Page](https://pytorch.org/get-started/locally/).
- Set Your Preferences: Choose PyTorch, Conda, CUDA 12.1
- Install PyTorch: Copy the generated command (like `conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia`). Paste it in the Command Prompt and hit Enter.

#### Step 6: Download Miner Scripts
1. Run `git clone https://github.com/heurist-network/miner-release` in command prompt. Or Click "Code -> Download ZIP" in this [Github repo - miner-release](https://github.com/heurist-network/miner-release) to download miner scripts.

#### Step 7: Install Dependencies from `requirements.txt`

1. Open Your Command Prompt
- Make sure you're still in your Conda environment. If not, activate it again with `conda activate gpu-3-11`

2. Navigate to `miner-release` folder
- Use the cd command to change directories to where `requirements.txt` is located. For example, `cd C:\Users\YourUsername\Documents\miner-release`.

3. Install Dependencies:
- `Run the command pip install -r requirements.txt`. This command tells pip (Python's package installer) to install all the packages listed in your requirements.txt file.

#### Step 8. Configuring Your Miner ID with a .env File
See the top of this guide.

#### Step 9. Run the miner program
1. Run `python3 sd-miner-v1.x.x.py` (select the latest version of file) in Conda environment command prompt.

2. Type `yes` when the program prompts you to download model files. It will take a while to download all models. The program will start processing automatically once it completes downloading.

#### Step 10. (Optional) Enhancing Your Mining Experience with CLI Options
To optimize and customize your mining operations, you can utilize the following command line interface (CLI) options when starting the miner:

#### `--log-level`
Control the verbosity of the miner's log messages by setting the log level. Available options are `DEBUG`, `INFO` (default), `WARNING`, `ERROR`, and `CRITICAL`.
#### `--auto-confirm`
Automate the download confirmation process, especially useful in automated setups. Use `yes` to auto-confirm or stick with `no` (default) for manual confirmation.
#### `--exclude-sdxl`
Exclude SDXL models. Recommended for Laptop GPUs, 3060, 4060, or if you are running LLM miner alongside SD miner on a same GPU, or if your available VRAM is less than 10GB. SDXL models consumes more resources (and they also earn more rewards). Turning it off will prevent performance issues or crashes on slower GPUs.

**Usage Example:**

To enable debug-level logging and auto-confirm:
```bash
python sd-miner.py --log-level DEBUG --auto-confirm yes
```

To exclude SDXL models:
```bash
python sd-miner.py --exclude-sdxl
```

Congratulations! 🌟 You're now set to serve image generation requests. You don't need to keep it up 24/7. Feel free to close the program whenever you need your GPU like playing video games or streaming videos.

</details>

<details>
<summary><b>Stable Diffusion Miner Guide (Linux)</b></summary>
This guide assumes you're familiar with the terminal and basic Linux commands. Most steps are similar to the Windows setup, with adjustments for Linux-specific commands and environments.

- Python Installation: If Python 3.x is already installed, you can skip the Miniconda installation. However, using Miniconda or Conda to manage dependencies is still recommended.
- CUDA: If CUDA is previously installed, ensure the PyTorch installation matches your CUDA version.

### Step 1. Update GPU drivers (Optional)
- Use your Linux distribution's package manager or download drivers directly from the [NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx). For Ubuntu, you might use commands like `sudo apt update` and `sudo ubuntu-drivers autoinstall`.

### Step 2. Install Miniconda or Conda (Optional)
- Download the Miniconda installer for Linux from the [Miniconda Downloads page](https://docs.anaconda.com/free/miniconda/).
- Use the command line to run the installer.
  
### Step 3. Create a Conda Environment
- Open a terminal.
- Create a new environment with `conda create --name gpu-3-11 python=3.11`.
- Activate the environment using `conda activate gpu-3-11`.

### Step 4: Install CUDA Toolkit
- Install CUDA from the [CUDA Toolkit download page](https://developer.nvidia.com/cuda-12-1-0-download-archive) appropriate for your Linux distribution. Follow the installation instructions provided on the NVIDIA website.

### Step 5: Install PyTorch with GPU Support
- Visit the [PyTorch installation guide](https://pytorch.org/get-started/locally/), set preferences for Linux, Conda, and the appropriate CUDA version.
- Use the provided command in the page, such as `conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia`, in your terminal.

### Step 6: Download Miner Scripts
- Use Git to clone the miner scripts repository with `git clone https://github.com/heurist-network/miner-release`. Alternatively, download the ZIP from the GitHub page and extract it.
  
### Step 7: Install Dependencies from requirements.txt
- Ensure you're in the Conda environment (`conda activate gpu-3-11`).
- Navigate to the miner-release directory.
- Install dependencies with `pip install -r requirements.txt`.

### Step 8. Configure your Miner ID
Use `.env` in the miner-release folder to set a unique miner_id for each GPU. (See the top of this guide. This is very important for tracking your contribution!)

### Step 9. Run the miner program
- Execute the miner script with `python3 sd-miner-v1.x.x.py` (select the latest version) in your terminal. Agree to download model files when prompted.

### Step 10. (Optional) Enhancing Your Mining Experience with CLI Options
To optimize and customize your mining operations, you can utilize the following command line interface (CLI) options when starting the miner:

#### `--log-level`
Control the verbosity of the miner's log messages by setting the log level. Available options are `DEBUG`, `INFO` (default), `WARNING`, `ERROR`, and `CRITICAL`.
#### `--auto-confirm`
Automate the download confirmation process, especially useful in automated setups. Use `yes` to auto-confirm or stick with `no` (default) for manual confirmation.
#### `--exclude-sdxl`
Exclude SDXL models. Recommended for Laptop GPUs, 3060, 4060, or if you are running LLM miner alongside SD miner on a same GPU, or if your available VRAM is less than 10GB. SDXL models consumes more resources (and they also earn more rewards). Turning it off will prevent performance issues or crashes on slower GPUs.

**Usage Example:**

To enable debug-level logging and auto-confirm:
```bash
python sd-miner.py --log-level DEBUG --auto-confirm yes
```

To exclude SDXL models:
```bash
python sd-miner.py --exclude-sdxl
```
  
### Additional Linux-Specific Tips:
- Use `screen` or `tmux` to keep the miner running in the background, especially when connected via SSH.

</details>

<details>
<summary><b>Large Language Model Miner Guide</b></summary>

We use [vLLM](https://docs.vllm.ai/en/latest/), a fast and easy-to-use library for LLM inference and serving. We have only tested the miner program on Linux.

### Prerequisites
- Make sure you have CUDA driver installed. We recommend using NVIDIA drivers with CUDA version 12.1 or 12.2. Other versions may probably work fine. Use `nvidia-smi` command to check CUDA version.
- You need enough disk space. You can find model size in [heurist-models repo](https://github.com/heurist-network/heurist-models/blob/main/models.json). Use `df -h` to see available disk space.
- You must be able to access [HuggingFace](https://huggingface.co/) from internet.

### Select a Model ID
LLMs typically consume a large amount of VRAM (Video Memory) of your GPU. Larger models have higher VRAM requirements and also have higher rewards. Read [Miner Guide Docs](https://docs.heurist.ai/guides/miner-guide) to choose a model that fits your hardware.

### Run the Setup Script
```bash
chmod +x llm-miner-starter.sh
./llm-miner-starter.sh <model_id> --miner-id-index 0 --port 8000 --gpu-ids 0
```

`model_id` is mandatory. For example, `openhermes-2.5-mistral-7b-gptq` is the smallest model that we support. It requires 12GB VRAM.

#### Meaning of Optional CLI arguments
- `--miner-id-index` specifies the index of miner_id in `.env` file to use. Default is 0 (using the first address configured)
- `--port` specifies the port to communicate with vLLM process. Default is 8000. Change this if this port is occupied.
- `--gpu-ids` specifies the GPU ID to use. Default is 0. Change this if you have multiple GPUs and want to use a different one.

#### Example startup command

To use default options:
```bash
./llm-miner-starter.sh openhermes-2.5-mistral-7b-gptq
```

To use the second address with custom port and GPU ID
```bash
./llm-miner-starter.sh openhermes-2.5-mistral-7b-gptq --miner-id-index 1 --port 8001 --gpu-ids 1
```

### If you have trouble downloading
The first time that the miner program starts up will take a long time because it needs to download the model file. You should see progress bars in the command line output. Models are saved in `$HOME/.cache/huggingface` by default. If download progress is interrupted or throws an error, press "Ctrl+C" to stop the starter script and retry. If it's still stuck, delete `$HOME/.cache/huggingface` and try again.

### If you are running 8x7b or 34b or 70b model
We notice that 8x7b, 34b, 70b model loading might take very long time (up to 1 hour) on some devices. If you keep seeing "Model is not ready" and if you don't see any error during downloading, you should wait for some more time.

### Reference table demonstrating model id and vram usage
| Model ID | VRAM Usage (GB) |
|----------|-----------------|
| openhermes-2.5-mistral-7b-gptq  | 10               |
| mistralai/mistral-7b-instruct-v0.2       | 15               |
| openhermes-2-pro-mistral-7b     | 15               |
| mistralai/mixtral-8x7b-instruct-v0.1 | 28               | 
| openhermes-mixtral-8x7b-gptq | 28        |
| openhermes-2-yi-34b-gptq       | 37               |
| meta-llama/llama-2-70b-chat              | 41               |

</details>

## ❓ Troubleshooting and FAQs

## General Questions

**Q: Can I run LLM miner on Windows?** 

**A:** You may run the miner program with WSL, but we haven't tested it yet. There may be unexpected issues.

## Technical Issues

**Q: Why do I see "Model is not ready. Waiting for LLM Server to finish loading the model to start."?**  

**A:** It takes some time to download and load model files before it starts serving requests. Please confirm the downloading progress bar is showing up. Otherwise, it may indicate that your internet is having issues connecting to HuggingFace where the model files are stored. We plan to host the model at a different location soon.

**Q: Why do I see "CUDA out of memory error"?**  

**A:** Use `nvidia-smi` to see available memory. Check if there are any other processes using the GPU. Confirm that your available GPU memory satisfies the minimum requirement for the model. If you have multiple GPUs, make sure you configure `--gpu-ids` to specify a GPU with sufficient free VRAM.
