
![](https://github.com/Staf707/Donut/blob/main/cube.gif)
<h1>3D Ascii Rendering In Python (Using Pygame)</h1>
A lightweight pygame engine, using pygame, to simulate a spinning in ascii characters.<br>
Learn about rotation matrices, 3D rendering, lumination and much more!
<h2>✅ Features</h2>
<ul>
  <li>3D Projection: Simulates 3D rendering using 2D transformations.</li>
  <li>Customizable: Easily tweak the cube's size, speed, and colors.</li>
  <li>Real-Time Rotation: The cube spins around its axes.</li>
  <li>Lighting Effects: Includes natural lighting simulation with dot products and plane vectors.</li>
</ul>
<h2>🧩 Repository Structure</h2>
Donut/<br>
<ul>
  <li>cube.py: Main script, spinning cube</li>
  <li>donut.py: Side script, spinning Donut, used as reference</li>
  <li>README.md: project overview</li>
</ul>


<h2>🛠️ Installation and Setup</h2>
<b>1. Clone The Repository</b>

```cmd
git clone https://github.com/Staf707/Donut.git
cd Donut
```
<b>2. Install Dependencies Ensure you have Python 3.x installed, then install Pygame:</b>
```cmd
pip install pygame
```
<b>3. Run The script</b>
```cmd
python cube.py
```

<h2>📖 How It Works</h2>
<h3>1. 3D to 2D projection</h3>
The cube's vertices are transformed and projected onto a 2D screen using the following:
<ul>
  <li>Rotation Matrices: Rotate the cube around its X, Y, and Z axes.</li>
  <li>Perspective Projection: Maps 3D coordinates into 2D space.</li>
</ul>
for more information about this topic, I like to refer to this website: https://www.a1k0n.net/2011/07/20/donut-math.html 
<h3>2. Shading and Lighting</h3>
<ul>
  <li>Natural lighting is simulated using vector dot products to determine luminance.</li>
  <li>ASCII characters (" .,-~:;=!*#$@") are used to represent varying levels of brightness.</li>
</ul>
<h3>3. Pixel Grid Rendering</h3>
<ul><li>The display is divided into a grid, and ASCII characters are drawn on each pixel based on the cube's projection.</li></ul>


<h2>🎮 Controls</h2>
<ul><li>Pause/Resume Rotation: Press any key to toggle the rotation of the cube.</li></ul>

<h2>🧑‍💻 Customization</h2>
<ul>
  <li>Lighting: Toggle natural lighting with the natural_light variable in the script.</li>
  <li>Color Mode: Set colour = False for a white cube or True for dynamic colors.</li>
  <li>Cube Size and Rotation: Modify the cube's dimensions and rotation speeds in the while running loop.</li>
</ul>
<h2>👨‍💻 Code Overview</h2>
<h3>1. Initializing everything</h3>
<h4>1. Importing all depenencies</h4>

```python
import os
import pygame
from math import cos, sin, tan, radians, pi, sqrt, acos, degrees
import time
```

<h4>2. Assigning the needed colours</h4>

```python
WHITE = (255,255,255)
BLACK = (0,0,0)

```

<h4>3. The Window</h4>
We make sure the window is in the middle of the screen. In this example, I'm choosing a resolution of 800x800 but you can change this if you want to, same as the FPS.

```python
os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 800, 800
FPS = 60
```

<h4>4. Pixels</h4>
We choose for a pixel width and height of 20, this means each charachter ( we call it pixel) is 20x20.
The 'x_pixel' and 'y_pixel' is later used when we are going to loop over all the characters.

```python
pixel_width = 20
pixel_height = 20

x_pixel = 0
y_pixel = 0
```


```python
screen_width = WIDTH // pixel_width # 40
screen_height = HEIGHT // pixel_height # 40
screen_size = screen_width * screen_height
```
screen_width/screen_height = how many characters there are in the width and height
<br>
size = how many chars their are in total on screen. (base x height)

<h4>5. Other</h4>

```python
FOV = 5
FOV_rad = radians(FOV)
```
Here, you can choose your FOV, this is mesured in degrees and transfered in radians.

```python
K2 = 70
spacing = 1
```

<h2>📟 Author</h2>
Developed by Staf707.
Feel free to reach out for collaboration or questions!
<h2></h2>
<br>
Let me know if you'd like to include any additional details or further enhancements!




```python
```
