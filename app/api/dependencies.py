from uuid import UUID, uuid4


async def generate_uuid() -> UUID:
    return uuid4()
