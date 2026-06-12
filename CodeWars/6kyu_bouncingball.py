def bouncing_ball (height : float, bounce: float, window_height: float) -> int:
    if not (0 < bounce < 0): 
        return -1
    
    count = 0
    while height > window_height:
        count += 1
        height *= bounce

        if height > window_height: # when bouncing back up, if it's still higher than window
            count += 1
    
    return count or -1 # if count = 0, then return -1