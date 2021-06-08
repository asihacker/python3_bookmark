import click


@click.group()  # 命令的总入口
def cli():
    pass


# argument的使用和 option 类似，但支持的功能比 option 少,两者的传参也有区别
# python group.py cmd1 value1 value2
# python 提取关键词demo.py --key value
@cli.command()  # `cli`表示该方法隶属于@click.group
@click.argument('name')  # 传参的时候仍然使用`click` 而不是`cli`|
@click.argument('age')  # 传参的时候仍然使用`click` 而不是`cli`|argument的使用和 option 类似，但支持的功能比 option 少
def cmd1(name, age):
    print("执行cmd1", name, age)


@cli.command()  # `cli`表示该方法隶属于@click.group
@click.argument('name')  # 传参的时候仍然使用`click` 而不是`cli`
def cmd2(name):
    print("执行cmd2", name)


if __name__ == "__main__":
    cli()  # 这里要调用`cli()`而不能调用子命令
