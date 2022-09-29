import asyncpg
import asyncio
import os
import sys
sys.path.append(os.getcwd())

from src import Config


# Credential DB
SERVER_DB = Config.DB_URL
DATABASE_DB = Config.DB_NAME
USERNAME_DB = Config.DB_USER
PASSWORD_DB = Config.DB_PASS
PORT_DB = Config.DB_PORT


class DBClient:
    ####### setup connection #######
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

                # await conn.close()

            except asyncpg.PostgresError as exc:
                return ("Failed to initialise database.", exc)

            else:
                pass

        return conn


    ####### setup connection with Pool #######
    async def ConnectionDBPool():

        conn = None
        if conn == None:

            try:
                conn = await asyncpg.create_pool(
                        user=USERNAME_DB,
                        password=PASSWORD_DB,
                        database=DATABASE_DB,
                        host=SERVER_DB,
                        port=PORT_DB,
                    )

                # await conn.close()

            except asyncpg.PostgresError as exc:
                return ("Failed to initialise database.", exc)

            else:
                pass

        return conn
