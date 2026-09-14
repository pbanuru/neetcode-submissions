class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we have a bunch of cars
        # all in one road
        # for each car, we know it's current speed, and current position
        # a car that is faster than the car in front cannot go faster than the car in front.
        # for each car, starting from the end,
        # we need to find out at what time it will reach the target
        # arrival time is calculated by distance / speed:
        # (tar-p) / s = t
        # if a car would reach the target faster than the car in front (if unblocked), it will
        # slow down to the speed of the car in front of it, and thus act as one group.
        # we will solve this problem by maintaining a stack.
        # we will calculate the arrival time of the current car. 
        # If the time <= (faster) the time of the car on the top of the stack, we ignore it.
        # if the time > (slower) the time of the car on the top of the stack, we add it to the stack.

        s = []
        times = [(target-pos)/spd for pos,spd in sorted(zip(position,speed))]
        for ctime in reversed(times):

            if (s and ctime > s[-1]) or not s:
                s.append(ctime)

        return len(s)
