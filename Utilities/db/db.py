# db
from os.path import isfile
from sqlite3 import connect
import asyncio
import asqlite

# custom utilities and setup
from Utilities import log
log = log.Logger("db")

DB_PATH = "./Data/database.db"
BUILD_PATH = "./Utilities/db/build.sql"

async def build():
    async with asqlite.connect(DB_PATH) as connection:
        async with connection.cursor() as cursor:
            if isfile(BUILD_PATH):
                with open(BUILD_PATH, "r", encoding="utf-8") as script:
                    await cursor.executescript(script.read())

                    await log.info("Database built.")

async def commit():
    async with asqlite.connect(DB_PATH) as connection:
        await connection.commit()

        await log.info("Committed to database.")

async def close():
    async with asqlite.connect(DB_PATH) as connection:
        await connection.close()

        await log.info("Closed database connection.")

async def field(command, *values):
    async with asqlite.connect(DB_PATH) as connection:
        async with connection.cursor() as cursor:
            await cursor.execute(command, tuple(values))
            
            await log.info(f"Executed {command} with {values}.")

            if (fetch := await cursor.fetchone()) is not None: 
                await log.info(f"Fetched {fetch}.")
                return fetch[0]


async def record(command, *values):
    async with asqlite.connect(DB_PATH) as connection:
        async with connection.cursor() as cursor:
            await cursor.execute(command, tuple(values))

            await log.info(f"Executed {command} with {values}.")
            
            return await cursor.fetchone()

async def records(command, *values):
    async with asqlite.connect(DB_PATH) as connection:
        async with connection.cursor() as cursor:
            await cursor.execute(command, tuple(values))

            await log.info(f"Executed {command} with {values}.")

            return await cursor.fetchall()

async def column(command, *values):
    async with asqlite.connect(DB_PATH) as connection:
        async with connection.cursor() as cursor:
            await cursor.execute(command, tuple(values))

            await log.info(f"Executed {command} with {values}.")

            return [item[0] for item in await cursor.fetchall()]

async def execute(command, *values):
    async with asqlite.connect(DB_PATH) as connection:
        async with connection.cursor() as cursor:
            await cursor.execute(command, tuple(values))

            await log.info(f"Executed {command} with {values}.")

async def multiexec(command, valueset):
    async with asqlite.connect(DB_PATH) as connection:
        async with connection.cursor() as cursor:
            await cursor.executemany(command, valueset)

            await log.info(f"Executed {command} with {valueset}.")