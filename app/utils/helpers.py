def build_pagination(base_url, total, offset, limit):
    next_url = None
    previous_url = None

    if offset + limit < total:
        next_url = f"{base_url}?offset={offset + limit}&limit={limit}"

    if offset > 0:
        previous_url = f"{base_url}?offset={offset - limit}&limit={limit}"

    return next_url, previous_url


def build_base_url(request):
    port = request.headers.get("x-forwarded-port", "")
    host = request.headers.get("host", "").split(":")[0]
    scheme = request.headers.get("x-forwarded-proto", request.url.scheme)
    return f"{scheme}://{host}:{port}" if port else f"{scheme}://{host}"
