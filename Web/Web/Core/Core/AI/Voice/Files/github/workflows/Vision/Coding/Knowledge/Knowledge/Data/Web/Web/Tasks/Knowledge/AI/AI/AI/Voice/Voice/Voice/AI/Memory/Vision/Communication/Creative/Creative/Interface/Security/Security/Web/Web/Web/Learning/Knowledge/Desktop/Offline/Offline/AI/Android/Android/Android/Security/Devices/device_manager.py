class DeviceManager:


    def __init__(self):

        self.devices=[]



    def register(self,device):

        self.devices.append(device)



    def send_command(self,device,command):

        return (
            "Sending "
            + command
            + " to "
            + device
        )
