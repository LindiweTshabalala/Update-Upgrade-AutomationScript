#!/usr/bin/env python3

import os

def update():
    print("Updating system")
    os.system("sudo apt update")

def upgrade():
    print("Upgrading system")
    os.system("sudo apt upgrade -y")


if __name__ == '__main__':
    update()
    upgrade()