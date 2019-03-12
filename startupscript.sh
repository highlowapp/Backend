CONTAINER_ALREADY_STARTED="CONTAINER_ALREADY_STARTED_PLACEHOLDER"
import os
if [ ! -e $CONTAINER_ALREADY_STARTED ]; then
    touch $CONTAINER_ALREADY_STARTED
    echo "-- First container startup --"
    # YOUR_JUST_ONCE_LOGIC_HERE
    cmd = "mysql < mysql_start_file -u root -p"
    os.system(cmd)
else
    echo "-- Not first container startup --"