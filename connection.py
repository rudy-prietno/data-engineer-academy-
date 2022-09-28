import asyncpg
import asyncio
import os
import sys
sys.path.append(os.getcwd())

from src import config


# Credential DB
SERVER_DB = config.DB_URL
DATABASE_DB = config.DB_NAME
USERNAME_DB = config.DB_USER
PASSWORD_DB = config.DB_PASS
PORT_DB = config.DB_PORT

class DBClient:

    async def ConnectionDB():
        conn = None
        if conn == None:
            try:

                conn = await asyncpg.connect(
                    user=USERNAME_DB,
                    password=PASSWORD_DB,
                    database=DATABASE_DB,
                    host=SERVER_DB,
                    port=PORT_DB,
                )

            except:

                print(f"[INFO] Can't connect PostgreSQL .....")

            return "[INFO] Success connect PostgreSQL .....{connd}".format(connd=conn)
