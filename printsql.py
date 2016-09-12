class SQL(object):
    def process_response(self, request, response):
        from django.db import connection
        import json
        for i, q in enumerate(connection.queries):
            print '{}) {} {}'.format(i+1, q['time'], q['sql'])
        return response
