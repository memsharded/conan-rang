from conans import ConanFile, tools
import os


class RangConan(ConanFile):
    name = "rang"
    version = "1.0"
    license = "Public domain"
    url = "https://github.com/memsharded/conan-rang"
    build_policy="missing"

    def source(self):
        self.run("git clone https://github.com/agauniyal/rang")
        self.run("cd rang && git checkout v1.0")

    def package(self):
        self.copy("*.h*", "include", "rang/include")
