#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import commands
arq = open('wordlist.txt', 'r')
texto = arq.readlines()
for linha in texto :
    argumento = linha.strip()
    os.system("python brainwallet-check.py '" + argumento + "'")
arq.close()


