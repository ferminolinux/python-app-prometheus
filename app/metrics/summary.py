from prometheus_client import Summary

__COMMON_LABELS = ('app_name', 'endpoint')

HTTP_REQUEST_LATENCY = Summary(\
        'HTTP_REQUEST_LATENCY', \
        'latebcy between http requests', \
        __COMMON_LABELS \
    )

