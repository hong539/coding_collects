#!/bin/bash

# [ Define Variables ]
HOST=`hostname -s`
syslogtag=MySQL-Backup
DEST=/var/dba/backup/
DBS="$(mysql -u root -Bse 'show databases' | egrep -v '^Database$|hold$' | grep -v 'performance_schema\|information_schema')"
DATE=$(date +'%F')

#[ Individually dump all databases with date stamps ]
for db in ${DBS[@]};
do  

GZ_FILENAME=$HOST-$db-$DATE.sql.gz
mysqldump -u root --quote-names --opt --single-transaction --quick $db > $DEST$HOST-$db-$DATE.sql
ERR=$?

if [ $ERR != 0 ]; then
NOTIFY_MESSAGE="Error: $ERR, while backing up database: $db"
logger -i -t ${syslogtag} "MySQL Database Backup FAILED; Database: $db"
else
NOTIFY_MESSAGE="Successfully backed up database: $db "
logger -i -t ${syslogtag} "MySQL Database Backup Successful; Database: $db"
fi
echo $NOTIFY_MESSAGE
done