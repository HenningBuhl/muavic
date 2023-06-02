import os


def main():
    for lang in ['en', 'ar', 'de', 'el', 'es', 'fr', 'it', 'pt', 'ru']:  # de, 
        os.system(f'python get_data.py --root-path ./data --src-lang {lang}')


if __name__ == '__main__':
    main()
