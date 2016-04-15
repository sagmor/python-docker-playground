def formatter(payload):
    result = {
            'id': payload['Id'][:12],
            'state': payload['State']
            }

    if type(result['state']) is dict:
        result['state'] = result['state']['Status']

    if 'Name' in payload:
        result['name'] = payload['Name'][1:]
    elif 'Names' in payload:
        result['name'] = payload['Names'][0][1:]

    return result
