import time
import random
from machine import Pin
from modulino import ModulinoPixels, ModulinoButtons

# ---------------------------------------------------------
# Define pump-pins (here example-pins)
# ---------------------------------------------------------
pumps = {
    "Pump 1": Pin(1, Pin.OUT),
    "Pump 2": Pin(2, Pin.OUT),
    "Pump 3": Pin(3, Pin.OUT)
}

pump_names = list(pumps.keys())   # ["Pump 1", "Pump 2", "Pump 3"]

# ---------------------------------------------------------
# Functions for pumps
# ---------------------------------------------------------
def pump_on(name):
  pumps[name].value(1)
  print(f"{name} ON")

def pump_off(name):
  pumps[name].value(0)
  print(f"{name} OFF")


# ---------------------------------------------------------
# Variables used
# ---------------------------------------------------------
current_pump = -1
pump_start = 0
pump_duration = 0

pixels = ModulinoPixels()
buttons = ModulinoButtons()

pixel_count = 8

MIN_RUN = 1     # seconds
MAX_RUN = 3     # seconds

runtime = 30    # seconds

# ---------------------------------------------------------
# Functions Buttons
# ---------------------------------------------------------

def wait_for_start():
    print("Bereit. Druecke Button A zum Starten...")
    
    while True:
        # Modulino Buttons aktualisieren
        buttons.update()
        
        # Prüfen ob der erste Button (Index 0) gedrückt ist
        if buttons.is_pressed(0):
          print("Button gedrueckt! Los geht's!")
          pumping_running = True
          return # Verlässt die Warte-Funktion und lässt das Programm weiterlaufen

# ---------------------------------------------------------
# Funcitons Pumps
# ---------------------------------------------------------

def start_random_pump():
    global current_pump, pump_start, pump_duration

    new_pump = current_pump
    while new_pump == current_pump:
      new_pump = random.choice(pump_names)

    current_pump = new_pump
    pump_duration = random.uniform(MIN_RUN, MAX_RUN)
    pump_start = time.ticks_ms()

    pump_on(current_pump)
    print(f"START → {current_pump} for {pump_duration:.2f} seconds")

def stop_current_pump():
    global current_pump
    pump_off(current_pump)
    print(f"STOP → {current_pump}")
    current_pump = None
  
    pixels.clear_all()
    pixels.show()

# ---------------------------------------------------------
# Functions pixels
# ---------------------------------------------------------

def pixels_countdown(time_to_full=1):
  pixels.clear_all()
  pixels.show()
  
  delay = time_to_full / pixel_count
  for i in range(pixel_count):
    pixels.set_rgb(i, 255, 0, 0)
    pixels.show()
    time.sleep(delay)
  
  pixels.set_all_rgb(0, 255, 0, 10)
  pixels.show()

def pixels_waiting():
  for i in range(pixel_count):
    pixels.set_all_rgb(255, 165, 0, 10)
  pixels.show()

# ---------------------------------------------------------
# Start
# ---------------------------------------------------------
while True:
  pixels_waiting()
  wait_for_start()
  
  start_random_pump()
  
  time_started = time.ticks_ms()
  countdown_seconds = 1

# ---------------------------------------------------------
# Mainloop
# ---------------------------------------------------------
  pumping_running = True
  while pumping_running:
    now = time.ticks_ms()
  
    if time.ticks_diff(now, pump_start) >= pump_duration * 1000:
      stop_current_pump()
      pixels_countdown(countdown_seconds)
      start_random_pump()
  
    time.sleep(0.05)  # relive CPU
  
    if time.ticks_diff(now, time_started) >= runtime * 1000:
      stop_current_pump()
      pixels.clear_all() # Turn off all pixels
      pixels.show() # Update the pixels to show changes
      pumping_running = False
      print("Pumping stopped")
