[app]

# (str) Title of your application
title = Joblink

# (str) Package name
package.name = joblink

# (str) Package domain (needed for android/ios packaging)
package.domain = com.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of service to declare
services = NAME:ENTRYPOINT_TO_PY,otherservice:otherservice.py


