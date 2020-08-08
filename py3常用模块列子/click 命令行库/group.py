import click


@click.group()  # 命令的总入口
def cli():
    pass


@cli.command()  # `cli`表示该方法隶属于@click.group
@click.argument('name')  # 传参的时候仍然使用`click` 而不是`cli`
def cmd1(name):
    print("执行cmd1")


@cli.command()  # `cli`表示该方法隶属于@click.group
@click.argument('name')  # 传参的时候仍然使用`click` 而不是`cli`
def check(name):
    print("执行cmd2")


if __name__ == "__main__":
    cli()  # 这里要调用`cli()`而不能调用子命令
