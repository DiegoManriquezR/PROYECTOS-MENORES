
import os, sys
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestor_reservas.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError('Django no está instalado. Instálalo con: pip install django mysqlclient') from exc
    execute_from_command_line(sys.argv)
