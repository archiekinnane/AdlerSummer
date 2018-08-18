# Tutorial

### What This Does
This package will take whatever phrase you like and represent it as a series of points in a RenderableBillboardsCloud renderable in OpenSpace. Your text will appear on a sphere of radius 1 Mpc.

### How It Works

After import,
```
from textOps import alphabet
```
the relevant function is called spellTime. It requires two variables to be initialized: the phrase you want to write and what you want your speck and asset files to be called. It has several more optional variables you can initialize, such as the first letter's position in RA and Dec, the letter width, and the letter height. If you don't provide these values they will be set at the defaults. If you want a reminder of the arguments, run
```
alphabet.printArgs()
```
which will return:
```
alphabet.spellTime(phrase, filename, topleft_word_ra = 40, letterwidth = 6, topleft_word_dec = 45, letterheight = 4)
```
Once you run this function, the speck and asset file that will display your text will be saved in your current directory ... IF

### What It Needs

IF you have my other package, files2ops, installed on your machine. This package uses that module to make the relevant files.
