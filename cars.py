class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >0:
            self.speed -= 5

    def step(self):
       self.odometer += self.speed
       self.time += 1

    def average_speed(self):
        return self.odometer / self.time


if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                        "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
            print("Accelerating...")
        elif action == 'B':
            my_car.brake()
            print("Braking...")
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()

## Part A: run the program and see the bug (run in terminal A,B,B,0)
# this is what the function is doing and therefore that's why the running A,B,B,O did not make sense‹
# A	0 + 5 = 5	0 + 5	5 ✅
# B	5 − 5 = 0	5 + 0	5 ✅
# B	0 − 5 = −5 ❌	5 + (−5)	0 ❌
# O	shows the odometer


## Step 1: set up the debugger (launch.json created and saved)
# Step 2: breakpoint on line 15 with the red dot

# Step 3: add self.odometer and self.speed to Watch
    # Click +, type self.odometer, and press Enter.
    # Click + again, type self.speed, and press Enter.
# Now both the variables (odometer and speed) are in the watch litst

# Step 4: Press the green “Play” button in the Run and Debug pane. 
# This will start the script.

# Step 5: 
# Ask a question in the terminal, type A

# Step 6

# Step 7
# Watch the odometer in the Watch panel go back 5

# Steps 8–13: watch the bug happen

# Step 14: the fix
# Change lines 11 and 12 to
# 11  def brake(self):
# 12      self.speed -= 5

# Step 15: Test

