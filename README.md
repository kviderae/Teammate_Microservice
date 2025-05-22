# Teammate_Microservice

Category Microservice for Jay's Expense Tracker
==============================================

This microservice handles expense category management, supporting both default and user-defined categories. It provides RESTful endpoints for retrieving, creating, and deleting categories.

------------------------------------------------------------
How to Programmatically REQUEST Data
------------------------------------------------------------

1. GET all categories for a specific user
-----------------------------------------
Send a GET request to:

    /categories?userId=<USER_ID>

Example:

    GET /categories?userId=jay123

Returns all default categories + any custom categories for the user.

2. POST a new custom category
-----------------------------
Send a POST request to:

    /categories
    Content-Type: application/json

Request body:

    {
      "userId": "jay123",
      "categoryName": "Pet Supplies"
    }

Creates a new user-defined category for the specified user.

3. DELETE a custom category
---------------------------
Send a DELETE request to:

    /categories/<CATEGORY_ID>?userId=<USER_ID>

Example:

    DELETE /categories/ed1e21e2-bc11-402c-83b2-69e2a44fa9f6?userId=jay123

Deletes the specified category if it belongs to the user and is not a default category.

------------------------------------------------------------
How to Programmatically RECEIVE Data
------------------------------------------------------------

Response from GET /categories
-----------------------------
Returns a list of JSON objects representing all categories for the user.

Example:

    [
      {
        "id": "d3f1b4a6-1e41-4cf6-83c0-89d2b5fdb1ee",
        "name": "Food",
        "type": "default"
      },
      {
        "id": "ba78f847-5122-4e3f-bb7d-2b44ed3edac5",
        "name": "Pet Supplies",
        "type": "custom"
      }
    ]

Response from POST /categories
------------------------------
Example:

    {
      "id": "ba78f847-5122-4e3f-bb7d-2b44ed3edac5",
      "name": "Pet Supplies",
      "type": "custom"
    }

Response from DELETE /categories/<id>
-------------------------------------
On success:

    {
      "message": "Category deleted"
    }

On failure:

    {
      "error": "Category not found"
    }

------------------------------------------------------------
UML Sequence Diagram
------------------------------------------------------------

Use Case: Get All Categories
----------------------------
User Client         → Category Microservice
                    → Look up default categories
                    → Look up custom categories for user
Category Microservice → Returns JSON list of categories

Use Case: Add Custom Category
-----------------------------
User Client         → Category Microservice (POST userId + name)
                    → Generate UUID, save category
Category Microservice → Returns JSON with new category object

Use Case: Delete Category
-------------------------
User Client         → Category Microservice (DELETE with userId + category ID)
                    → Find user’s category list
                    → Remove category if matched
Category Microservice → Returns JSON success or error message

------------------------------------------------------------
Summary
------------------------------------------------------------
- All endpoints use standard REST over HTTP.
- All data is exchanged in JSON format.
- Use userId as a query parameter to access or manage a user's custom categories.
- The microservice stores data IN MEMORY; restarting the service clears all data.

If you have any issues integrating with this microservice, please contact me directly a day before the deadline so we can resolve it before the sprint ends.

