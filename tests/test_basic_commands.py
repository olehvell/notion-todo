from unittest.mock import patch
from click.testing import CliRunner
from tests.responses import db_query_response_success, db_retrieve_query
from todo.cli import show
from notion_client.api_endpoints import DatabasesEndpoint


def test_show():
    with patch.object(DatabasesEndpoint, 'query',
                      return_value=db_query_response_success):
        test_runner = CliRunner()
        result = test_runner.invoke(show)
        assert "uno" in result.output
        assert "dos" in result.output
        assert "Tres" in result.output


def test_show_unknown_column():
    with patch.object(DatabasesEndpoint, 'query',
                      return_value=db_retrieve_query):
        test_runner = CliRunner()
        result = test_runner.invoke(show, ['this column does not exist'])
        assert "Column 'this column does not exist' does not exist in the db" in result.output

