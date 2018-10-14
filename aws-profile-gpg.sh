#!/usr/bin/env python

import os
import sys
import subprocess

def main():

    home_path = os.getenv( 'AWS_PROFILE_GPG_HOME', '/usr/local/opt/aws-profile-gpg' )
    script_path = home_path + '/aws-profile-gpg.py'

    if not os.path.exists( script_path ):
        sys.exit(
            'Error: Unable to find script, ' + script_path +
            '; AWS_PROFILE_GPG_HOME=' + home_path
        )

    rv = subprocess.call(
        [ home_path + '/venv/bin/python', script_path ]
        + sys.argv[1:]
    )

    sys.exit(rv)

if __name__ == "__main__":
    main()
