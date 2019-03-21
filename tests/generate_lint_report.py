import subprocess

cmd = 'pylint -ry src/ tests/ >> tests/pylint.out'
try:
    subprocComplete = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(subprocComplete.stdout.decode('utf-8'))
except subprocess.CalledProcessError as err:
    print(err.output.decode('utf-8'))