class server:
    def __init__(self, hostname):
        self.hostname = hostname
        self.status = "stopped"
        self.cpu_usage = 0

    def boot(self):
        self.status = "running"

    def shutdown(self):
        self.status = "stopped"
        self.cpu_usage = 0

    def increase_load(self):
        if self.status == "running":
            self.cpu_usage = min(self.cpu_usage + 10, 100)

    def display_status(self):
        print(f"Hostname: {self.hostname}")
        print(f"Status: {self.status}")
        print(f"CPU usage: {self.cpu_usage}%")


my_server = server("server01")
my_server.boot()
my_server.increase_load()
my_server.display_status()
