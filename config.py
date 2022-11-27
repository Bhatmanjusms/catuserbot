from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 977080
    API_HASH = "0c20c4265501492a1513f91755acd42b"
    # the name to display in your alive message
    ALIVE_NAME = "i'm alive"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://yjsmplyl:ZegZsJBvh6JcW2OoPNvjVlfWHjSu_IH0@heffalump.db.elephantsql.com/yjsmplyl"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "Your value"
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5901549073:AAGkgZ3RMftX-9Bqzj7mxOrxe_vn6BCa_Zs"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001723543713
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
