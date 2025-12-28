# Hubble - A USB Recovery Tool for Exynos devices

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

## Recovery demo

https://github.com/user-attachments/assets/78ca9dda-04c2-45d3-ad47-5a713086e33e

## Supported Devices

| Symbol | Meaning      |
|:------:|:------------:|
| ✅     | Working     |
| ❌     | Not Working |

### Exynos 9830 Devices

| Name             | Codename | Tested Firmware | Tested by                                             | State |
|:-----------------|:---------|:---------------:|:------------------------------------------------------|:-----:|
| Galaxy S20       | x1s      | `G981BXXSMHXK1` | [halal-beef](https://github.com/halal-beef)           | ✅    |
| Galaxy S20+      | y2s      | `G986BXXSNHYB1` | [Android-Artisan](https://github.com/Android-Artisan) | ✅    |
| Galaxy S20 Ultra | z3s      | `G988BXXSMHXK1` | [BotchedRPR](https://github.com/BotchedRPR)           | ✅    |
| Galaxy S20 FE    | r8s      | `G780FXXUDFWH5` | [Sota4Ever](https://github.com/Sota4Ever)             | ✅    |

### Exynos 9820 Devices

| Name       | Codename   | Tested Firmware | Tested by                               | State |
|:-----------|:-----------|:---------------:|:----------------------------------------|:-----:|
| Galaxy S10 | beyond1lte | `G973FXXSGHWC2` | [Robotix](https://github.com/Robotix22) | ✅    |

### Exynos 9810 Devices

| Name      | Codename   | Tested Firmware | Tested by                               | State |
|:----------|:-----------|:---------------:|:----------------------------------------|:-----:|
| Galaxy S9 | starlte    | `G960FXXUHFVG4` | [Robotix](https://github.com/Robotix22) | ✅    |

### Exynos 7580 Devices

| Name             | Codename   | Tested Firmware | Tested by                                       | State |
|:-----------------|:-----------|:---------------:|:------------------------------------------------|:-----:|
| Galaxy A5 (2016) | a5xelte    | `A510FXXS8CTI7` | [Daniel224455](https://github.com/Daniel224455) | ✅    |

## Credits

Thanks to these people:

[VDavid003](https://github.com/vdavid003) for Helping on the BL2 split for Exynos 9830. <br>
[gaitenis](https://xdaforums.com/m/gaitenis.13049039) found the LK Split for Exynos 9830. <br>
[halal-beef](https://github.com/halal-beef) for finding most of the Exynos 9830 Splits & for the initial Idea. <br>
[Robotix](https://github.com/Robotix22) for adding Support for Exynos 9820, 9810 & 7580. <br>
[alextrack2013](https://github.com/alextrack2013) for adding proper Linux Docs.
