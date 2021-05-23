from click import echo
from tabulate import tabulate

from todo.query import get_db_column, ToDoItem
import click


def _output(tilte: str, items: list[ToDoItem]):
    items = tabulate([[item.title] for item in items], headers=[f"<<{tilte.upper()}>>"], tablefmt="fancy_grid", stralign="center")
    return echo(items)


@click.group()
def todo_commands():
    pass


@click.command()
@click.argument('column', default="Backlog")
def show(column) -> None:
    try:
        backlog_items = get_db_column(column=column)
    except KeyError as err:
        return echo(str(err))
    return _output(tilte=column, items=backlog_items)


todo_commands.add_command(show)


if __name__ == "__main__":
    show()
