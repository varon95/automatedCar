# Automated mini RC car
The goal of the project is to automate a small RC car

The project consists of 3 parts
- A RC car, with simple 4 button remote (forward, backward, left, right). The car is marked with a green and a blue dot to make tracking the car easy
- An electrical circuit with
  -Four relays, which can turn the four direction button on the remote on and off
  -An Arduino microcontroller, which can communicate with the computer and control the relays
- A webcamera, which is placed abowe the car

## Demo (Video)
[![Mini RC demo](http://img.youtube.com/vi/4yC3YnzzTqE/0.jpg)](http://www.youtube.com/watch?v=4yC3YnzzTqE "")

## Results

In this project I controlled a small (5x3cm) RC car using my computer. And with the help of a camera above the car I managed to do these:
- The car can stay between the chosen boundaries
- The car can navigate randomly
- Or get to a selected point
However, there were several limitations this, since the car did not have precision control (it had only a four button remote) it also had battery problems and there was no point improving it further. [I came back to the idea later](https://github.com/varon95/CSAI_2020_Thesis), when I found that there is a new 1:87 car model with precise analogue controls and long lasting battery.

## Source code
**ArduinoCarControl**: Protocol for the Arduino to control the relays upon recieving commands through the serial port.

**ArduinoCarControlSlow**: Same as **ArduinoCarControl**, but the car is slowed down via turning the main motor on and off repeatedly

**AutomatedCarPython**: Recieves signals from the camera, identifies the blue and green dots on the car, then controlls the car in one of two modes: (1) Drives the car to a selected point on the screen; (2) Drives the car randomly while staying between the cameras' field of view.

**CarControlCSsharp**: Allows the user to control the car through a simple interface.

**carControlPython**: Allows the user to control the car from the computer using the arrow keys.
