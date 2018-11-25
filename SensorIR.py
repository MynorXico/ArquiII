import RPi.GPIO as IO

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(14,IO.IN)

while True:
    if(IO.input(14)==True): # object is far away
    	print("No Obstacle")
    else:
    	print("Obstacle")


