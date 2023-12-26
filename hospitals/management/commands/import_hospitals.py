# hospitals/management/commands/import_hospitals.py
import pandas as pd
from django.core.management.base import BaseCommand
from hospitals.models import Hospital

class Command(BaseCommand):
    help = 'Import hospitals from Excel file'

    def handle(self, *args, **options):
        excel_file_path = 'C:\\hospital_project\\mh(3).xlsx'  # Replace with the actual path of your Excel file

        # Clear existing records
        Hospital.objects.all().delete()

        try:
            hospitals_data = pd.read_excel(excel_file_path)

            for _, row in hospitals_data.iterrows():
                Hospital.objects.create(
                    name=row['Hospital_Name'],
                    address=row['Address'],
                    phone_number=row['Phone_Number'],
                    type_of_hospital=row['Type_of_hosp'],
                    latitude=row['Latitude'],  # Use the actual column name in your Excel file
                    longitude=row['Longitude']  # Use the actual column name in your Excel file
                )

            self.stdout.write(self.style.SUCCESS('Hospitals imported successfully!'))
        except pd.errors.EmptyDataError:
            self.stdout.write(self.style.WARNING('The Excel file is empty.'))
        except pd.errors.ParserError as e:
            self.stdout.write(self.style.ERROR(f'Error parsing Excel file: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An unexpected error occurred: {e}'))
