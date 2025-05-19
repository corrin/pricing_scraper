import gspread
from google.oauth2.service_account import Credentials
from typing import List
from ..interfaces.exporter import Exporter
from ..models.product import ProductData
import os

class GoogleSheetsExporter(Exporter):
    """
    Exporter implementation for Google Sheets.
    """
    def __init__(self, spreadsheet_name: str, credentials_path: str):
        """
        Initializes the GoogleSheetsExporter.

        Args:
            spreadsheet_name: The name of the Google Sheet to export to.
            credentials_path: The path to the Google service account credentials JSON file.
        """
        self.spreadsheet_name = spreadsheet_name
        self.credentials_path = credentials_path
        self.client = self._authenticate()

    def _authenticate(self) -> gspread.Client:
        """
        Authenticates with Google Sheets using service account credentials.

        Returns:
            A gspread Client instance.
        """
        if not os.path.exists(self.credentials_path):
            raise FileNotFoundError(f"Credentials file not found at {self.credentials_path}")

        scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        credentials = Credentials.from_service_account_file(
            self.credentials_path,
            scopes=scopes
        )
        return gspread.authorize(credentials)

    def export_data(self, product_data: List[ProductData]):
        """
        Exports the list of ProductData objects to the specified Google Sheet.

        Args:
            product_data: A list of ProductData objects to export.
        """
        try:
            spreadsheet = self.client.open(self.spreadsheet_name)
            worksheet = spreadsheet.sheet1 # Assuming data is exported to the first sheet

            # Prepare data for export (e.g., list of lists)
            # Assuming ProductData has attributes like name, price, url
            data_to_export = [["Name", "Price", "URL"]] # Header row
            for product in product_data:
                data_to_export.append([product.name, product.price, product.url])

            # Clear existing content and write new data
            worksheet.clear()
            worksheet.update(data_to_export)

            print(f"Successfully exported data to Google Sheet: {self.spreadsheet_name}")

        except gspread.exceptions.SpreadsheetNotFound:
            print(f"Error: Google Sheet '{self.spreadsheet_name}' not found.")
        except Exception as e:
            print(f"An error occurred during export: {e}")