from main import alarm, screen_clean, SEC_IN_MIN
import time


def work_count(work_sec):
    for i in range(work_sec, 0, -1):  # Count down from the minute given to zero
        min_left = i // SEC_IN_MIN
        sec_left = i % SEC_IN_MIN
        if i < 60:  # alarm trigger
            alarm()
        screen_clean()
        print(min_left, ":", sec_left)
        time.sleep(1)


def rest_count(rest_sec):
    for i in range(rest_sec, 0, -1):
        if i < 15:  # alarm trigger
            alarm()
        screen_clean()
        print(i, "seconds left")
        time.sleep(1)
