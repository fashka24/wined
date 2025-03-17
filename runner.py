# execute of files

import os

def run_py(file, args):
    print(f"[RUN] python {file} {' '.join(args)}")
    print("exit code:", os.system(f"node {file} {' '.join(args)}") >> 8)
def run_js(file, args):
    print(f"[RUN] node {file} {' '.join(args)}")
    print("exit code:", os.system(f"node {file} {' '.join(args)}") >> 8)

def build_cpp(file, args):
    print(f"[BUILD] g++ {file} {' '.join(args)}")
    print("exit code:", os.system(f"g++ {file} {' '.join(args)}") >> 8)
def build_c(file, args):
    print(f"[BUILD] gcc {file} {' '.join(args)}")
    print("exit code:", os.system(f"gcc {file} {' '.join(args)}") >> 8)

runs = {
    "Python": run_py,
    "JavaScript": run_js,
}
builds = {
    "C++": build_cpp,
    "C": build_c,
}

def do_run(run_type, file, args):
    try:
        runs[run_type](file, args)

    except Exception as e:
        return


def do_build(build_type, file, args):
    try:
        builds[build_type](file, args)

    except Exception as e:
        return