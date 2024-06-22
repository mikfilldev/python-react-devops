import pytest
from db import (
    ProductModel,
    create_product,
    get_product_by_id,
    update_product,
    delete_product,
)


@pytest.fixture
def setup_database():
    """Setup an in-memory database for testing."""
    ProductModel._meta.database.init(":memory:")
    ProductModel.create_table()
    yield
    ProductModel.drop_table()


def test_create_product(setup_database):
    """Test creating a product in the database."""
    product = create_product("Test Product", 100)
    assert product.id is not None
    assert product.name == "Test Product"
    assert product.price == 100


def test_get_product_by_id(setup_database):
    """Test retrieving a product by ID."""
    product = create_product("Retrieve Me", 250)
    retrieved_product = get_product_by_id(product.id)
    assert retrieved_product is not None
    assert retrieved_product.name == "Retrieve Me"
    assert retrieved_product.price == 250

    # Test retrieving a non-existing product
    assert get_product_by_id(999) is None


def test_update_product(setup_database):
    """Test updating a product in the database."""
    product = create_product("Old Name", 100)
    updated_product = update_product(product.id, name="New Name", price=150)
    assert updated_product.name == "New Name"
    assert updated_product.price == 150

    # Test partial update
    updated_product = update_product(product.id, price=200)
    assert updated_product.name == "New Name"  # Name should remain the same
    assert updated_product.price == 200


def test_delete_product(setup_database):
    """Test deleting a product from the database."""
    product = create_product("To Be Deleted", 300)
    assert delete_product(product.id) is True
    assert get_product_by_id(product.id) is None

    # Test deleting a non-existing product
    assert delete_product(999) is False
