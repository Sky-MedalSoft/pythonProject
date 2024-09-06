TORTOISE_ORM = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.mysql",
                "credentials": {
                    "host": "localhost",
                    "port": 3306,
                    "database": "test",
                    "user": "root",
                    "password": "root",
                    "charset": "utf8mb4",
                    "minsize": 1,
                    "maxsize": 5,
                    "echo": True,
                }
            }
        },
        "apps": {
            "models": {
                "models": ["day0821.ORM.models", "aerich.models"],
                "default_connection": "default",
            }
        },
        "use_tz": False,
        "timezone": "Asia/Shanghai",
    }