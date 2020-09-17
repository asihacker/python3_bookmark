import click


# default：给命令行选项添加默认值
# help：给命令行选项添加帮助信息
# type：指定参数的数据类型，例如int、str、float
# required：是否为必填选项，True为必填，False为非必填
# prompt：在命令行提示用户输入对应选项的信息
# nargs：指定命令行选项接收参数的个数，如果超过则会报错
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
