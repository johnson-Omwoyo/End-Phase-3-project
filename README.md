# Pet Vaccination Management System

## Welcome!

This Pet Vaccination Management System helps manage pet vaccination records effectively. Follow the instructions below to get started.

## Files Overview

1. **`interface.py`**: The main application file. This is where you will interact with the system to manage pets, owners, and vaccines.
2. **`tables.py`**: Contains the database schema and models. This file sets up the necessary tables for owners, pets, and vaccines in the SQLite database.

## Getting Started

### 1. Running the Application

- **File to Run**: `interface.py`
- **When to Run**: After setting up your environment and installing the necessary packages.
- **What to Expect**: The application will launch a command-line interface where you can manage pets and vaccines. The first time you run it, it will create a SQLite database named `Vaccinations.db`.

### 2. Database Initialization

- **File to Run**: `tables.py` (only needed once if the database already exists)
- **When to Run**: Before you start using the application, or if you want to reset the database.
- **What to Expect**: This will create the necessary tables in the SQLite database. You should see console output indicating that the tables have been created.

## How to Use

### Launching the Application

- Start `interface.py` to see the menu.
- You can choose options to manage pets, owners, and vaccines. Follow the prompts as they guide you through each function.

### Navigating the Menu

- The menu will present options to:
  - Add a pet
  - Search for pets
  - Manage vaccines
  - Exit the application
- It’s user-friendly and designed for ease of use, so you can focus on managing your pets’ health.

## Functionality Demo

For a demonstration of the application’s features, check out this video: [Demo Video](https://drive.google.com/file/d/1S9DblJr1aWEwbsjmrPx3_z8y4ttN2lW-/view?usp=drive_link).

## Code Structure

### Key Classes

- **Owner**: Manages information related to pet owners.
- **Pet**: Contains details about pets, including their vaccination status.
- **Vaccine**: Represents vaccines available for pets.

## Contribution

Contributions are welcome! Feel free to report bugs, suggest features, or submit pull requests.

This project is open-source and available

If you have questions or need help, please reach out through the project’s GitHub page. Happy managing!
