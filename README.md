# Integrative Project in Networks & Operating Systems - *Personal*

Welcome to my personal sandbox repository for the **Networks & Operating Systems Integrative Project**. Here, I've built a simple, dynamic web storefront showcasing products from the Robo-Clean ecosystem using Python only, no JavaScript needed.

---

## Project Overview

This project simulates an e-commerce-like experience for the **Robo-Clean** robot and its accessories:

- **Robo-Clean**: A household robot equipped with arms that picks up objects from the floor, keeping your home tidy with minimal effort.
- **Accessories include**:
  - Replacement **Filters**
  - **Dish-washing arms**, so Robo-Clean can handle water safely
  - **Fast-charging dock** that Robo-Clean automatically returns to after finishing its task
  - **Laser scanner** that enhances cleaning accuracy by detecting fine particles

All product data is stored in a structured `PRODUCTS` module. The storefront is dynamically generated via Python backend, without relying on client-side JavaScript.

---

## Repository Structure

```
proyecto-redes-sandbox/
├── src/
│   ├── index.py              # Constructs dynamic HTML page based on PRODUCTS
│   ├── simple_handler.py     # HTTP server handler serving HTML & assets
│   └── products.py           # PRODUCT list with attributes, specs, images, etc.
├── web-page/
│   └── style.css             # (Optional) CSS for styling the storefront
├── .gitignore
└── README.md                 # You are reading it now!
```

---

## How to Run

1. **Clone this repo**:
   ```bash
   git clone <your-repo-url>
   cd proyecto-redes-sandbox
   ```

2. **(Optional) Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Run the server**:
   ```bash
   python -m src.server
   ```

4. **Open your browser** and go to `http://127.0.0.1:8000/` to view the dynamic storefront.

---

## Key Features

- **Server-side rendered HTML** using Python only, no JavaScript required.
- **Modular code organization**:
  - `products.py`: Defines all product details
  - `index.py`: Generates the HTML from PRODUCTS
  - `simple_handler.py`: Serves HTML and optional CSS
- **Optional styling support** via an external CSS file (`web-page/style.css`) for improved UI.

---

## Future Enhancements

- **Visual enhancements**: include product images, detailed layout with cards or tables.
- **Dynamic routing**: add separate pages for product details or admin functionalities.
- **Inventory management**: add forms to update product stock or add new items.
- **Project polish**: improve `.gitignore`, write unit tests, and expand documentation (e.g., `/docs` folder).

---
