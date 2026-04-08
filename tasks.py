from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/ui.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest src", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run -m pytest src", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def pylint(ctx):
    ctx.run("pylint src/run.py src/database", pty=True)