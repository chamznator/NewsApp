import pytest
from flask import Flask
from unittest.mock import patch, Mock
from app import fetch_summary

@pytest.fixture
def test_client():
    app = Flask(__name__)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_fetch_summary_no_topic(test_client):
    response = test_client.get('/fetch_summary')
    assert response.status_code == 400
    assert response.get_json() == {"error": "No topic provided"}

@patch('app.fetch_news')
@patch('app.summarize_text')
def test_fetch_summary_success(mock_summarize, mock_fetch_news, test_client):
    mock_articles = [
        {'content': 'Article 1 content'},
        {'content': 'Article 2 content'},
        {'content': None}
    ]
    mock_fetch_news.return_value = mock_articles
    mock_summarize.side_effect = ['Summary 1', 'Summary 2']
    
    response = test_client.get('/fetch_summary?topic=technology')
    
    assert response.status_code == 200
    assert response.get_json() == {"summaries": ['Summary 1', 'Summary 2']}
    mock_fetch_news.assert_called_once()
    assert mock_summarize.call_count == 2

@patch('app.fetch_news')
def test_fetch_summary_no_content(mock_fetch_news, test_client):
    mock_fetch_news.return_value = [{'content': None}, {'content': None}]
    
    response = test_client.get('/fetch_summary?topic=technology')
    
    assert response.status_code == 200
    assert response.get_json() == {"summaries": []}

@patch('app.fetch_news')
def test_fetch_summary_empty_articles(mock_fetch_news, test_client):
    mock_fetch_news.return_value = []
    
    response = test_client.get('/fetch_summary?topic=technology')
    
    assert response.status_code == 200
    assert response.get_json() == {"summaries": []}
