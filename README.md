# Requirements:
1. [Micro:bit](https://www.microbit.co.uk/)
2. usb cable
3. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
4. [python](https://www.python.org/downloads/)

# Download and preparation:
1. Clone the repository
2. Use the command `make install`

It will create a new virtual environment and install [microFS](https://microfs.readthedocs.io/en/latest/)

# How to copy the files:
1. Connect your micro:bit by usb
2. In the terminal, use the command `make`. It will copy all files in the micro:bit

You should have privilege to copy files in micro:bit.

you have two options:
- Using root to copy the files.
- Adding your user in the group dialout.

# Controllers:

## Menu:
- **Button a and b:** Those are used to move you between applications.
- **tilt your micro:bit forward:** It will start the application that you have chosen.

## Lantern:
Lantern is the letter **L** in the menu
- **Button a and b**: Those are used to add more intensity on every led or less intensity

## Paint:
Paint is the letter **P** in the menu
- **Button a**: To move you to right
- **Button b**: To move you to bottom
- **tilt your micro:bit forward(a lot):** It let you paint or remove a led.
