# gym-server

## POSTGRESQL SETUP

createdb gym
createuser -P gymuser
[.. enter password in settings.py ..]

GRANT ALL PRIVILEGES ON DATABASE gym TO gymuser;