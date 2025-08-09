from unittest.mock import AsyncMock

import pytest

from store.usecases.product import ProductUsecase


@pytest.mark.asyncio
async def test_usecases_should_return_success(product_in):
    mock_collection = AsyncMock()
    usecase = ProductUsecase(collection=mock_collection)

    await usecase.create(body=product_in)

    mock_collection.insert_one.assert_awaited_once_with(product_in.model_dump())
