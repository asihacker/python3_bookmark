import click


@click.command()
@click.option('--name', default='asi', help='名字', prompt=True)
@click.option('--age', default=18, help='年龄', prompt=False)
# default：给命令行选项添加默认值
# help：给命令行选项添加帮助信息
# type：指定参数的数据类型，例如int、str、float
# required：是否为必填选项，True为必填，False为非必填
# prompt：在命令行提示用户输入对应选项的信息
# nargs：指定命令行选项接收参数的个数，如果超过则会报错
def test(name: str, age: int):
    click.echo(f'你的名字:{name},你的年龄是:{age}')


if __name__ == "__main__":
    test()
