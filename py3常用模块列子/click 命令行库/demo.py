import click


@click.command()
@click.option('--name', default='asi', help='名字', prompt=True)
@click.option('--age', default=18, help='年龄', prompt=False)
def test(name: str, age: int):
    click.echo(f'你的名字:{name},你的年龄是:{age}')


if __name__ == "__main__":
    test()