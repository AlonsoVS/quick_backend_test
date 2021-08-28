        Prueba para Backend Quick
    Api para administrar facturación

    Caracteristicas:
        Ver Lista de Productos
        Añadir y Borrar Nuevos Productos
        Ver Lista de Clientes
        Añadir y Borrar Nuevos Clientes
        Ver Lista de Facturas
        Añadir y Borrar Nuevas Facturas
        Authenticación con JSON Web Token

    Construido con:
        Python/Django

    Configurar en modo de desarrollo:

        Prerequisitos:
            pipenv
            $pip install --user pipenv
            o
            $brew install pipenv
            
            $pipenv --three
            $pipenv shell

        Instalacion local:
            Clonar repositorio:
                git clone https://github.com/AlonsoVS/quick_backend_test.git
            Instalar dependencias:
                pipenv install

        Configurar base de datos local:
            En quick_backend_test/settings.py
                    DATABASES = {
                        'default': {
                            'ENGINE': 'django.db.backends.postgresql_psycopg2',
                            'NAME': 'nombre_de_bsae_de_datos',
                            'USER': 'usuario_de_base_de_datos',
                            'PASSWORD': 'contraseña_de_base_de_datos',
                            'HOST': 'localhost',
                            'PORT': 'puerto_de_base_de_datos',
                        }
                    }

        Configurar clave secreta:
            En quick_backend_test/settings.py:
                SECRET_KEY = "clave_secreta"
        
        Crear Schemas en base de datos:
            $python manage.py makemigrations
            $python manage.py migrate
        Ejecutar:
            $python manage.py runserver
