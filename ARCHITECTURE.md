# Python Pricing Scraper Framework Architecture

Based on the requirements, here is a proposed architecture for the Python pricing scraper framework, focusing on modularity, separation of concerns, and testability, utilizing `requests`, `BeautifulSoup`, and `pandas`.

## Proposed Architecture

The framework will be structured around a core set of interfaces and classes that define the interactions between different components. Supplier-specific logic will be isolated in dedicated modules, adhering to these interfaces.

## Key Components:

1.  **`Supplier` Interface:**
    *   Defines the contract for any specific supplier implementation.
    *   Composes instances of `Authenticator`, `PageFetcher`, and `Parser` specific to that supplier.
    *   Provides a method (e.g., `scrape()`) that orchestrates the fetching and parsing process for the specific supplier.

2.  **`Authenticator` Interface:**
    *   Defines methods for handling supplier login and maintaining an authenticated session (e.g., `login()`, `get_session()`).
    *   Specific implementations (`SupplierAAuthenticator`, `SupplierBAuthenticator`, etc.) will handle different authentication mechanisms using the `requests` library to manage sessions.

3.  **`PageFetcher` Interface:**
    *   Defines methods for fetching content from a supplier's website, handling pagination as needed (e.g., `fetch_pages(session)`).
    *   Takes an authenticated `requests.Session` object obtained from the `Authenticator`.
    *   Specific implementations (`SupplierAPageFetcher`, `SupplierBPageFetcher`, etc.) will implement supplier-specific pagination logic using `requests`.

4.  **`Parser` Interface:**
    *   Defines a method for parsing raw page content (HTML) into the unified data model (e.g., `parse(html_content)`).
    *   Specific implementations (`SupplierAParser`, `SupplierBParser`, etc.) will use `BeautifulSoup` to navigate and extract data from the HTML based on the supplier's layout.

5.  **`ProductData` Model:**
    *   A class or data structure (e.g., a simple class or a dictionary structure) representing the standardized product information (name, SKU, price, stock, etc.).
    *   Collections of `ProductData` instances can be managed using `pandas` DataFrames for easy manipulation and preparation for export.

6.  **`Exporter` Interface:**
    *   Defines a method for exporting the collected `ProductData` (e.g., `export(product_data)`).
    *   Specific implementations (`GoogleSheetsExporter`, `CSVExporter`, etc.) will handle writing the data to different destinations. The `GoogleSheetsExporter` would use the `gspread` library.

7.  **`ScraperFramework`:**
    *   The main orchestrator class.
    *   Takes instances of a specific `Supplier` implementation and an `Exporter` implementation during initialization.
    *   Provides a high-level method (e.g., `run()`) that calls the supplier's scrape method and then passes the resulting data to the exporter.

## Project Structure:

```
pricing_scraper/
├── src/
│   ├── framework/
│   │   ├── __init__.py
│   │   ├── interfaces.py  # Defines base interfaces (Authenticator, PageFetcher, Parser, Exporter, Supplier)
│   │   ├── data_model.py  # Defines the ProductData class/structure
│   │   └── scraper.py     # Defines the ScraperFramework class
│   └── suppliers/
│       ├── __init__.py
│       ├── supplier_a/
│       │   ├── __init__.py
│       │   ├── auth.py      # Supplier A Authenticator implementation
│       │   ├── fetcher.py   # Supplier A PageFetcher implementation
│       │   └── parser.py    # Supplier A Parser implementation
│       ├── supplier_b/
│       │   ├── __init__.py
│       │   ├── auth.py      # Supplier B Authenticator implementation
│       │   ├── fetcher.py   # Supplier B PageFetcher implementation
│       │   └── parser.py    # Supplier B Parser implementation
│       └── ... # Directory for each additional supplier
│   └── exporters/
│       ├── __init__.py
│       ├── google_sheets.py # GoogleSheetsExporter implementation
│       └── ... # Directory for other exporters (e.g., csv.py)
├── tests/
│   └── ... # Unit and integration tests
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt # Lists dependencies: requests, beautifulsoup4, pandas, gspread, etc.
└── main.py # Entry point: configures and runs the scraper
```

## Library Usage:

*   `requests`: Used within `Authenticator` and `PageFetcher` implementations for making HTTP requests and managing sessions.
*   `BeautifulSoup`: Used within `Parser` implementations for parsing HTML content.
*   `pandas`: Used for the `ProductData` model and potentially for aggregating and manipulating data before export.

## Testability and Reuse:

*   **Interfaces:** The use of interfaces allows for easy mocking of dependencies during testing. Each component can be tested in isolation.
*   **Separation of Concerns:** The clear division of responsibilities makes each part of the system simpler and easier to understand, test, and maintain.
*   **Modularity:** Supplier-specific logic is encapsulated, preventing cross-contamination and allowing new suppliers to be added without modifying core framework code.
*   **Dependency Injection:** The `ScraperFramework` depends on abstract interfaces (`Supplier`, `Exporter`), allowing specific implementations to be injected, which is beneficial for testing and flexibility.

## Relationships Diagram:

```mermaid
graph TD
    A[ScraperFramework] --> B[Supplier Interface]
    A --> C[Exporter Interface]
    B --> D[Authenticator Interface]
    B --> E[PageFetcher Interface]
    B --> F[Parser Interface]
    E --> D
    F --> G[ProductData Model]
    C --> G

    subgraph Suppliers
        B1[Supplier A Implementation] --> D1[Supplier A Authenticator]
        B1 --> E1[Supplier A PageFetcher]
        B1 --> F1[Supplier A Parser]
        D1 -- uses requests --> H[requests]
        E1 -- uses requests --> H
        F1 -- uses BeautifulSoup --> I[BeautifulSoup]
    end

    subgraph Exporters
        C1[Google Sheets Exporter] -- uses gspread --> J[gspread]
    end

    G -- uses pandas --> K[pandas]

    classDef interface fill:#f9f,stroke:#333,stroke-dasharray: 5 5;
    class B,C,D,E,F,G interface;