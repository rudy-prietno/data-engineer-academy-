import asyncpg
import asyncio
import os
import sys
sys.path.append(os.getcwd())


class dataExtract_base ():
    ####### running extract data #######
    async def extract(connection, query):
        try:
            record = await connection.fetch(query)

        except asyncpg.PostgresError as exc:
                return ("Failed to extract data. ", exc)
        else:
            return connection
            await connection.close()


    ####### running extract data #######
    async def extractPool(connection, query):
        try:
            async with connection.acquire() as con:
                record = await con.fetch(query= query)
                
        except asyncpg.PostgresError as exc:
                return ("Failed to extract data. ", exc)

        else:
            return record
            await connection.close()
