#
# Collection of tasks and useful command to setup and manage Arnica project
#

from invoke import task, Collection


@task
def build(ctx, docs=False):
    ctx.run("python setup.py build")
    if docs:
        ctx.run("sphinx-build docs docs/_build")


@task
def freeze(ctx, docs=False):
    ctx.run("pip freeze | sort > requirements.txt")


@task
def docker_build(ctx, version="latest"):
    ctx.run(f"docker build -t mlhamel/arnica:{version} .")


@task
def docker_push(ctx, version="latest"):
    ctx.run(f"docker push mlhamel/arnica:{version}")


# Docker collection
docker = Collection("docker")
docker.add_task(docker_build, "build")
docker.add_task(docker_push, "push")


# Main collection
ns = Collection()
ns.add_task(build, "build")
ns.add_task(freeze, "freeze")
ns.add_collection(docker)
