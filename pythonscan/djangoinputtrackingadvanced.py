import os
import re

def scan_django_projects(directory):
    # Verilen dizindeki tüm dizinleri al
    directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    
    for d in directories:

        if re.match(r'^[a-zA-Z0-9_-]+$', d):
            project_path = os.path.join(directory, d)
            

            settings_file = os.path.join(project_path, 'settings.py')
            if os.path.isfile(settings_file):

                for root, dirs, files in os.walk(project_path):
                    for file in files: # eğer dosya py ile bitiyorsa al
                        if file.endswith('.py'):
                            views_file_path = os.path.join(root, file)

                            with open(views_file_path, 'r') as f:
                                for line in f:
                                    #kullanıcıdan input alıyor mu diye kontrol et
                                    if 'request.POST' in line or 'request.GET' in line:

                                        print(f"Kullanıcı girdisi tespit edildi: {line.strip()}")
                                    if '.cleaned_data' in line:
                                        # from verisi var mı diye tespit et
                                        print(f"Form verileri tespit edildi: {line.strip()}")
                                    if 'Model.objects.create(' in line or 'Model.objects.update(' in line:
                                        #Veritabanı modeli var mı diye bak
                                        print(f"Veritabanı kaydı tespit edildi: {line.strip()}")



    for d in directories:
        new_directory = os.path.join(directory, d)
        if os.path.isdir(new_directory):
            scan_django_projects(new_directory)
