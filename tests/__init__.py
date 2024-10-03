# SPDX-FileCopyrightText: 2024-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT
import time

import src.pygamedebugscreen as pds
import pygame

pygame.init()

dw = pds.DebugWindow((200, 150), font_size=10)

w = 0

dw.add_text("some debug value: ", lambda: w)
dw.add_text("secondary debug value: ", lambda: w**2)

f = lambda: w

dw.start(delay=0.1)

other_window = pygame.display.set_mode((800, 800))

while True:
    w += 1

    time.sleep(0.1)

