provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "resource_group" {
  name      = var.AZURE_RESOURCE_GROUP_NAME
  location  = var.AZURE_RESOURCE_GROUP_LOCATION
}