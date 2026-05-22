class SystemController:
    def __init__(self):
        self.system_status = "OFF"

    def start_system(self):
        self.system_status = "ON"
        print("System started successfully")

    def stop_system(self):
        self.system_status = "OFF"
        print("System stopped successfully")

controller = SystemController()

controller.start_system()
controller.stop_system()