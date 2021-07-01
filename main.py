# -*- coding: utf-8 -*-
""""""
"""
Created on Sat Jun 26 00:10:56 2021

@author: Nicolas Striebig
"""

from modules.nexysio import Nexysio
from modules.asic import Asic
from modules.voltageboard import Voltageboard
from modules.injectionboard import Injectionboard


def main():
    nexys = Nexysio()

    # Open FTDI Device with Index 0
    handle = nexys.open_device(0)

    # Write 0x55 to register 0x09 and read it back
    nexys.write_register(0x09, 0x55, True)
    nexys.read_register(0x09)

    #
    # Write Asicconfig
    #

    # Generate pattern for asicSR
    asic = Asic(handle)
    asic.update_asic()

    #
    # Configure Voltageboard
    #

    # Configure Voltageboard in Slot 4 with list values
    # Set measured 1V for one-point calibration
    vboard1 = Voltageboard(handle, 4, (8, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]))
    vboard1.vcal = 0.989
    vboard1.update_vb()

    #vboard1.dacvalues = (8, [1.2, 1, 1])
    vboard1.update_vb()
    vboard1.update_vb()

    #    # Injection
    #

    # Set Injection level
    injvoltage = Voltageboard(handle, 5, (2, [1, 1]))
    injvoltage.vcal = 0.989
    injvoltage.update_vb()

    inj = Injectionboard(handle)

    # Set Injection Params 330MHz clock
    inj.period = 100
    inj.clkdiv = 300
    inj.initdelay = 100
    inj.cycle = 0
    inj.pulsesperset = 1

    # Start injection
    #inj.start()

    # Close connection
    nexys.close()


if __name__ == "__main__":

    main()
