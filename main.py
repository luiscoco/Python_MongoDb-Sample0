# -----------------------------------------------------------------------------------------------------------
# -----------------------------------FIRST APPLICATION ------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# print("Hello, World!")

# -----------------------------------------------------------------------------------------------------------
# -----------------------------------SECOND APPLICATION ------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
import sentry_sdk
from aiohttp import web
from sentry_sdk.integrations.aiohttp import AioHttpIntegration

API_PORT = 8000


def create_application():
    app = web.Application()
    # Add your routes and middleware here
    return app


if __name__ == '__main__':
    app = create_application()

    async def hello(request):
        return web.Response(text='HELLO WORLD')

    app.router.add_route('GET', '/', hello)
    
    web.run_app(
        app,
        port=API_PORT,
        print=None
    )
