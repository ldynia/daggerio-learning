#!/usr/bin/env python3

import sys
import anyio
import dagger


async def provision_python():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        container = client.container().from_("python:3.10-slim-buster")
        container = container.with_exec(["python", "-V"])
        py_version = await container.stdout()
    
    print(f"{py_version}")


async def provision_os():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        container = client.container().from_("python:3.10-slim-buster")
        container = container.with_exec(["apt-get", "update"])
        container = container.with_exec(["apt-get", "install", "-y", "vim"])
        exit_code = await container.exit_code()
    
    print(f"Program status code: {exit_code}")


if __name__ == "__main__":
    anyio.run(provision_python)
    anyio.run(provision_os)
