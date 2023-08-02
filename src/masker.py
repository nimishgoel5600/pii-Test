import hashlib

def mask_pii(data):
    masked_data = data.copy()
    masked_data["masked_device_id"] = hashlib.sha256(masked_data["device_id"].encode()).hexdigest()
    masked_data["masked_ip"] = hashlib.sha256(masked_data["ip"].encode()).hexdigest()
    return masked_data

