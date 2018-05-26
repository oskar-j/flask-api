#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.factory import create_app
from api.utils.config import DevelopmentConfig, ProductionConfig, SqlLiteDevelopmentConfig, TestingConfig
import os


settings = {'IP_ADDRESS': "0.0.0.0",
            'PORT': 5000}


if __name__ == '__main__':

    if 'IP_ADDRESS' in os.environ:
        print('Setting host IP address to {}'.format(os.environ.get('IP_ADDRESS')))
        settings['IP_ADDRESS'] = os.environ.get('IP_ADDRESS')

    if 'PORT' in os.environ:
        print('Setting host PORT to {}'.format(os.environ.get('PORT')))
        settings['PORT'] = os.environ.get('PORT')

    if 'DEVTEST_CONF' in os.environ:

        config = os.environ.get('DEVTEST_CONF')

        print('Reading configuration set {}'.format(config))

        if config in ['PROD', 'PRODUCTION']:
            app = create_app(ProductionConfig)
            app.run(port=settings['PORT'], host=settings['IP_ADDRESS'],
                    use_reloader=ProductionConfig.USE_RELOADER)
        elif config in ['DEV', 'DEVEL', 'DEVELOPMENT']:
            app = create_app(DevelopmentConfig)
            app.run(port=settings['PORT'], host=settings['IP_ADDRESS'],
                    use_reloader=DevelopmentConfig.USE_RELOADER)
        elif config in ['TEST', 'TESTING']:
            app = create_app(TestingConfig)
            app.run(port=settings['PORT'], host=settings['IP_ADDRESS'],
                    use_reloader=TestingConfig.USE_RELOADER)
        elif config == 'SQLITE':
            app = create_app(SqlLiteDevelopmentConfig)
            app.run(port=settings['PORT'], host=settings['IP_ADDRESS'],
                    use_reloader=SqlLiteDevelopmentConfig.USE_RELOADER)

    else:
        app = create_app(DevelopmentConfig)
        app.run(port=settings['PORT'], host=settings['IP_ADDRESS'], use_reloader=True)
