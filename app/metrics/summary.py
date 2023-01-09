from prometheus_client import Summary

__COMMON_LABELS = ('app_name', 'endpoint')

HTTP_REQUEST_LATENCY = Summary(\
        'http_request_latency', \
        'latebcy between http requests', \
        __COMMON_LABELS \
    )

