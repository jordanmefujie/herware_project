#!/usr/bin/python3

import time
import random


class Herware:
    def __init__(self):
        self.name = "Herware Device"
        self.status = "Idle"

    def start_process(self, process_name):
        """Start a process on the hardware device."""
        self.status = "Processing"
        time.sleep(random.randint(1, 5))  # Simulate processing time
        self.status = "Idle"
        return f"{process_name} completed"

    def stop_process(self):
        """Stop the current process on the hardware device."""
        self.status = "Idle"

    def get_status(self):
        """Get the current status of the hardware device."""
        return self.status


class EnhancedHerware(Herware):
    def __init__(self):
        super().__init__()
        self.process_log = []

    def start_process(self, process_name):
        """Start a process on the hardware device and log the process."""
        self.process_log.append(f"{process_name} started")
        return super().start_process(process_name)

    def stop_process(self):
        """Stop the current process on the hardware and log the process."""
        self.process_log.append("Process stopped")
        return super().stop_process()

    def get_process_log(self):
        """Get the process log from the hardware device."""
        return self.process_log


class AdvancedHerware(EnhancedHerware):

    def __init__(self):
        super().__init__()
        self.settings = {"process_timeout": 10}

    def start_process(self, process_name):
        """Start a process on the hardware device with timeout settings."""
        if self.status == "Processing" and time.time(
        ) < self.settings["process_timeout"]:
            return "Processing in progress, please wait"
        return super().start_process(process_name)
