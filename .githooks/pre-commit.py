#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Github pre-commit hook based on Python to pylint source code. The source code here were adopted from
https://github.com/sebdah/git-pylint-commit-hook/blob/master/git_pylint_commit_hook/commit_hook.py

You may skip this hook using the no-verify option. For example,
git commit -no-verify -m "my message"
"""

import collections
import os
import re
import sys
import subprocess

prj_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, prj_dir)

LIMIT = 8
ExecutionResult = collections.namedtuple('ExecutionResult', 'status, stdout, stderr')
_SCORE_REGEXP = re.compile(r'^Your\ code\ has\ been\ rated\ at\ (\-?[0-9\.]+)/10')
_IGNORE_REGEXT = re.compile(r'(Ignoring entire file \(file\-ignored\))|(^0 statements analysed.)')


def _futurize_str(obj):
    if isinstance(obj, bytes):
        obj = obj.decode('utf-8')
    return obj


def _execute(cmd):
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    status = process.poll()
    return ExecutionResult(status, stdout, stderr)


def _current_commit():
    if _execute('git rev-parse --verify HEAD'.split()).status:
        return '4b825dc642cb6eb9a060e54bf8d69288fbee4904'
    return 'HEAD'


def _get_list_of_committed_files():
    """ Returns a list of files about to be commited. """
    files = []
    # pylint: disable=E1103
    diff_index_cmd = 'git diff-index --cached %s' % _current_commit()
    output = subprocess.check_output(
        diff_index_cmd.split()
    )
    for result in _futurize_str(output).split('\n'):
        if result != '':
            result = result.split()
            if result[4] in ['A', 'M']:
                files.append(result[5])
    return files


def _parse_score(pylint_output):
    """Parse the score out of pylint's output as a float
    If the score is not found, return 0.0.
    """
    for line in pylint_output.splitlines():
        match = re.match(_SCORE_REGEXP, _futurize_str(line))
        if match:
            return float(match.group(1))
    return 0.0


def _check_ignore(pylint_output):
    """Check the python file whether ignored
    If the file is ignored returns True,
    returns False otherwise
    """
    for line in pylint_output.splitlines():
        match = re.search(_IGNORE_REGEXT, _futurize_str(line))
        if match:
            return True

    return False


def _is_python_file(filename):
    """Check if the input file looks like a Python script
    Returns True if the filename ends in ".py" or if the first line
    contains "python" and "#!", returns False otherwise.
    """
    if filename.endswith('.py'):
        return True
    with open(filename, 'r') as file_handle:
        first_line = file_handle.readline()
    return 'python' in first_line and '#!' in first_line


def pylint_files():
    stop_commit = False
    my_files = _get_list_of_committed_files()

    python_files = []
    for f in my_files:
        if _is_python_file(f):
           python_files.append(f)

    for python_file in python_files:
        # Allow __init__.py files to be completely empty
        if os.path.basename(python_file) == '__init__.py':
            if os.stat(python_file).st_size == 0:
                continue

        # Start pylinting
        sys.stdout.write("RUNNING PYLINT ON FILE: {}".format(python_file))
        sys.stdout.flush()
        try:
            command = ['pylint']
            command.append(python_file)
            proc = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            out, _ = proc.communicate()
        except OSError:
            print("\nAn error occurred. Is pylint installed?")


        # Verify the score
        score = _parse_score(out)
        ignored = _check_ignore(out)
        if ignored or score >= float(LIMIT):
            status = 'PASSED'
        elif not out and not proc.returncode:
            # pylint produced no output but also no errors
            status = 'SKIPPED'
        else:
            status = 'FAILED'
            stop_commit = True

        sys.stdout.write("\nSCORE: {} ({})\n".format(score, status))

        command.append('--reports=n')
        proc = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, _ = proc.communicate()
        print(_futurize_str(out))

    if stop_commit:
        print ("""\n
 ____________________
/                    \
|        STOP        |
\____________________/
         !  !
         !  !
         L_ !
        / _)!
       / /__L
 _____/ (____)
        (____)
 _____  (____)
      \_(____)
         !  !
         !  !
         \__/        
        """)
        sys.exit(1)
    else:
        print ("""
 _______________
|@@@@|     |####|
|@@@@|     |####|
|@@@@|     |####|
\@@@@|     |####/
 \@@@|     |###/
  `@@|_____|##'
       (O)
    .-'''''-.
  .'  * * *  `.
 :  *       *  :
: ~   G I T   ~ :
: ~ A W A R D ~ :
 :  *       *  :
  `.  * * *  .'
    `-.....-'
        """)

pylint_files()

