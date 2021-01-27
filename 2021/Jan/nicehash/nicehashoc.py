from datetime import datetime
import os
import json


def get_device_config(filepath):
    with open(filepath, 'r') as f:
        config = json.load(f)
    return config

def save_config(save_filepath, config):
    with open(save_filepath, 'w') as f:
        json.dump(config, f, indent=4)

def get_settings(filepath):
    with open(filepath, 'r') as f:
        raw = f.read()
    result = {}
    for line in raw.split('\n'):
        gpu = line.split('\t')
        result[gpu[0]] = {
            "core": gpu[1],
            "memory": gpu[2],
            "power": gpu[3]
        }
    return result

def configure_device_settings(config, settings):
    for device in config['detected_devices']:
        for key, value in settings.items():
            if key.lower() in device["name"].lower():
                for algo in device["algorithms"]:
                    for power in algo['power']:
                        if power['mode'] == 'high':
                            power['tdp'] = value['power']
                            power['core_clocks'] = value['core']
                            power['memory_clocks'] = value['memory']

def main(base_dir):
    device_file_loc = os.path.join(base_dir, "nhm/configs/device_settings.json")
    device_config = get_device_config(device_file_loc)
    save_config(f'backups/device_settings_{datetime.now().strftime("%Y-%m-%d_%H%M%S")}.json', device_config)

    nh_gpu_settings = get_settings('gpus.config')
    configure_device_settings(device_config, nh_gpu_settings)
    # print(device_config)
    save_config(device_file_loc, device_config)

if __name__ == "__main__":
    base_nh_dir = '/mnt/d'
    main(base_nh_dir)
    # print(get_config('gpus.config'))