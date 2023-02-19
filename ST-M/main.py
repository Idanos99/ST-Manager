import os
import user_param
import count_loops

SEC_IN_MIN = 60
sec_work = user_param.args.min * SEC_IN_MIN


def screen_clean():
    os.system('clear')  # screen clearing


def alarm():
    if user_param.args.quiet:
        print("\a")  # sound alarm


def suspend():
    if user_param.args.suspend:
        screen_clean()
        os.system("systemctl suspend")  # suspend
        raise SystemExit  # kill process


if __name__ == "__main__":
    count_loops.loops(user_param.args.loop)
