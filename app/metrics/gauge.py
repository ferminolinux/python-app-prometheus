from prometheus_client import Gauge

__COMMON_LABELS = ('app_name', 'endpoint')

HTTP_REQUEST_IN_PROGRESS = Gauge(\
        'http_request_in_progress', \
        'total requests in progress', \
        __COMMON_LABELS \
    )