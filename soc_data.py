EXYNOS_DATA = {
    "Exynos9830\0": {
        "response_support": True,
        "files_to_extract_from_tar": ["sboot.bin.lz4", "ldfw.img.lz4", "tzsw.img.lz4"],
        "lz4_files_to_extract": ["sboot.bin.lz4"],
        "files_to_send": ["ldfw.img.lz4", "tzsw.img.lz4"],
        "bootloader_splits": {
            "fwbl1.img": {
                "start": 0x0,
                "end": 0x3000,
            },
            "epbl.img": {
                "start": 0x3000,
                "end": 0x16000,
            },
            "bl2.img": {
                "start": 0x16000,
                "end": 0x82000,
            },
            "lk.bin": {
                "start": 0xDB000,
                "end": 0x35B000,
            },
            "el3_mon.img": {
                "start": 0x35B000,
                "end": 0x39B000,
            }
        }
    },

    "Exynos9820\0": {
        "response_support": True,
        "files_to_extract_from_tar": ["sboot.bin.lz4"],
        "lz4_files_to_extract": ["sboot.bin.lz4"],
        "files_to_send": [],
        "bootloader_splits": {
            "epbl.img": {
                "start": 0x0,
                "end": 0x3000,
            },
            "fwbl1.img": {
                "start": 0x3000,
                "end": 0x16000,
            },
            "bl2.img": {
                "start": 0x16000,
                "end": 0x68000,
            },
            "u-boot.bin": {
                "start": 0xA4000,
                "end": 0x224000,
            },
            "el3_mon.img": {
                "start": 0x224000,
                "end": 0x264000,
            }
        }
    },

    "Exynos9810\0": {
        "response_support": False,
        "files_to_extract_from_tar": ["sboot.bin.lz4"],
        "lz4_files_to_extract": ["sboot.bin.lz4"],
        "files_to_send": [],
        "bootloader_splits": {
            "epbl.img": {
                "start": 0x0,
                "end": 0x2000,
            },
            "fwbl1.img": {
                "start": 0x2000,
                "end": 0x15000,
            },
            "bl2.img": {
                "start": 0x15000,
                "end": 0x64000,
            },
            # Repeat to allow the authentication and load of further images.
            "epbl.img": {
                "start": 0x0,
                "end": 0x2000,
            },
            "u-boot.bin": {
                "start": 0x7D000,
                "end": 0x1FD000,
            },
            "el3_mon.img": {
                "start": 0x1FD000,
                "end": 0x23D000,
            }
        }
    },

    "Exynos7580\0": {
        "response_support": False,
        "files_to_extract_from_tar": ["sboot.bin.lz4"],
        "lz4_files_to_extract": ["sboot.bin.lz4"],
        "files_to_send": [],
        "bootloader_splits": {
            "epbl.img": {
                "start": 0x0,
                "end": 0x2000,
            },
            "fwbl1.img": {
                "start": 0x2000,
                "end": 0x32000,
            },
            "bl2.img": {
                "start": 0x32000,
                "end": 0x3A000,
            },
            "u-boot.bin": {
                "start": 0x3A000,
                "end": 0x10B000,
            }
        }
    }
}
