import csv
from django.core.management.base import BaseCommand
from home.models import Admission 
class Command(BaseCommand):
    help = 'Export admission data to CSV'

    def handle(self, *args, **kwargs):
        filename = 'admission_data.csv'
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow([
                'Name', 'Address', 'Contact', 'Mail', 'DOB', 'Gender',
                'Occupation', 'Guardian Name', 'Guardian Occupation', 'Guardian Contact',
                'Institute1', 'Class/Sem1', 'Stream1', 'Passing Year1', 'Percentage1',
                'Institute2', 'Class/Sem2', 'Stream2', 'Passing Year2', 'Percentage2',
                'Institute3', 'Class/Sem3', 'Stream3', 'Passing Year3', 'Percentage3',
                'Subjects', 'References', 'Ref Name'
            ])

            # Write data rows
            for entry in Admission.objects.all():
                writer.writerow([
                    entry.name, entry.address, entry.contact, entry.mail, entry.dob, entry.gender,
                    entry.occupation, entry.guardian_name, entry.guardian_occupation, entry.guardian_contact,
                    entry.institute1, entry.class_sem1, entry.stream1, entry.passing_year1, entry.percentage1,
                    entry.institute2, entry.class_sem2, entry.stream2, entry.passing_year2, entry.percentage2,
                    entry.institute3, entry.class_sem3, entry.stream3, entry.passing_year3, entry.percentage3,
                    entry.subjects, entry.references, entry.refname
                ])
        
        self.stdout.write(self.style.SUCCESS(f'Data exported successfully to {filename}'))

# python3 manage.py export_admissions
# To run this command, use the following in your terminal: