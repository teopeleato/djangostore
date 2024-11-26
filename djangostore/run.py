"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangostore.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Verifica si hay argumentos en sys.argv
    if len(sys.argv) == 1:
        # Si no se pasan argumentos, añade los predeterminados
        sys.argv += ["runserver", "0.0.0.0:8000"]
    execute_from_command_line(sys.argv)
if __name__ == "__main__":
    main()
