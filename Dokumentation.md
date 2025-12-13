# Catch Your Drink  
**Physical Computing Project**

---

## Concept Description
**Catch Your Drink** is a fast-paced physical computing drinking game built with MicroPython.  
Three pumps are connected to the board, and during the game one of them activates at random. Players must react quickly and catch the liquid with a cup. The goal: fill your cup as much as possible before the timer runs out.

The project uses RGB LEDs to show states (waiting, countdown, running) and buttons to start the game.

---

## How to Play
1. Press **Button A** to start the game.  
2. Hold your cup under the bottles.  
3. One of the three pumps will randomly start pumping liquid.  
4. Catch as much as you can.  
5. The game switches between pumps until the total playtime ends.  
6. When your cup is full, enjoy your drink!

### Interactions
- ModulinoButtons:
  - **Button A** → Starts the game  
  - **Button C** → Runs all Pumpsin order to check if they actually work
- **LED (ModulinoPixels):**  
  - Orange → Waiting  
  - Red countdown animation → Pump switching  
  - Green → Pump cycle completed
  - Orange → Pumps are being tested
- **3 pumps** → for randomized liquid output  

---

## Requirements

### Hardware
- Arduino Nano ESP32 or Modulino board  
- 3x Pumps  
- 3x Tubes  
- 1x ModulinoPixels  
- 1x ModulinoButtons  
- Cups(as many as Pumps)
- USB-C cable  
- Wooden frame / Can be painted to match you Vision  
- Cup holder made from 3D printing  

### Software
- MicroPython  
- Arduino Lab for MicroPython  
- Arduino MicroPython Installer  

### Libraries
- ModulinoPixels  
- ModulinoButtons  

---

## How to Build

### Wiring
- Pumps connected to pins  
- ModulinoPixels connected via Modulino port  
- ModulinoButtons connected via Modulino port  
- Our pumps had to be submerged in water, so place them in the cups, or route your tubes accordingly .  
- Place the cups inside the enclosure and route the tubes through the enclosure.

### Uploading the Code
1. Open **Arduino Lab for MicroPython** and connect your board via USB-C.  
2. Copy the provided code to Arduino Lab for MicroPython and check if the Pins are corectly configured. We recommend you testing them first before assembling – all libraries are already included, so your only worry should be the Pins to the pumps.
3. After you are sure everything works, load the code onto the board. It should be called main.py
3. Restart the board — the game will start after pressing **Button A**. 