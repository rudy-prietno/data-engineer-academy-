import time

import asyncio
from src.Connection import DBClient
from dataExtract1 import dataExtract_base
from dataExtract2 import dataExtract_com

import os
import sys
sys.path.append(os.getcwd())

start_time = time.time()

loop = asyncio.new_event_loop()



if __name__ == '__main__':
    query = "SELECT t.* FROM public.film t  order by 1 desc LIMIT 5"
    query1 = "SELECT t.* FROM public.film t  order by 1 desc LIMIT 2"
    
    
    r = loop.run_until_complete(
                DBClient.ConnectionDB()
                )

    s = loop.run_until_complete(
        dataExtract_base.extract(
            connection= r, 
            query= query
        )
    )

    t = loop.run_until_complete(
        dataExtract_com.extract(
            connection= r, 
            query= query
        )
    )


    print(s)
    print(t)

    print("--- %s seconds ---" % (time.time() - start_time))
