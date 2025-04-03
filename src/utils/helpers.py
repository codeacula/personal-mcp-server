def format_response(data, status_code=200):
    return {
        'statusCode': status_code,
        'body': data
    }

def handle_error(message, status_code=400):
    return format_response({'error': message}, status_code)