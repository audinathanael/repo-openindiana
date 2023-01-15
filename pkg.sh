#! /bin/bash
pkg install pkg://openindiana.org/SUNWPython-extra@0.5.11,5.11-0.151.1.9:20140117T202839Z

pkgrecv -s http://localhost:10000 -d /repo2 -a -r pkg://openindiana.org/SUNWarbel@0.5.11,5.11-0.151.1.9:20140117T205427Z