from uuid import UUID

import pytest
from pydantic import ValidationError

from store.core.schemas.product import ProductIn
from tests.schemas.factories import product_data


def test_schemas_return_success():
    data = product_data()

    product = ProductIn.model_validate(data)

    assert product.name == "Redmi Note Pro 15 5G"
    assert isinstance(product.id, UUID)


def test_schemas_return_raise():
    data = {
        "name": "Redmi Note Pro 15 5G",
        "quantity": 10,
        "price": 1999.99,
    }

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Redmi Note Pro 15 5G", "quantity": 10, "price": 1999.99},
        "url": "https://errors.pydantic.dev/2.11/v/missing",
    }
