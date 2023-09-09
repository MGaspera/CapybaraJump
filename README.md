# Capybara Platformer
A simple platformer made for a school project using pygame 2.5.1 and python 3.11.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Required Libraries](#required-libraries)
- [Assets](#assets)

## Introduction
A very simple game that I'm making at the very beginning of my computer science A-level.

## Getting Started

To get started with Capybara Platformer, follow these steps:

1. Clone or download this repository to your local machine.

2. Ensure you have Python 3.11.5 or a compatible version installed. You can download Python from the official website [python.org](https://www.python.org/).

3. Install the required libraries, including Pygame and os. You can use the following commands to install them:

    ```bash
    pip install -U pygame --user
    pip install os-sys
    ```

4. Once the libraries are installed, you can run the game using Python. Navigate to the project directory and execute the following command:

    ```bash
    python main.py
    ```

## Required Libraries <br>
***Pygame*** <br>
(installation instructions from https://www.pygame.org/wiki/GettingStarted)  <br>   Pygame requires Python; if you don't already have it, you can download it from python.org. It's recommended to run the latest python version, because it's usually faster and has better features than the older ones. Bear in mind that pygame has dropped support for python 2.

The best way to install pygame is with the pip tool (which is what python uses to install packages). Note, this comes with python in recent versions. We use the --user flag to tell it to install into the home directory, rather than globally.

``` python3 -m pip install -U pygame --user``` 

To see if it works, run one of the included examples:

``` python3 -m pygame.examples.aliens``` 

***os*** <br>
os allows us to search through various directories. Currently, it's being used to locate the "images" folder, which stores all the sprites and the background. it should be installed by default with python, but incase it isn't, install using the following command taken from https://pypi.org/project/os-sys/:

```pip install os-sys```


## Assets <br>
***Background*** <br>
"STARSTRING FIELDS" by trixelized on Itch.io: https://trixelized.itch.io/starstring-fields <br>

***Player Sprite*** <br>
"Charlie the Capybara by niffirgGames on itch.io: https://niffirggames.itch.io/charliethecapybara
