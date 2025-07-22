# The Proxy Pattern provides a placeholder or surrogate for another object to control access to it.

from abc import ABC, abstractmethod

class Internet(ABC):
    @abstractmethod
    def connect_to(self, site: str):
        pass


class RealInternet(Internet):
    def connect_to(self, site: str):
        print(f"Connecting to {site}")


class ProxyInternet(Internet):
    def __init__(self):
        self._real_internet = RealInternet()
        self._banned_sites = ["facebook.com", "instagram.com", "tiktok.com"]

    def connect_to(self, site: str):
        if site.lower() in self._banned_sites:
            raise Exception(f"Access Denied to {site}")
        self._real_internet.connect_to(site)

internet = ProxyInternet()

try:
    internet.connect_to("google.com")
    internet.connect_to("facebook.com")

except Exception as e:
    print(e)