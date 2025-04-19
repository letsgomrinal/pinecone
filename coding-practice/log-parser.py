from collections import deque

def detect_bursts(timestamps):
    window = deque()
    result = []

    for t in timestamps:
        # Slide the window
        while window and t - window[0] > 5:
            window.popleft()
        window.append(t)
        
        if len(window) == 3:
            result.append(window[0])  

    return result


            

if __name__=='__main__':
    timestamps = [1, 2, 3, 10, 11, 12, 30, 32, 40]
    print(detect_bursts(timestamps))
