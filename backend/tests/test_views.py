import json

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient


# Тестирование регистрации пользователя
@pytest.mark.django_db
def test_register_user(api_client, user_data):
    url = reverse('backend:user-register')

    # Отправляем запрос
    response = api_client.post(url, user_data, format='json')

    # Проверяем статус код
    assert response.status_code == 200

    try:
        response_data = response.json()

        # Проверяем, что в ответе есть ожидаемые поля
        assert 'Status' in response_data
        assert response_data.get('Status') is True

    except json.JSONDecodeError as e:
        pytest.fail(f"Response is not valid JSON: {e}")
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")