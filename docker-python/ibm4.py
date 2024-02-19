def countNumbers(arr):
    total_count = 0
    
    for interval in arr:
        start, end = interval
        count = 0
        
        for num in range(start, end + 1):
            digits = set(str(num))
            if len(digits) == len(str(num)):
                count += 1
        
        print(count)

if __name__ == '__main__':
    num_intervals = int(input().strip())
    intervals = []
    for _ in range(num_intervals):
        start, end = map(int, input().strip().split())
        intervals.append([start, end])
    
    countNumbers(intervals)
