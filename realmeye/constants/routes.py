from pydantic_settings import BaseSettings

class APIRoutes(BaseSettings):
    base_guild_url: str = "https://www.realmeye.com/guild/"
    base_player_url: str = "https://www.realmeye.com/player/"

routes = APIRoutes()
