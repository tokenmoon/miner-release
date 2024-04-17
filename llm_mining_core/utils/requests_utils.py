import time
import psutil
import requests
from .cuda_utils import get_hardware_description

DEFAULT_MINER_ID = "default_miner_id"

def check_vllm_server_status():
    """
    Checks if the vLLM server process is currently running.
    This function iterates over the running processes and checks if any process
    matches the criteria for the vLLM server process. It looks for a process
    with 'python' as the first argument, '-m' as one of the arguments, and
    'vllm.entrypoints.openai.api_server' as another argument.
    Returns:
        bool: True if the vLLM server process is running, False otherwise.
    """
    for proc in psutil.process_iter(['pid', 'cmdline']):
        cmdline = proc.info['cmdline']
        if cmdline and 'python' in cmdline[0] and '-m' in cmdline and 'vllm.entrypoints.openai.api_server' in cmdline:
            return True
    return False

def send_miner_request(config, miner_id, model_id):
    """
    Sends a request for a new mining job to the server using the given configuration.

    Parameters:
        config (BaseConfig): The configuration instance containing necessary settings.
        miner_id (str): The ID of the miner requesting a job.

    Returns:
        dict or None: The job details as a dictionary if available, otherwise None.
    """
    url = f"{config.base_url}/miner_request"
    if miner_id is None:
        miner_id = DEFAULT_MINER_ID
    request_data = {
        "miner_id": miner_id,
        "model_id": model_id,
        "min_deadline": 1
    }

    # Check and update the last heartbeat time for the specific miner_id
    current_time = time.time()
    if current_time - config.last_heartbeat_per_miner[miner_id] >= 60:
        request_data['hardware'] = get_hardware_description()
        request_data['version'] = config.version
        config.last_heartbeat_per_miner[miner_id] = current_time

    response = requests.post(url, json=request_data)
    # Assuming response.text contains the full text response from the server
    warning_indicator = "Warning:"
    if response and warning_indicator in response.text:
        # Extract the warning message and use strip() to remove any trailing quotation marks
        warning_message = response.text.split(warning_indicator)[1].strip('"')
        print(f"WARNING: {warning_message}")
        return None, None

    try:
        data = response.json()
        end_time = time.time()
        request_latency = end_time - current_time
        if isinstance(data, dict):
            return data, request_latency
        else:
            return None, None
    except Exception as e:
        # fail silently
        return None, None