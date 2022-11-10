#!/usr/bin/python3

import subprocess


def write_to_beginning(filename: str, line: str):
    with open(filename, 'r+') as f:
        content = f.read()
        if not content.startswith('#!'):
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n\n' + content)


def main():
    run_file = 'dz1_run.py'
    py_shebang = '#!/usr/bin/python3'

    # 4.a
    subprocess.run(['sudo', 'cp', 'dz1_1.py', run_file])

    # 4.b
    subprocess.run(['sudo', 'chmod', '777', run_file])
    write_to_beginning(run_file, py_shebang)

    # 4.c
    subprocess.run(['sudo', 'chmod', '500', run_file])

    # 4.d
    subprocess.run(['sudo', f'./{run_file}'])


if __name__ == '__main__':
    main()
