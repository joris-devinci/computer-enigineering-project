# Software Requirements Specification

## Shoe Store API

## 1. Introduction

This document explains the requirements for our shoe store backend API. It is part of the first sprint documentation.

Our project is a simple online shoe store. The main idea is that a customer should be able to browse shoes, add them to a cart, and place an order.

The system should allow users to:

- View available shoes.
- Register and log in.
- Add shoes to a cart.
- View their cart.
- Place an order.
- View their previous orders.

This SRS focuses on what the software should do. The technical design and code structure will be explained more in the SDD.

## 2. System Overview

The project is a backend system for a small shoe store. It will be built as an API using Python and FastAPI.

The main things we need to store in the system are:

- User
- Shoe
- Cart
- Cart item
- Order
- Order item

Each shoe has information such as its name, price, color, brand, and category.

## 3. Users

The main user of the system is a customer.

A customer should be able to:

- Register an account.
- Log in.
- Browse shoes.
- Add shoes to a cart.
- Checkout.
- See previous orders.

## 4. Functional Requirements

### 4.1 Shoe Collection

- The system should show a list of available shoes.
- Each shoe should have an id, name, price, color, brand, and category.
- Shoe color should be one of: green, yellow, white, black.
- Shoe brand should be one of: Nike, Adidas.
- Shoe category should be one of: padel, tennis, hiking.

### 4.2 User Account

- The system should allow a new user to register.
- A user should have firstname, lastname, email, postcode, and house number.
- The system should allow a user to log in.
- The system should reject invalid login details.

### 4.3 Cart

- The system should allow a user to add a shoe to their cart.
- A cart item should contain a shoe and an amount.
- The amount must be greater than zero.
- The system should allow a user to view their cart.
- A user can have one active cart.

### 4.4 Orders

- The system should allow a user to place an order.
- An order should be created from the user's cart.
- An order should contain one or more order items.
- Each order should have a timestamp.
- The system should allow a user to view previous orders.

### 4.5 Error Handling

- The system should show an error if a user does not exist.
- The system should show an error if a shoe does not exist.
- The system should show an error if the cart is empty during checkout.
- The system should show an error if required data is missing.

## 5. API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/collection` | Get all shoes |
| POST | `/user/register` | Register a user |
| POST | `/user/login` | Log in a user |
| POST | `/cart` | Add a shoe to the cart |
| GET | `/cart` | View the cart |
| POST | `/order` | Place an order |
| GET | `/order` | View previous orders |

## 6. Data Requirements

### User

- id
- firstname
- lastname
- email
- postcode
- house number

### Shoe

- id
- name
- price
- color
- brand
- category

### Cart

- id
- user id

### Cart Item

- id
- amount
- cart id
- shoe id

### Order

- id
- timestamp
- user id

### Order Item

- id
- amount
- order id
- shoe id

## 7. Non-Functional Requirements

- The API should return data in JSON format.
- The API should give clear error messages.
- The API should validate user input.
- A user should only access their own cart and orders.
- The code should be organized in a way that is easy for the team to understand and update later.

## 8. Acceptance Criteria

For this first sprint, we can consider the SRS requirements successful if:

- A user can register.
- A user can log in.
- A user can view shoes.
- A user can add shoes to a cart.
- A user can view their cart.
- A user can place an order.
- A user can view previous orders.
- Invalid actions return clear errors.

## 9. Out of Scope

The following features are not required for this sprint, because they would make the project too large at this stage:

- Payment system.
- Shipping system.
- Admin dashboard.
- Product images.
- Discounts.
- Password reset.
