import obsws_python as obs

# Configure your connection settings
# Default host is localhost and default port for v5 is 4455
OBS_HOST = "localhost"
OBS_PORT = 4455
OBS_PASSWORD = ";lkj;lkj71"

def start_obs_recording():
    try:
        # Establish a request client connection to OBS
        cl = obs.ReqClient(host=OBS_HOST, port=OBS_PORT, password=OBS_PASSWORD, timeout=3)
        
        # Send the command to start recording
        cl.start_record()
        print("Successfully sent command: OBS Recording Started!")
        
    except Exception as e:
        print(f"Failed to connect or send command to OBS: {e}")

if __name__ == "__main__":
    start_obs_recording()
