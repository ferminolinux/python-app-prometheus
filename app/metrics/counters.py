from prometheus_client import Counter

__COMMON_LABELS = ('app_name', 'endpoint', 'status_code')

HTTP_REQUESTS_TOTAL = Counter('http_requests', 'total of http request per endpoint', __COMMON_LABELS)

HTTP_EXCEPTIONS_TOTAL = Counter('http_exceptions', 'total of exceptions per endpoint', __COMMON_LABELS)