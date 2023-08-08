# Setting Up Thonny IDE and MicroPython on Raspberry Pi Pico

This guide provides step-by-step instructions to download and set up the Thonny IDE on your PC, as well as how to download the MicroPython UF2 file and load it onto a Raspberry Pi Pico board.

## Installing Thonny IDE

1. Visit the Thonny IDE website: [https://thonny.org/](https://thonny.org/)
2. Download the appropriate version for your operating system (Windows, macOS, Linux).
3. Follow the installation instructions provided for your operating system.
4. Launch Thonny IDE after installation.

## Downloading MicroPython UF2 File

1. Visit the official MicroPython website: [https://micropython.org/](https://micropython.org/)
2. Navigate to the "Download" section or directly to the MicroPython GitHub releases page: [https://github.com/micropython/micropython/releases](https://github.com/micropython/micropython/releases)
3. Look for the MicroPython UF2 release corresponding to your Raspberry Pi Pico board version (e.g., pico_v1.1, pico_v1.2).
4. Download the appropriate UF2 file for your board.

## Flashing MicroPython onto Raspberry Pi Pico

1. Connect your Raspberry Pi Pico to your computer using a USB cable.
2. Press and hold the BOOTSEL button on the Raspberry Pi Pico.
3. While holding the BOOTSEL button, press and release the RST (Reset) button.
4. Release the BOOTSEL button. This puts the Pico into bootloader mode.
5. Your computer should recognize the Raspberry Pi Pico as a removable drive named "RPI-RP2."
6. Drag and drop the downloaded MicroPython UF2 file onto the "RPI-RP2" drive.
7. The UF2 file will be copied to the board, and the Pico will restart automatically.

## Testing MicroPython on Raspberry Pi Pico

1. After flashing MicroPython, the Pico will reboot.
2. Open Thonny IDE on your PC.
3. Go to the "Tools" menu and select "Options."
4. Under the "Interpreter" section, select "MicroPython (Raspberry Pi Pico)" from the drop-down menu.
5. Click "OK" to save the settings.
6. Write your MicroPython code in Thonny IDE.
7. Click the "Run" button (green arrow) to execute your code on the Raspberry Pi Pico.

## Additional Resources

- [Thonny Documentation](https://thonny.org/doc/index.html)
- [MicroPython Documentation](https://docs.micropython.org/en/latest/)
- [Raspberry Pi Pico Getting Started Guide](https://www.raspberrypi.org/documentation/pico/getting-started/)

Happy coding!
