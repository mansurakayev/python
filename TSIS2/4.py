class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max, altitude = 0, 0
        for i in range(len(gain)):
            altitude += gain[i]
            if altitude > max: max = altitude
        return max