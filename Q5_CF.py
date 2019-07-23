import base64

def hello_pubsub(event, context):
	import time
	from google.cloud import monitoring_v3
	client = monitoring_v3.MetricServiceClient()
	project_name = client.project_path('pe-training')
	interval = monitoring_v3.types.TimeInterval()
	now = time.time()
	interval.end_time.seconds = int(now)
	interval.end_time.nanos = int(
		(now - interval.end_time.seconds) * 10**9)
	interval.start_time.seconds = int(now - 60)
	interval.start_time.nanos = interval.end_time.nanos
	results = client.list_time_series(
		project_name,
		'metric.type = "compute.googleapis.com/instance/cpu/utilization"',
		interval,
		monitoring_v3.enums.ListTimeSeriesRequest.TimeSeriesView.FULL)
	for result in results:
		print(result)
		print('--')