import os
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)


@app.route("/")
def index():
    try:
        page_reviews = redis().incr("page_reviews")
    except RedisError:
        app.logger.exception("Redis Error")
        return "Sorry, something went wrong \N{PENSIVE FACE}", 500
    return f"This page has been reviewed {page_reviews} times."


@cache
def redis():
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))
