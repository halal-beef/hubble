# Hubble - A USB Recovery Tool for devices based on Exynos9830 or Exynos9820

## Why?
 - Why not?
 - I don't want people to be paying to unbrick their devices

## Environment preparation

### Linux

- Run ```bash udev_rules.sh``` as root to setup udev rules
- You can now run the tool.

### Windows

- Uninstall any existing BootROM Drivers
- Import the needed certificates by double clicking the ```## Driver Certificate (INSTALL ME FIRST BEFORE THE DRIVER).reg``` file and importing the regkeys
- Install the ones provided by right clicking the inf and pressing install
- You can now run the tool.

## How to use
 - Install required python packages via ```pip3 install -r requirements.txt```
 - Run the tool, pointing to your bootloader tar file via ```python3 hubble.py -b <PATH_TO_BL_TAR>```
 - Plug in your bricked phone
 - Let it run it's magic
 - Reflash the stock firmware

## Supported devices

 - [ ] Means your device is most likely supported but not tested
 - [x] Means your device is supported and tested

Exynos 9830 Devices:

 - [x] Samsung Galaxy S20 (x1s/lte)
 - [x] Samsung Galaxy S20 Ultra (z3s/lte)
 - [ ] Samsung Galaxy S20+ (y2s/lte)
 - [ ] Samsung Galaxy S20 FE (r8s)
 - [ ] Samsung Galaxy Note20 (c1s/lte)
 - [ ] Samsung Galaxy Note20 Ultra (c2s/lte)

Exynos 9820 Devices:

 - [ ] Samsung Galaxy S10e (beyond0lte)
 - [x] Samsung Galaxy S10 (beyond1lte)
 - [ ] Samsung Galaxy S10+ (beyond2lte)
 - [ ] Samsung Galaxy S10 5G (beyondx)

## Credits
 - [VDavid003](https://github.com/vdavid003) ```Helped me get the BL2 split on the bootloader```
 - [gaitenis](https://xdaforums.com/m/gaitenis.13049039) ```Finding lk.bin split```
 - [halal-beef](https://github.com/halal-beef) ```Initial idea, writing the tool and getting most of the splits```
 - [BotchedRPR](https://github.com/BotchedRPR) ```Loads of support and bricked his S20 Ultra for testing splits, absolute legend```
 - [Robotix](https://github.com/Robotix22) ```Added Exynos 9820 Support, Tested splits on his Galaxy S10```
