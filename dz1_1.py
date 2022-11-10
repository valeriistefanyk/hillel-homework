#!/usr/bin/python3

import subprocess
import calendar
import datetime
import random


def gen_log_filename(day, month, year):
    return f"{day:02d}-{month:02d}-{year}.log"


def main():
    # 3.a
    subprocess.run(["whoami"])

    # 3.b
    subprocess.run(["pwd"])

    # 3.c
    subprocess.run(["mkdir", "dz1"])

    # 3.d
    now = datetime.datetime.now()
    month = now.month
    year = now.year
    days_per_month = calendar.monthrange(now.year, now.month)[1]
    log_filenames = ([gen_log_filename(day, month, year)
                      for day in range(1, days_per_month + 1)])
    subprocess.run(['touch', *log_filenames], cwd='dz1')

    # 3.e
    subprocess.run(['sudo', 'chown', '-R', 'root:root', 'dz1'])

    # 3.f
    files_to_remove = random.sample(log_filenames, 5)
    subprocess.run(['rm', *files_to_remove], cwd='dz1')


if __name__ == '__main__':
    main()
