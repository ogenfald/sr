#!/usr/bin/python3

#  ____                  ____            _ _           _
# / ___| _   _ ___      |  _ \ ___ _ __ | (_) ___ __ _| |_ ___  _ __
# \___ \| | | / __|_____| |_) / _ \ '_ \| | |/ __/ _` | __/ _ \| '__|
#  ___) | |_| \__ \_____|  _ <  __/ |_) | | | (_| (_| | || (_) | |
# |____/ \__, |___/     |_| \_\___| .__/|_|_|\___\__,_|\__\___/|_|
#        |___/                    |_|

# Sys-Replicator V1 2019-06-19
# Ben Joyner

import os
import argparse

class parseArguments():
    parser = argparse.ArgumentParser(description='A simple system replicator to backup/restore dotfiles')
    parser.add_argument('-b', '--backup', action='store_true', help='Backup ~/.config/')
    parser.add_argument('-r', '--restore', action='store_true', help='Restore dotfiles to ~/.config/')
    parser.add_argument('-v', '--verbose', action='store_true', help='Copy files with extra verbosity')
    parser.add_argument('-l', '--list', action='store_true', help='List the contents of ~/.config/')
    parser.add_argument('-a', '--all', action='store_true', help='Include dotfiles outside of ~/.config/')
    args = parser.parse_args()

def backup():
    print('Creating dotfiles backup')
    if p.args.verbose:
        if p.args.all:
            os.system('mkdir -p ~/dotfiles && cp -vr ~/.* ~/dotfiles')
        else:
            os.system('mkdir -p ~/dotfiles && cp -vr ~/.config/* ~/dotfiles/')
    elif p.args.all:
        os.system('mkdir -p ~/dotfiles && cp -r ~/.* ~/dotfiles/')
    else:
        os.system('mkdir -p ~/dotfiles && cp -r ~/.config/* ~/dotfiles/')

def restore():
    print('Restoring dotfiles to ~/.config')
    if p.args.verbose:
        if p.args.all:
            os.system('cp -vr ~/dotfiles/* ~/')
        else:
            os.system('cp -vr ~/dotfiles/* ~/.config')
    elif p.args.all:
        os.system('cp -r ~/dotfiles/* ~/')
    else:
        os.system('cp -r ~/dotfiles/* ~/.config')

def list():
    if p.args.all:
        os.system('ls -a ~/')
    else:
        os.system('ls ~/.config')

def main():
    if p.args.backup:
        backup()
    elif p.args.restore:
        restore()
    elif p.args.list:
        list()
    else:
        p.parser.print_help()

p = parseArguments()

if __name__ == '__main__':
    main()
