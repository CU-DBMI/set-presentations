"""
Run tests for multiple Python versions concurrently.

referenced with modifications from:
https://docs.dagger.io/sdk/python/628797/get-started
"""

import sys

import anyio

import dagger


async def compile_presentation():
    """
    Runs tests through Dagger
    """
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        # get reference to the local project
        src = client.host().directory(".")

        async def compilation():
            python = (
                client.container()
                .from_("python:-slim-buster")
                # mount cloned repository into image
                .with_mounted_directory("/presentation", src)
                # set current working directory for next commands
                .with_workdir("/presentation")
                # install test dependencies
                .with_exec(["pip", "install", "poetry==1.4"])
                .with_exec(["poetry", "install"])
                # run tests
                .with_exec(["poetry", "run", "python", "-m", "pytest"])
            )

            # execute
            await python.exit_code()

        # when this block exits, all tasks will be awaited (i.e., executed)
        async with anyio.create_task_group() as task_group:
            task_group.start_soon(compilation)

    print("All tasks have finished")


if __name__ == "__main__":
    anyio.run(compile_presentation)
