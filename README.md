# Payment System CLI

A command-line payment system built with Python that supports multiple payment methods, automatic price adjustments, input validation, and CSV-based sales reporting.

This project was developed as a study project to practice object-oriented programming, separation of concerns, modular design, and CLI development.

## Features

* Multiple payment methods:

  * Pix — 5% discount
  * Credit Card — 10% interest
  * Debit Card — no discount or interest
  * Boleto — 2% discount
  * Cash — 15% discount
* Automatic final price calculation
* Input validation and error handling
* Terminal-based user interface
* Payment confirmation flow
* Sales history stored in a CSV file

## Screenshots

### Main Menu

![Main Menu](assets/menu.png)

### Payment Method Selection

![Payment Method Selection](assets/chose-option.png)

### Payment Summary

![Payment Summary](assets/resume.png)

### Payment Confirmation

![Payment Confirmation](assets/confirm-payment.png)

### CSV Sales Report

![CSV Sales Report](assets/csv-exemple.png)

## Project Structure

```text
payment-system-cli/
├── payments/
│   ├── __init__.py
│   └── methods.py              # Payment methods and business rules
│
├── reports/
│   ├── __init__.py
│   └── sales_report.py         # CSV sales report generation
│
├── utils/
│   ├── __init__.py
│   ├── input.py                # User input validation
│   ├── terminal_commands.py
│   └── ui.py                   # Terminal UI and formatting
│
├── main.py                     # Application entry point
├── requirements.txt
└── LICENSE
```

## Design

### Separation of Concerns

Business rules, terminal interface, input handling, and report generation are separated into dedicated modules.

### Object-Oriented Programming

Payment methods are represented by classes that use inheritance and polymorphism to encapsulate their respective pricing rules.

### Extensibility

The payment logic is structured so that additional payment methods can be introduced without concentrating every pricing rule in the application flow.

### CLI Design

The terminal interface provides a structured flow for selecting a payment method, reviewing the calculated amount, and confirming the transaction.

## Sales Report

Completed payments are stored in:

```text
sales_report.csv
```

Each record contains:

* date;
* payment method;
* original value;
* final value after the applicable discount or interest.

## Getting Started

### Prerequisites

* Python 3

### Installation

Clone the repository:

```bash
git clone https://github.com/omarcelodev/payment-system-cli.git
cd payment-system-cli
```

Optionally, create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Or on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python main.py
```

## Possible Improvements

* [ ] Add automated tests
* [ ] Allow sales reports to be viewed directly from the CLI
* [ ] Add coupons and promotional discounts
* [ ] Support additional report formats
* [ ] Improve currency and language configuration

## What I Learned

This project was developed to practice software development fundamentals in Python, including:

* object-oriented programming;
* inheritance and polymorphism;
* separation of responsibilities;
* modular code organization;
* input validation;
* file-based persistence with CSV;
* terminal application design.

## License

This project is licensed under the terms provided in the [LICENSE](LICENSE) file.
