from flask import jsonify,make_response

class Response:

    @staticmethod
    def error(message, code):
        response = make_response(
        jsonify({
            'data': {},
            'meta': {
                'message': message,
                'code': code
            }
            }),
            code
        )
        response.headers["Content-Type"] = "application/json"
        return response

    @staticmethod
    def success(data):
        response = make_response(
        jsonify({
            'data': data,
            'meta': {
                'message': 'Success',
                'code': 200
            }
            }),
            200
        )
        response.headers["Content-Type"] = "application/json"
        return response
