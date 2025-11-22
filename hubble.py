import usb.core
import usb.util
import usb.backend.libusb1
import libusb
import tarfile
import lz4.frame
import argparse
import struct
import sys
import os
import coloredlogs
import logging
from time import sleep

from soc_data import EXYNOS_DATA

soc     = ""
logger  = logging.getLogger(__name__)
verbose = False

def write_u32(value):
    return struct.pack('<I', value)

def write_header(data, size):
    data[4:8] = write_u32(size)

def load_file(file_input):
    try:
        if isinstance(file_input, str):  # If input is a filename
            with open(file_input, 'rb') as file:
                file_data = file.read()
        elif isinstance(file_input, bytes):  # If input is raw bytes
            file_data = file_input
        else:
            raise TypeError("Invalid file input type. Must be filename (str) or raw data (bytes).")

        size = len(file_data) + 10
        block = bytearray(size)
        block[8:8+len(file_data)] = file_data

        return block
    except Exception as e:
        logger.critical(f"Error loading file: {e}")
        return None

def calculate_checksum(data):
    checksum = sum(data[8:-2]) & 0xFFFF
    logger.warning(f"=> Data checksum {checksum:04X}")
    data[-2:] = struct.pack('<H', checksum)

def find_device():
    usb_backend = None
    device_connection_attempts = 0

    if os.name == "nt":
        usb_backend = usb.backend.libusb1.get_backend(find_library=lambda x: libusb.dll._name)

    while True:
        device = usb.core.find(idVendor=0x04e8, idProduct=0x1234, backend=usb_backend)

        if device is None:
            if device_connection_attempts == 15:
                device_connection_attempts = 0

                print()
                logger.debug(f"Tip: Plug in your device with the power button pressed.")

            print(".", end="", flush=True)
            device_connection_attempts += 1
            sleep(1)
        else:
            print()
            return device

def send_part_to_device(device, file, filename):
    file_size = len(file)

    logger.warning(f"=> Downloading {file_size} bytes")

    write_header(file, file_size)
    calculate_checksum(file)

    ret = device.write(2, file, timeout=50000)

    if EXYNOS_DATA[soc]["response_support"] == True and verbose == True:
        while True:
            try:
                data = device.read(0x81, 512, timeout=1000)

                byte_str = ''.join(chr(n) for n in data[0:])
                response = byte_str.split('\x00',1)[0]

                if len(response) != 0:
                    logger.debug(f"=> Device Response: {response}")
            except:
                break

    if ret == file_size:
        logger.info(f"=> {ret} bytes written.")
    else:
        logger.critical(f"=> {ret} bytes written.")
        logger.critical(f"Failed to write {file_size} bytes")
        sys.exit(-1)

    print()

def filter_tar(tarinfo, unused):
    if tarinfo.name in EXYNOS_DATA[soc]["files_to_extract_from_tar"]:
        logger.warning(f"Extracted: {tarinfo.name}")
        return tarinfo

    return None

def extract_bl_tar(path):
    with tarfile.open(path, 'r') as tar:
        try:
            tar.extractall(path='.', members=tar.getmembers(), filter=filter_tar)
        except:
            logger.critical("Failure in extracting BL tar! Bailing!")
            sys.exit(-1)

    tar.close()

    for resultant_bin in EXYNOS_DATA[soc]["lz4_files_to_extract"]:
        with open(resultant_bin, 'rb') as input_lz4:
            try:
                filename_no_lz4 = os.path.splitext(resultant_bin)[0]

                with open(filename_no_lz4, 'wb') as output_bin:
                    output_bin.write(lz4.frame.decompress(input_lz4.read()))

                    output_bin.close()

                logger.warning(f"Extracted: {filename_no_lz4}")
            except:
                logger.critical("Failure in extracting LZ4 archives! Bailing!")
                sys.exit(-1)

        input_lz4.close()

        try:
            delete_file(resultant_bin)
        except:
            logger.critical("Failure in preliminary cleanup! Bailing!")
            sys.exit(-1)

    print()

def delete_file(filename):
    os.remove(filename)
    logger.warning(f"Deleted: {filename}")

def display_and_verify_device_info(device):
    global soc

    device_config = device.get_active_configuration()

    soc = usb.util.get_string(device, device.iProduct)
    usb_serial_num = usb.util.get_string(device, device.iSerialNumber)
    usb_booting_version = usb.util.get_string(device, device_config[(0, 0)].iInterface)

    print()
    logger.debug(f"==================== Device Information ====================")
    logger.info(f"SoC: {soc}".center(60))
    logger.info(f"SoC ID: {usb_serial_num[0:15]}".center(60))
    logger.info(f"Chip ID: {usb_serial_num[15:31]}".center(60))
    logger.info(f"USB Booting Version: {usb_booting_version[12:16]}".center(60))
    print()

    for soc_name in EXYNOS_DATA.keys():
        if soc == soc_name:
            return

    logger.critical("This SoC is not Supported!")
    sys.exit(-1)

def main():
    global verbose

    coloredlogs.install(
        level="DEBUG",
        fmt="%(asctime)s %(message)s",
        level_styles={
            'debug': {'color': 'magenta'},
            'info': {'color': 'green'},
            'warning': {'color': 'white', 'bold': True},
            'error': {'color': 'yellow', 'bold': True},
            'critical': {'color': 'red', 'bold': True},
        },
        field_styles={
            'asctime': {'color': 'blue'},
            'levelname': {'bold': True},
        }
    )

    logger.debug(r"""
  _    _ _    _ ____  ____  _      ______
 | |  | | |  | |  _ \|  _ \| |    |  ____|
 | |__| | |  | | |_) | |_) | |    | |__
 |  __  | |  | |  _ <|  _ <| |    |  __|
 | |  | | |__| | |_) | |_) | |____| |____
 |_|  |_|\____/|____/|____/|______|______|
    """)

    print("USB Recovery Tool")
    print("Version 1.0 (c) 2025 Umer Uddin <umer.uddin@mentallysanemainliners.org>")
    print()
    logger.error("Notice: This program and it's source code is licensed under GPL 2.0.")
    logger.error("Notice: If you have paid for this, you have been scammed!")
    logger.error("Please issue a refund and get the official program from")
    logger.info("https://github.com/halal-beef/hubble")
    print()

    parser = argparse.ArgumentParser(description="USB Recovery Tool for Exynos devices.")
    parser.add_argument('-b', '--bl-tar', type=str, help="Path to the .tar or .tar.md5 file", required=True)
    parser.add_argument('-v', '--verbose', action="store_true", help="Enables more Logs during Operation")

    args = parser.parse_args()

    if args.bl_tar:
        if os.path.isfile(args.bl_tar):
            logger.warning(f"Using file: {args.bl_tar}")
        else:
            logger.critical(f"Error: The file {args.bl_tar} does not exist or is not a valid file.")
            sys.exit(-1)

    if args.verbose:
        verbose = True

    logger.warning("Waiting for device")
    device = find_device()
    logger.warning("Found device.")

    display_and_verify_device_info(device)

    logger.warning("Extracting files...")
    extract_bl_tar(args.bl_tar)

    logger.warning(f"Starting USB booting...")
    print()

    if os.name != "nt":
        if device.is_kernel_driver_active(0):
            device.detach_kernel_driver(0)

    usb.util.claim_interface(device, 0)

    with open("sboot.bin", "rb") as sboot:
        for img_name, split_params in EXYNOS_DATA[soc]["bootloader_splits"].items():
            try:
                logger.debug(f"Sending file part {img_name} (0x{split_params["start"]:X} - 0x{split_params["end"]:X})...")

                sboot.seek(split_params["start"])
                sboot_section = load_file(sboot.read(split_params["end"] - split_params["start"]))

                if sboot_section is None:
                    logger.critical(f"Failed to load {img_name}")
                    sys.exit(-1)

                send_part_to_device(device, sboot_section, img_name)
            except Exception as e:
                logger.critical(f"Error when trying to process sboot.bin! ({e})")
                sys.exit(-1)

        sboot.close()

    for file_to_send in EXYNOS_DATA[soc]["files_to_send"]:
        logger.debug(f"Uploading file {file_to_send}...")

        file_data = load_file(file_to_send)

        if file_data is None:
            logger.critical(f"Failed to load {file_to_send}")
            sys.exit(-1)

        send_part_to_device(device, file_data, file_to_send)

    usb.util.release_interface(device, 0)
    usb.util.dispose_resources(device)

    logger.warning("Cleaning up...")
    print()

    try:
        for file in EXYNOS_DATA[soc]["lz4_files_to_extract"]:
            filename_no_lz4 = os.path.splitext(file)[0]
            delete_file(filename_no_lz4)

        for file in EXYNOS_DATA[soc]["files_to_send"]:
            delete_file(file)
    except:
        logger.critical("Failure in cleaning up! Bailing!")
        sys.exit(-1)

    print()
    logger.error("You should be in download mode now, please reflash the stock firmware as the bootloader will still be wiped.")

if __name__ == "__main__":
    main()
