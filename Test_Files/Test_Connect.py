from python_obs.clients import OBS


obs = OBS(host="localhost", port=4455, password="password")
obs.connect()

#print("Connected!")