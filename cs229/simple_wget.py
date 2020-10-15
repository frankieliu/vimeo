from subprocess import Popen, STDOUT, PIPE, CalledProcessError
import shlex

def wget(ain, aout=None, print_stdout=True):
    """wget("http://www.google.com", print_stdout=False)
    
    Parameters
    ----------
    ain : string
        input link
    aout : string, optional
        output file
    print_stdout: bool, optional
        whether or not to print the stdout/stderr

    """
    if aout is None:
        wget_cmd = f"wget {ain}"
    else:
        wget_cmd = f"wget -O {aout} {ain}"

    with Popen(shlex.split(wget_cmd),
            stdout=PIPE,
            stderr=STDOUT,
            bufsize=1, universal_newlines=True) as p:
        p.wait()
        if print_stdout:
            for line in p.stdout:
                print(line)
        if p.returncode:
            raise CalledProcessError(p.returncode, p.args)

