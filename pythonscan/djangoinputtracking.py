import os
import re

def scan_django_projects(directory):

    directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    
    for d in directories:

        if re.match(r'^[a-zA-Z0-9_-]+$', d):
            project_path = os.path.join(directory, d)
            

            settings_file = os.path.join(project_path, 'settings.py')
            if os.path.isfile(settings_file):

                views_directory = os.path.join(project_path, 'app_name', 'views')
                if os.path.isdir(views_directory):
                    for views_file in os.listdir(views_directory):
                        if views_file.endswith('.py'):
                            views_file_path = os.path.join(views_directory, views_file)

                            with open(views_file_path, 'r') as f:
                                for line in f:
                                    if 'request.POST' in line or 'request.GET' in line:

                                        print(f"Kullanıcı girdisi tespit edildi: {line.strip()}")
    

    for d in directories:
        new_directory = os.path.join(directory, d)
        if os.path.isdir(new_directory):
            scan_django_projects(new_directory)
