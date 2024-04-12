from fastapi import FastAPI, HTTPException
from database import queries

app = FastAPI()


@app.on_event("startup")
async def startup():
    app.state.connection = await queries.connect_to_database()


@app.on_event("shutdown")
async def shutdown():
    await queries.disconnect_from_database(app.state.connection)


@app.get('/api/users/{user_id}')
async def delete_user(user_id: int):
    async with queries.connect_to_database() as connection:
        await connection.execute('CALL delete_user_by_id($1)', user_id)
    return {'message': f'User with ID {user_id} deleted successfully'}
