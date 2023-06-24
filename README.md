# Turtle Crossing :pickup_truck:	🐢 :pickup_truck: :pickup_truck: :pickup_truck: :pickup_truck:
Python 100 Days of Code: Day 23

Stream-of-conscious thoughts and questions while building: 
* Might be a good idea to spawn the cars and place them at random x and y co-ordinates just off-screen
* Once cars have made it to the left end of the screen, resend them to the right end (the illusion of a respawn) to save memory
* Otherwise, we're just spawning cars and not killing them
* Get it to work quick and dirty and then improve upon performance because it is going to be hard to optimize for performance from the get-go

Overall post-development thoughts: 
* Tweaking game mechanics is fun:
  * Control how many cars are on screen at any point to tweak difficulty
  * Spawns the cars randomly off-screen over an area exactly the size of the visible game area so the cars are evenly spaced and there is no car-free zone


Key pieces of logic: 
* 
