import user_param
from countdowns import work_count, rest_count
from main import SEC_IN_MIN, suspend


def loops(loops_count):
    while loops_count > 0:
        work_count(user_param.args.min * SEC_IN_MIN)
        suspend()
        rest_count(user_param.args.sec)
        loops_count -= 1

    if loops_count == -1:
        while True:
            work_count(user_param.args.min * SEC_IN_MIN)
            suspend()
            rest_count(user_param.args.sec)
