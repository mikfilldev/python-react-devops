import pytest
from flask.testing import FlaskClient
from app import (
    app,
    ProductModel,
    create_product,
    get_product_by_id,
)


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            # Initialize the in-memory database for testing
            ProductModel._meta.database.init(":memory:")
            ProductModel.create_table()
            yield client
            # Drop the table after tests
            ProductModel.drop_table()


def test_get_all_products(client: FlaskClient):
    """Test retrieving all products when the database is empty."""
    response = client.get("/api/products")
    assert response.status_code == 200
    assert response.json == []

    # Add a product and test again
    create_product("Test Product", 100)
    response = client.get("/api/products")
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["name"] == "Test Product"


def test_create_product(client: FlaskClient):
    """Test creating a new product."""
    response = client.post("/api/products", json={"name": "New Product", "price": 50})
    assert response.status_code == 201
    assert response.json["message"] == "Product added successfully."
    product_id = response.json["productId"]

    # Verify the product was created in the database
    product = get_product_by_id(product_id)
    assert product is not None
    assert product.name == "New Product"
    assert product.price == 50


def test_get_single_product(client: FlaskClient):
    """Test retrieving a single product by ID."""
    # Create a product
    product = create_product("Single Product", 150)
    response = client.get(f"/api/products/{product.id}")
    assert response.status_code == 200
    assert response.json["name"] == "Single Product"
    assert response.json["price"] == 150

    # Test retrieving a non-existing product
    response = client.get("/api/products/999")
    assert response.status_code == 404
    assert response.json["error"] == "Product not found."


def test_update_product(client: FlaskClient):
    """Test updating an existing product."""
    # Create a product
    product = create_product("Old Product", 75)
    response = client.patch(
        f"/api/products/{product.id}", json={"name": "Updated Product", "price": 100}
    )
    assert response.status_code == 200
    assert response.json["message"] == "Product updated successfully."

    # Verify the product was updated in the database
    updated_product = get_product_by_id(product.id)
    assert updated_product.name == "Updated Product"
    assert updated_product.price == 100


def test_delete_product(client: FlaskClient):
    """Test deleting a product."""
    # Create a product
    product = create_product("Delete Me", 200)
    response = client.delete(f"/api/products/{product.id}")
    assert response.status_code == 200
    assert response.json["message"] == "Product deleted."

    # Verify the product was deleted from the database
    deleted_product = get_product_by_id(product.id)
    assert deleted_product is None
