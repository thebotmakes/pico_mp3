# pico_mp3

## Code for getting a DFPlayer mini to work with a raspberry pi pico

This largely uses the library detailed here:  https://github.com/lavron/micropython-dfplayermini

Connections are:

* Pico                 DFPlayer Mini
* GP0 / UART TX        2 / RX
* GP1 / UART RX        3 / TX
* GP36 / 3V3OUT        1 / VCC
* GP23 / GND           7 / GND         (note - this can be any ground on pico / either of the grounds on DFPlayer)


Then pins 4 / 5 on DFPLayer go to left / right on outputs (I'm connecting up to amplifier via an audio jack) and 10 to ground on jack.

Audio files are saved to the micro SD card with names like 0001.mp3 / 0002.mp3 (as in exactly this format - 4 numbers with the leading zeroes).  Apparently you can then add text after the numbers, but I haven't tried this.  The numbering defines the playing order.
